# 離れた位置にあるコミットをまとめたい

状況:

- 同じ作業のコミットが履歴上で離れている
- 例として 1, 2, 4 番目のコミットをまとめたい
- 間に別目的のコミットが挟まっている

例:

```text
1111111 feat(api): add user search endpoint
2222222 fix(api): adjust user search validation
3333333 docs(readme): update setup steps
4444444 test(api): add user search test
```

この例では、`1111111`, `2222222`, `4444444` は同じ作業だが、`3333333` は別目的のドキュメント変更。

前提:

- まとめたいコミット同士が同じ目的である
- 間に挟まったコミットは別目的として残す
- コミット順序を入れ替えても依存関係が壊れない

手順:

```bash
git status
git log --oneline --decorate --graph -10
git rebase -i HEAD~4
```

エディタで、まとめたいコミットを連続するように並べ替える。

変更前:

```text
pick 1111111 feat(api): add user search endpoint
pick 2222222 fix(api): adjust user search validation
pick 3333333 docs(readme): update setup steps
pick 4444444 test(api): add user search test
```

変更後:

```text
pick 1111111 feat(api): add user search endpoint
fixup 2222222 fix(api): adjust user search validation
fixup 4444444 test(api): add user search test
pick 3333333 docs(readme): update setup steps
```

ポイント:

- `fixup` は直前の `pick` にまとめられる
- 離れたコミットをまとめるには、まず対象コミットを隣接させる
- 間にあった別目的のコミットは、まとめた後ろへ移動する

コンフリクトした場合:

```bash
git status
git diff
git add path/to/file
git rebase --continue
```

中止する場合:

```bash
git rebase --abort
```

完了後に確認する:

```bash
git log --oneline --decorate --graph -10
git show HEAD
```

注意:

- コミット順序の入れ替えは、依存関係があるとコンフリクトやビルド失敗の原因になる
- `3333333` が `4444444` の前提になっている場合は、この方法で単純に入れ替えない
- 迷う場合は、先に対象範囲を小さくして `git rebase -i HEAD~N` を実行する
- push 済みの履歴を書き換えた場合は `git push --force-with-lease` を使う
