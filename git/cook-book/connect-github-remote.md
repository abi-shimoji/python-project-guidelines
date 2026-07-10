# GitHubリポジトリへ接続したい

状況:

- ローカルリポジトリを GitHub リポジトリへ push したい
- `origin` の URL を GitHub に向けたい
- SSH または HTTPS の接続設定を確認したい

前提:

- GitHub 側にリポジトリが作成済みである
- Git のユーザー名とメールアドレスが設定済みである
- SSH 接続は `gh` コマンドで設定することを推奨する
- GitHub ではデフォルトブランチ名として `main` を使う運用を推奨する
- 既存リポジトリで `master` がデフォルトの場合は、`main` にリネームしてから連携する

SSH 設定を `gh` で行う場合:

```bash
gh auth login
gh auth status
ssh -T git@github.com
```

手動で SSH 設定する場合は、公開鍵を GitHub に登録してから接続確認する。

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
cat ~/.ssh/id_ed25519.pub
ssh -T git@github.com
```

確認:

```bash
git status
git remote -v
git branch --show-current
```

現在のブランチが `master` の場合は、ローカルのデフォルトブランチを `main` に変更する。

```bash
git branch -m master main
```

SSH で `origin` を追加する:

```bash
git remote add origin git@github.com:<owner>/<repository>.git
```

既存の `origin` を SSH に変更する:

```bash
git remote set-url origin git@github.com:<owner>/<repository>.git
```

HTTPS を使う場合:

```bash
git remote set-url origin https://github.com/<owner>/<repository>.git
```

設定確認:

```bash
git remote -v
```

初回 push:

```bash
git push -u origin main
```

GitHub 側の Default branch を `main` に変更する。

```bash
gh repo edit --default-branch main
```

作業ブランチを push する場合:

```bash
git push -u origin feature/example
```

注意:

- 認証トークンや秘密情報をコミットしない
- `master` を削除する場合は、GitHub 側の Default branch が `main` に変更済みであることを確認する
- push 前に `git status` と `git diff` を確認する
- 共有ブランチへ強制 push しない
- 詳細な手順は `../GITHUB_INTEGRATION_GUIDE.md` を参照する
