# 別作業を急ぎで挟みたい

変更を一時退避:

```bash
git stash push -m "wip: current task"
git switch main
git switch -c fix/hotfix-issue
```

元作業へ戻る:

```bash
git switch previous-branch
git stash pop
```
