# コミット単位を整理したい

状況:

- 途中作業の細かいコミットが残っている
- 1 つのコミットに複数の目的が混ざっている
- コミットメッセージだけを直したい
- `cherry-pick` やレビューに向けて、コミット単位を整えたい

前提:

- 作業ブランチがまだ共有されていない、または履歴を書き換える合意が取れている
- 整理前の状態を `git log` と `git status` で確認している
- 整理対象のベースブランチが明確になっている

確認:

```bash
git status
git log --oneline --decorate --graph -20
```

ベースブランチからのコミットを整理する:

```bash
git fetch origin
git rebase -i origin/main
```

直近の数コミットだけ整理する:

```bash
git rebase -i HEAD~3
```

細かすぎるコミットをまとめる場合:

```text
pick 1111111 feat(api): add user search endpoint
fixup 2222222 fix typo
fixup 3333333 adjust test
```

大きすぎるコミットを分ける場合:

```text
edit 1111111 feat(api): add user search endpoint
```

`edit` で止まった後:

```bash
git reset HEAD^
git add -p
git commit -m "feat(api): add user search endpoint"
git add -p
git commit -m "test(api): cover user search endpoint"
git rebase --continue
```

メッセージだけ修正する場合:

```text
reword 1111111 feat(api): add user search endpoint
```

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

注意:

- 共有済みブランチでは安易に `rebase -i` しない
- フォーマット変更と挙動変更は別コミットに分ける
- 整理後は `git log --oneline --decorate --graph -20` で履歴を確認する
- push 済みの履歴を書き換えた場合は、必要性を確認して `git push --force-with-lease` を使う
