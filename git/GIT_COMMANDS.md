# Gitコマンド集

この文書は、開発時によく使う Git コマンドを用途別にまとめる。

## 1. 状態確認

作業状態を確認:

```bash
git status
```

未ステージ差分を確認:

```bash
git diff
```

ステージ済み差分を確認:

```bash
git diff --cached
```

変更ファイル一覧だけ見る:

```bash
git diff --name-only
```

## 2. ブランチ操作

ブランチ一覧:

```bash
git branch
git branch -a
```

新規ブランチ作成と切り替え:

```bash
git switch -c feature/add-login-api
```

既存ブランチへ切り替え:

```bash
git switch main
```

追跡ブランチ込みで削除:

```bash
git branch -d feature/add-login-api
git push origin --delete feature/add-login-api
```

## 3. ステージングとコミット

個別ファイルをステージ:

```bash
git add path/to/file
```

差分単位でステージ:

```bash
git add -p
```

直前コミットをメッセージごと修正:

```bash
git commit --amend
```

メッセージを付けてコミット:

```bash
git commit -m "feat(api): add login endpoint"
```

## 4. 取得と同期

リモート情報取得:

```bash
git fetch origin
```

fast-forward のみで更新:

```bash
git pull --ff-only
```

最新の `main` を現在ブランチへ rebase:

```bash
git fetch origin
git rebase origin/main
```

## 5. 履歴確認

簡潔な履歴:

```bash
git log --oneline --decorate -20
```

グラフ付き履歴:

```bash
git log --oneline --decorate --graph --all -20
```

特定ファイルの履歴:

```bash
git log -- path/to/file
```

変更者確認:

```bash
git blame path/to/file
```

## 6. 取り消しと復旧

未ステージ変更を破棄:

```bash
git restore path/to/file
```

ステージだけ外す:

```bash
git restore --staged path/to/file
```

直前コミットを取り消して変更は残す:

```bash
git reset --soft HEAD~1
```

コミットを打ち消す新規コミットを作る:

```bash
git revert <commit-hash>
```

## 7. cherry-pick

> [!WARNING]
> `cherry-pick` は、対象コミットが独立した意味のある単位になっていることを前提に使う。
> 前後のコミットに依存している変更を単体で取り込まず、取り込み後はテストや差分確認を行う。

別ブランチの特定コミットを取り込む:

```bash
git cherry-pick <commit-hash>
```

複数コミットを指定して取り込む:

```bash
git cherry-pick <old-commit-hash> <new-commit-hash>
```

範囲指定で取り込む:

```bash
git cherry-pick <start-commit>^..<end-commit>
```

コンフリクト解消後に続行:

```bash
git cherry-pick --continue
```

中止して元に戻す:

```bash
git cherry-pick --abort
```

## 8. stash

一時退避:

```bash
git stash push -m "wip: login form"
```

一覧確認:

```bash
git stash list
```

退避内容を戻す:

```bash
git stash pop
```

## 9. push

初回 push:

```bash
git push -u origin feature/add-login-api
```

通常 push:

```bash
git push
```

安全な強制 push:

```bash
git push --force-with-lease
```

## 10. よく使う確認コマンド

現在のブランチ名:

```bash
git branch --show-current
```

追跡先確認:

```bash
git branch -vv
```

マージ済みブランチ確認:

```bash
git branch --merged
```

未マージブランチ確認:

```bash
git branch --no-merged
```
