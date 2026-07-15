# Ubuntu 公開サーバーの基本ハードニング

Ubuntu Server 上で公開 Web サーバーを構築する際の基本的な確認と設定例を示す。方針は [公開サーバーセキュリティガイドライン](../PUBLIC_SERVER_SECURITY_GUIDELINE.md) を参照する。

この手順は Ubuntu Server 24.04 LTS を主な想定とする。クラウドのセキュリティグループ、OS イメージ、SSH 設定、利用中の構成管理ツールによって手順が異なるため、適用前に差分を確認する。

## 1. 作業前の準備

事前に次を確認する。

- クラウドコンソールやシリアルコンソールなど、SSH 以外の復旧経路がある
- 管理者の固定グローバル IP または VPN の CIDR が分かっている
- 公開するポートが決まっている
- スナップショットまたはバックアップを取得している
- SSH の既存セッションを維持したまま、別セッションで接続試験できる

この手順では、次のプレースホルダーを実際の値へ置き換える。

- `<ADMIN_CIDR>`: 管理元の IP アドレスまたは CIDR。例: `203.0.113.10/32`
- `<ADMIN_USER>`: 公開鍵認証を確認済みの管理ユーザー
- `<SERVER_NAME>`: サーバーの DNS 名

## 2. 現在の状態を確認する

OS とカーネルを確認する。

```bash
cat /etc/os-release
uname -r
```

待受ポートと実行中サービスを確認する。

```bash
sudo ss -lntup
systemctl --type=service --state=running
```

ファイアウォールの状態を確認する。

```bash
sudo ufw status verbose
```

クラウド環境では、セキュリティグループやネットワーク ACL も管理画面または構成管理コードで確認する。

## 3. OS を更新する

パッケージ一覧を更新し、適用予定を確認してから更新する。

```bash
sudo apt update
apt list --upgradable
sudo apt upgrade
```

再起動の要否を確認する。

```bash
test -f /var/run/reboot-required && cat /var/run/reboot-required
```

再起動が必要な場合は、サービス影響と復旧手順を確認してからメンテナンス時間内に実施する。

## 4. UFW を設定する

SSH を制限する前に、`<ADMIN_CIDR>` が現在の接続元と一致することを確認する。クラウド側ファイアウォールにも同じ許可範囲を設定する。

初期方針を設定する。

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

UFW を有効化する前に、管理用 SSH を許可する。

```bash
sudo ufw allow proto tcp from <ADMIN_CIDR> to any port 22
```

Web サーバーとして HTTP と HTTPS を公開する場合だけ許可する。

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

ルールと IPv6 の設定を確認する。

```bash
sudo ufw status numbered
grep '^IPV6=' /etc/default/ufw
```

IPv6 を使用する場合は `IPV6=yes` であることを確認し、IPv6 側も同じ方針で制御する。IPv6 を無効化する場合は、UFW だけでなく OS とクラウド側の設定を含めて設計する。

ログを有効にしてから UFW を有効化する。

```bash
sudo ufw logging medium
sudo ufw enable
sudo ufw status verbose
```

既存の SSH セッションを閉じず、別の端末から SSH と Web サービスへの接続を確認する。接続不能になった場合は、事前に確保したコンソールからルールを修正する。緊急時に UFW を一時停止する場合は次を使用し、復旧後に原因を修正して再度有効化する。

```bash
sudo ufw disable
```

## 5. SSH をハードニングする

先に公開鍵認証で接続できることを確認する。

```bash
ssh -o PreferredAuthentications=publickey <ADMIN_USER>@<SERVER_NAME>
```

Ubuntu の OpenSSH 設定は、各項目で最初に読み込まれた値が使われる。既存の drop-in より先に読み込ませるため、`/etc/ssh/sshd_config.d/00-local-hardening.conf` を作成する。

```bash
sudoedit /etc/ssh/sshd_config.d/00-local-hardening.conf
```

次の内容を設定する。`AllowUsers` を使う場合は、運用に必要な全管理ユーザーを列挙する。

```text
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
KbdInteractiveAuthentication no
AllowUsers <ADMIN_USER>
```

設定ファイルの構文と、実際に適用される値を確認する。

```bash
sudo sshd -t
sudo sshd -T | grep -E 'permitrootlogin|pubkeyauthentication|passwordauthentication|kbdinteractiveauthentication|allowusers'
```

構文エラーがない場合だけ設定を再読み込みする。

```bash
sudo systemctl reload ssh.service
sudo systemctl status ssh.service --no-pager
```

既存セッションを維持したまま、別端末から公開鍵認証で再接続する。接続確認が完了するまで既存セッションを閉じない。

## 6. セキュリティ更新を自動化する

Ubuntu Server では `unattended-upgrades` が標準で導入されている場合がある。存在と設定を確認する。

```bash
dpkg -s unattended-upgrades
systemctl status apt-daily.timer apt-daily-upgrade.timer --no-pager
grep -R 'APT::Periodic' /etc/apt/apt.conf.d/
```

未導入の場合はインストールする。

```bash
sudo apt install unattended-upgrades
```

実行前の確認を行う。

```bash
sudo unattended-upgrade --dry-run --debug
```

本番では、自動再起動の可否、更新失敗の通知、保留パッケージ、サードパーティーリポジトリの扱いを別途定める。

## 7. 不要なサービスを停止する

待受ポートとサービスを再確認する。

```bash
sudo ss -lntup
systemctl --type=service --state=running
```

不要と判断したサービスは、依存関係と影響を確認してから停止・無効化する。

```bash
sudo systemctl disable --now <SERVICE_NAME>
```

パッケージを削除する場合は、削除対象と依存関係を確認してから実行する。

```bash
sudo apt remove <PACKAGE_NAME>
```

## 8. ログを確認する

SSH の認証ログを確認する。

```bash
sudo journalctl -u ssh.service --since today
```

UFW のログを確認する。

```bash
sudo journalctl -k --grep=UFW --since today
```

自動更新のログを確認する。

```bash
sudo journalctl -u unattended-upgrades.service --since today
sudo ls -l /var/log/unattended-upgrades/
```

ログはサーバー外へ転送し、保存期間、容量制限、閲覧権限、アラート条件を定める。

## 9. 公開後の確認

サーバー上で待受ポートとファイアウォールを確認する。

```bash
sudo ss -lntup
sudo ufw status verbose
```

HTTPS の応答と証明書を確認する。

```bash
curl --fail --head https://<SERVER_NAME>/
openssl s_client -connect <SERVER_NAME>:443 -servername <SERVER_NAME> </dev/null
```

管理ネットワーク外から、意図したポートだけに接続できることを確認する。ポートスキャンは、自社が所有または明示的な許可を得た対象にのみ実施する。

公開後は、次を定期的に確認する。

- OS とパッケージの更新状況
- 公開ポートとクラウド側ファイアウォール
- 管理ユーザーと SSH 公開鍵
- TLS 証明書の期限と自動更新
- ログ、監視、アラート
- バックアップと復元試験

## 参考資料

- [Ubuntu Server documentation: Firewall](https://documentation.ubuntu.com/server/how-to/security/firewalls/)
- [Ubuntu Server documentation: OpenSSH server](https://documentation.ubuntu.com/server/how-to/security/openssh-server/)
- [Ubuntu Server documentation: Automatic updates](https://documentation.ubuntu.com/server/how-to/software/automatic-updates/)
