# 直前コミットにファイルを追加し忘れた

対処:

```bash
git add path/to/file
git commit --amend
```

push 済みなら:

```bash
git push --force-with-lease
```
