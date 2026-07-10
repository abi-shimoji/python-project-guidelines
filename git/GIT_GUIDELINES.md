# Gitガイドライン

このガイドラインは、開発時に Git を安全かつ一貫して運用するための基本方針をまとめる。

## 1. 基本方針

- 変更は小さく区切ってコミットする
- `main` や `master` への直接コミットは避け、作業ブランチで開発する
- コミット前に差分を確認し、不要な変更を含めない
- 共有済みブランチの履歴改変は原則として避ける
- 強制 push が必要な場合は `--force` ではなく `--force-with-lease` を使う

## 2. ブランチ運用

### 2.1 ブランチ作成

新しい作業は目的ごとにブランチを切る。

例:

- `feature/add-login-api`
- `fix/null-check-on-user-service`
- `docs/update-git-guide`
- `chore/update-ci-config`

推奨:

- 1 ブランチ 1 目的を守る
- 長期間放置するブランチを減らす
- レビューしやすい単位で PR を分ける

### 2.2 ベースブランチの更新

作業開始前や PR 更新前には、ベースブランチの最新状態を取り込む。

```bash
git switch main
git pull --ff-only
git switch feature/add-login-api
git rebase main
```

`pull --ff-only` によって、意図しないマージコミットの混入を防ぎやすくする。

## 3. ステージングとコミット

### 3.1 ステージング

コミット前には変更を丸ごと追加せず、差分単位で確認する。

```bash
git status
git diff
git add -p
```

推奨:

- `git add .` を常用せず、意図した変更だけをステージする
- 生成物、ログ、秘密情報が含まれていないか確認する
- フォーマット変更と機能変更は可能な限り分ける

### 3.2 コミット

コミットは「後から履歴を読んだときに意味が分かる最小単位」で行う。

- 1 つのコミットに複数の目的を混ぜない
- リファクタリングと挙動変更は分ける
- 失敗時に戻しやすい粒度を意識する
- コミットメッセージは `COMMIT_MESSAGE_GUIDE.md` に従う
- コミット単位の詳細は `COMMIT_UNIT_GUIDE.md` に従う

## 4. 取得・統合方針

### 4.1 fetch と pull

- まず `git fetch` でリモート状況を確認する
- 自動マージを避けたい場合は `git pull` より `fetch + rebase` を使う

例:

```bash
git fetch origin
git rebase origin/main
```

### 4.2 merge と rebase

- ローカル作業ブランチの追従には `rebase` を優先する
- 履歴をそのまま残したい統合には `merge` を使う
- 公開済みブランチを安易に `rebase` しない

判断基準:

- 自分だけが使っている作業ブランチ: `rebase`
- 共有ブランチや統合作業: `merge`

### 4.3 cherry-pick

`cherry-pick` は、別ブランチの特定コミットだけを現在のブランチへ取り込む操作。

前提:

- 対象コミットが 1 つの目的にまとまっている
- 対象コミット単体で意味が通る
- 前後のコミットに暗黙依存していない
- フォーマット変更や無関係な修正が混ざっていない

コミット単位が粗い場合や複数目的が混ざっている場合は、`cherry-pick` ではなく元ブランチ側でコミットを整理してから取り込む。
コミット単位の判断基準は `COMMIT_UNIT_GUIDE.md` を参照する。

実行例:

```bash
git switch release/1.2
git cherry-pick <commit-hash>
```

複数コミットを取り込む場合は、取り込む順序と依存関係を確認する。

```bash
git cherry-pick <old-commit-hash> <new-commit-hash>
```

## 5. push と共有

通常の push:

```bash
git push -u origin feature/add-login-api
```

履歴更新後の push:

```bash
git push --force-with-lease
```

運用ルール:

- 初回 push では `-u` を付けて追跡設定を作る
- 他人が触る可能性のあるブランチで強制 push しない
- 強制 push 前に `git log --oneline --decorate --graph -20` で履歴を確認する

## 6. コードレビュー前の確認

PR 作成前の最小確認:

```bash
git status
git diff --cached
git log --oneline --decorate -5
```

確認内容:

- ステージ済み差分に不要な変更がないか
- コミットの分け方が妥当か
- コミットメッセージが Conventional Commits に沿っているか
- ベースブランチとの差分量が過剰でないか

## 7. 禁止または慎重に扱う操作

- `git push --force`
- `git reset --hard`
- `git clean -fd`
- `git rebase -i` での共有済み履歴改変
- 目的を理解しないままの `git checkout .`

これらは便利だが破壊的な操作になりやすい。実行前に対象範囲と復旧方法を確認する。
