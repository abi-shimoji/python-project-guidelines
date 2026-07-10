# 同じ作業で細かく分かれたコミットを 1 つにまとめたい

状況:

- 同じ作業の途中修正が複数コミットに分かれている
- `fix typo` や `adjust test` のような補修コミットを残したくない
- レビュー前に、意味のある 1 コミットへまとめたい

例:

```text
1111111 feat(api): add user search endpoint
2222222 fix(api): fix user search typo
3333333 test(api): adjust user search test
```

前提:

- 対象ブランチがまだ共有されていない、または履歴を書き換える合意がある
- まとめるコミットが同じ目的の作業である
- まとめた後の 1 コミットで意味が通る

手順:

```bash
git status
git log --oneline --decorate --graph -10
git rebase -i HEAD~3
```

エディタで、残したい先頭コミットを `pick` にし、まとめたい後続コミットを `fixup` または `squash` にする。

```text
pick 1111111 feat(api): add user search endpoint
fixup 2222222 fix(api): fix user search typo
fixup 3333333 test(api): adjust user search test
```

使い分け:

- `fixup`: 後続コミットのメッセージを捨ててまとめる
- `squash`: 後続コミットのメッセージも残して編集する

完了後に履歴を確認する:

```bash
git log --oneline --decorate --graph -10
git show HEAD
```

push 済みの履歴を書き換えた場合:

```bash
git push --force-with-lease
```

注意:

- 別目的のコミットまでまとめない
- まとめた後にテストや差分確認を行う
- 作業ログではなく、変更意図として読める履歴にする
