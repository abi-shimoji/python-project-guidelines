# コンフリクトが起きた

状況:

- `pull` や `rebase` の途中で競合した
- 同じ行や近い領域を別ブランチが更新していた

対処:

```bash
git status
git diff
```

競合ファイルを修正した後:

```bash
git add path/to/file
git rebase --continue
```

merge 中なら:

```bash
git add path/to/file
git commit
```

補足:

- どちらを残すかではなく、最終的にあるべき状態を手で作る
- 判断に迷う差分は元のコミットを `git log` や `git show` で確認する
