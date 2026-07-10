# 誤って push した変更を取り消したい

共有履歴を保ったまま取り消す場合:

```bash
git revert <commit-hash>
git push
```

理由:

- すでに共有された履歴を壊さない
- 取り消し意図が履歴上に残る
