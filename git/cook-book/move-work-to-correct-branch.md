# 間違ったブランチで作業していた

まだコミット前なら:

```bash
git stash push -m "move work"
git switch -c feature/correct-branch
git stash pop
```

すでにコミット済みなら:

```bash
git branch feature/correct-branch
git switch feature/correct-branch
```

元ブランチにコミットを残したくない場合は、共有状況を確認した上で `reset` や `revert` を選ぶ。
