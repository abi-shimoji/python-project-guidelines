# GitHub連携ガイド

この文書は、ローカルの Git リポジトリと GitHub リポジトリを連携するための基本手順をまとめる。

## 1. 基本方針

- GitHub との接続方式は SSH を推奨する
- SSH 設定は GitHub CLI の `gh` コマンドを使う方法を推奨する
- デフォルトブランチ名は `main` を推奨する
- リモート名は原則として `origin` を使う
- push 前にブランチ名、リモート URL、差分を確認する
- 認証情報やトークンをリポジトリに含めない
- 共有ブランチへの履歴改変は避ける

## 2. 事前確認

Git のユーザー設定を確認する。

```bash
git config --global user.name
git config --global user.email
```

未設定の場合:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

現在のリモート設定を確認する。

```bash
git remote -v
```

デフォルトブランチ名を確認する。

```bash
git branch --show-current
git remote show origin
```

## 3. デフォルトブランチ名

GitHub では、新規リポジトリのデフォルトブランチ名として `main` を使う運用を推奨する。このガイドでも、デフォルトブランチ名は `main` に統一する。

既存リポジトリや古いプロジェクトでは `master` がデフォルトブランチになっている場合がある。その場合は、ローカルのデフォルトブランチを `main` にリネームし、GitHub 側のデフォルトブランチも `main` に変更する。

現在のブランチが `master` の場合、ローカルブランチ名を `main` に変更する。

```bash
git branch --show-current
git branch -m master main
```

`main` を GitHub へ push し、追跡先を設定する。

```bash
git push -u origin main
```

GitHub のリポジトリ設定で Default branch を `main` に変更する。

GitHub CLI を使える場合は、次のように変更できる。

```bash
gh repo edit --default-branch main
```

GitHub 側のデフォルトブランチを `main` に変更した後、不要になったリモートの `master` を削除する。

```bash
git push origin --delete master
```

> [!WARNING]
> `master` を削除する前に、GitHub 側の Default branch が `main` に変更済みであることを確認する。
> 他の開発者が `master` を使っている場合は、事前に周知してから変更する。

## 4. SSHで接続する

SSH 接続の設定は、GitHub CLI の `gh` コマンドを使う方法を推奨する。手動で SSH キーを作成して GitHub に登録する方法も利用できる。

### 4.1 ghコマンドを使う方法（推奨）

GitHub CLI の認証を開始する。

```bash
gh auth login
```

対話中の選択は、基本的に次を選ぶ。

- `GitHub.com`
- `SSH`
- GitHub へ SSH key をアップロードする

認証状態を確認する。

```bash
gh auth status
```

SSH 接続を確認する。

```bash
ssh -T git@github.com
```

補足:

- `gh auth login` は SSH キーの作成や GitHub への登録を補助できる
- 既存の SSH キーを使うか、新しく作成するかは対話中に選択できる
- 以降のリモート URL は `git@github.com:<owner>/<repository>.git` 形式を使う

### 4.2 手動でSSHキーを設定する方法

既存の SSH キーを確認する。

```bash
ls ~/.ssh
```

SSH キーを作成する。

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

公開鍵を表示し、GitHub の SSH keys に登録する。

```bash
cat ~/.ssh/id_ed25519.pub
```

接続確認:

```bash
ssh -T git@github.com
```

## 5. GitHubリポジトリをリモートに設定する

まだリモートがない場合:

```bash
git remote add origin git@github.com:<owner>/<repository>.git
```

既存の `origin` を変更する場合:

```bash
git remote set-url origin git@github.com:<owner>/<repository>.git
```

設定確認:

```bash
git remote -v
```

## 6. 初回push

現在のブランチ名を確認する。

```bash
git branch --show-current
```

初回 push:

```bash
git push -u origin main
```

作業ブランチを push する場合:

```bash
git push -u origin feature/example
```

`-u` を付けると、ローカルブランチとリモートブランチの追跡関係が設定される。

## 7. 日常運用

リモートの更新を取得する。

```bash
git fetch origin
```

デフォルトブランチを fast-forward のみで更新する。

```bash
git switch main
git pull --ff-only
```

作業ブランチを push する。

```bash
git push
```

追跡先を確認する。

```bash
git branch -vv
```

## 8. Pull Request運用

作業ブランチを作成する。

```bash
git switch main
git pull --ff-only
git switch -c feature/example
```

コミット後に push する。

```bash
git push -u origin feature/example
```

GitHub 上で Pull Request を作成する。

PR 作成前の確認:

```bash
git status
git diff origin/main...HEAD
git log --oneline --decorate origin/main..HEAD
```

確認すること:

- PR に含める差分が意図した範囲か
- コミット単位がレビューしやすいか
- コミットメッセージが `COMMIT_MESSAGE_GUIDE.md` に沿っているか
- 不要なファイルや秘密情報が含まれていないか

## 9. HTTPSを使う場合

HTTPS の URL を設定する。

```bash
git remote set-url origin https://github.com/<owner>/<repository>.git
```

HTTPS ではパスワードではなく Personal Access Token や GitHub CLI の認証を使う。

> [!WARNING]
> Personal Access Token をファイルやコミットに含めない。
> 誤って含めた場合は、即座にトークンを失効させる。

## 10. よくある確認コマンド

リモート URL 確認:

```bash
git remote -v
```

現在のブランチと追跡先確認:

```bash
git branch -vv
```

リモートブランチ一覧:

```bash
git branch -r
```

push 先を確認する:

```bash
git remote show origin
```

## 11. 注意

- `git push --force` ではなく `git push --force-with-lease` を使う
- 共有ブランチで強制 push しない
- GitHub 上の protected branch ルールを尊重する
- リポジトリ URL を変更した後は `git remote -v` で必ず確認する
