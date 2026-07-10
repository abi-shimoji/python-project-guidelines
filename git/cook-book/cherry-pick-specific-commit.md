# 別ブランチの特定コミットだけ取り込みたい

状況:

- 修正済みの 1 コミットだけをリリースブランチへ反映したい
- hotfix 用ブランチへ、既存ブランチの一部変更だけを持っていきたい

前提:

- 対象コミットが 1 つの目的にまとまっている
- 対象コミット単体でビルドやテストが通る見込みがある
- 前後のコミットに暗黙依存していない
- 関係ない整形、リファクタリング、設定変更が混ざっていない

対処:

```bash
git switch release/1.2
git fetch origin
git cherry-pick <commit-hash>
```

コンフリクトした場合:

```bash
git status
git diff
git add path/to/file
git cherry-pick --continue
```

取り込みを中止する場合:

```bash
git cherry-pick --abort
```

注意:

- コミット単位がきちんとしていない変更は `cherry-pick` に向かない
- 複数コミットが必要な場合は、古い順に取り込む
- 取り込み後は `git show HEAD` で差分を確認する
- リリースブランチへ反映する場合は、対象範囲が本当に必要最小限か確認する
