# コミットメッセージガイド

この文書は、Conventional Commits を前提にしたコミットメッセージの運用ルールをまとめる。

## 1. 基本形式

基本形式は次の通り。

```text
<type>(<scope>): <description>
```

`scope` は任意だが、変更対象が明確になる場合は付ける。

例:

```text
feat(auth): add refresh token validation
fix(api): handle empty query parameter
docs(git): add conventional commits guide
```

## 2. type 一覧

日常運用では次の `type` を使う。

- `feat`: ユーザー向け機能追加
- `fix`: バグ修正
- `docs`: ドキュメント変更
- `refactor`: 挙動を変えない構造改善
- `test`: テスト追加・修正
- `chore`: 雑多なメンテナンス、設定変更、依存更新
- `build`: ビルド設定や依存解決に関わる変更
- `ci`: CI/CD 設定変更
- `perf`: 性能改善
- `revert`: 変更の取り消し

## 3. description のルール

- 英語または日本語で簡潔に書く
- 句点は付けない
- 何をしたかが分かる表現にする
- あいまいな表現を避ける

### 3.1 英語の場合

- 先頭は小文字にする
- 動詞から始める
- 過去形ではなく命令形または現在形で書く

良い例:

- `fix(user): prevent duplicate email registration`
- `docs(readme): update local setup steps`
- `refactor(service): split payment validation logic`

### 3.2 日本語の場合

- 体言止めで簡潔に書く
- `です`、`ます`、`する` で終えない
- 主語を省き、変更内容から始める

良い例:

- `fix(user): メールアドレスの重複登録防止`
- `docs(readme): ローカルセットアップ手順の更新`
- `refactor(service): 支払い検証ロジックの分離`

### 3.3 避ける例

- `fix: bug fix`
- `feat: Update feature`
- `docs: updated`
- `fix: 修正`
- `fix(user): メールアドレスの重複登録を防ぐ`
- `docs: ドキュメントをいい感じに更新`

## 4. scope の運用

`scope` は対象領域を短く表す。

例:

- `auth`
- `api`
- `ui`
- `db`
- `git`
- `readme`

ルール:

- ディレクトリ名、モジュール名、機能名など一貫した単位で付ける
- 毎回無理に付ける必要はない
- 長すぎる識別子は避ける

## 5. Breaking Change

後方互換性を壊す変更は `!` または本文で明示する。

例:

```text
feat(api)!: remove legacy login response
```

または:

```text
feat(api): change login response format

BREAKING CHANGE: response field `token` was renamed to `access_token`
```

## 6. 本文とフッター

件名だけで意図が十分に伝わらない場合は本文を付ける。

本文で書く内容:

- 変更理由
- 制約や移行上の注意
- 代替案を採らなかった理由

例:

```text
fix(auth): reject expired refresh tokens

The previous validation only checked signature and issuer.
This change also validates expiration to prevent reuse of stale tokens.
```

Issue 連携がある場合の例:

```text
feat(ui): add loading state to dashboard

Refs: #123
```

## 7. 粒度のルール

- 1 コミット 1 目的を守る
- フォーマット変更と機能変更を混ぜない
- 大きな変更はレビューしやすい単位に分割する
- 一時退避の `wip` コミットは共有前に整理する

詳細なコミット単位の判断基準と、`rebase -i` による整理手順は `COMMIT_UNIT_GUIDE.md` を参照する。

## 8. 推奨例

```text
feat(api): add user search endpoint
fix(worker): retry on temporary network error
docs(git): add cookbook for conflict resolution
test(service): cover invalid token case
chore(deps): update pytest to 8.4.0
ci(actions): cache uv dependencies
```
