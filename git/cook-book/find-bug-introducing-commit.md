# どのコミットが不具合を入れたか調べたい

履歴確認:

```bash
git log --oneline --decorate --graph -20
git show <commit-hash>
```

段階的に切り分ける場合:

```bash
git bisect start
git bisect bad
git bisect good <known-good-commit>
```

補足:

- `bisect` は再現手順が明確な不具合で有効
- 調査後は `git bisect reset` で元に戻す
