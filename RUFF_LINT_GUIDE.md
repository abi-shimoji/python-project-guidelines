# Ruff Lint設定ガイド

この文書は、`ruff` のうち lint 設定に絞って説明する。

- 対象: `ruff check`
- 非対象: `ruff format`

`ruff` は多数のルールを持つため、最初から広く有効化しすぎると既存コードベースでは運用負荷が上がる。最初は基本ルールから始め、必要に応じて段階的に拡張する。

## 1. 基本方針

- 設定は `pyproject.toml` に集約する
- まずはデフォルトに近い狭いルールセットから始める
- 自動修正できるものは `ruff check --fix` を活用する
- `ignore` を増やしすぎず、理由のあるものだけ抑制する
- プロジェクト全体の設定と、例外的なファイル単位設定を分けて管理する

## 2. 基本設定

最小構成の例:

```toml
[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F"]
```

意味:

- `line-length`: 1行の長さの基準
- `target-version`: 対象 Python バージョン
- `select`: 有効化するルール群

`E` と `F` は、まず導入しやすい基本ルール。

- `E`: pycodestyle 系の一部エラー
- `F`: Pyflakes 系の問題検出

## 3. よく使うルール群

実務で追加しやすい代表例:

```toml
[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]
```

各ルール群の概要:

- `E`: 基本的なコードスタイル上の問題
- `F`: 未使用 import、未定義名などの不具合候補
- `I`: import 順序と import 整理
- `UP`: 新しい Python 構文への更新候補
- `B`: バグになりやすい書き方の検出

推奨の考え方:

- 新規プロジェクト: `E`, `F`, `I`, `UP`
- 品質を少し強めたい場合: `B` を追加
- ドキュメント規約や命名規約は、必要性が明確になってから追加

## 4. 設定例

### 4.1 標準的な設定

```toml
[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]
```

この設定は、基本的な不具合検出と import 整理、Python の更新提案までをカバーする。

### 4.2 段階的導入向け設定

```toml
[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F"]
ignore = ["E501"]
```

この設定は、既存コードベースへ導入しやすい。長い行の扱いは formatter や後続整理に任せやすい。

### 4.3 import 整理を重視する設定

```toml
[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I"]
```

`I` を有効にすると、import 並び順やグループ整理を一貫させやすい。

## 5. `select` と `ignore`

`select` は有効化するルール、`ignore` は無効化するルール。

例:

```toml
[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]
ignore = ["B008"]
```

考え方:

- `select` で基準を定義する
- `ignore` は例外として最小限に使う

`ignore` を増やしすぎると、何を守りたい設定なのかが曖昧になる。

## 6. `extend-select` と `extend-ignore`

既存設定に追加したい場合は `extend-select`、追加で除外したい場合は `extend-ignore` を使う。

例:

```toml
[tool.ruff.lint]
select = ["E", "F"]
extend-select = ["I", "UP"]
extend-ignore = ["E501"]
```

用途:

- ベースルールは維持したまま少しずつ厳しくする
- 共通テンプレートに追加差分だけ書く

## 7. ファイル単位の例外設定

特定ファイルだけルールを緩めたい場合は `per-file-ignores` を使う。

例:

```toml
[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["S101"]
"__init__.py" = ["F401"]
```

用途:

- `__init__.py` で再公開 import を許可する
- テストコードだけ一部ルールを緩和する

注意:

- 例外はファイル種別ごとに理由が説明できるものに限る
- 広すぎるパターン指定は避ける

## 8. 自動修正

`ruff` は多くの指摘を自動修正できる。

実行例:

```bash
uv run ruff check --fix
```

確認だけ行う場合:

```bash
uv run ruff check
```

自動修正の対象は便利だが、すべての問題が直るわけではない。意味変更の可能性がある指摘は手動確認する。

## 9. 抑制コメント

行単位で抑制する場合:

```python
from typing import Iterable  # noqa: UP035
```

ファイル単位で抑制する場合:

```python
# ruff: noqa: F401
```

運用方針:

- まず設定で解決できるか確認する
- 次にコード修正で対応できるか確認する
- それでも必要な場合だけ `noqa` を使う

## 10. 推奨コマンド

日常利用:

```bash
uv run ruff check
uv run ruff check --fix
```

対象を限定する場合:

```bash
uv run ruff check src
uv run ruff check src tests
```

CI 向け:

```bash
uv run ruff check
```

## 11. 推奨運用パターン

### 新規プロジェクト

```toml
[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "UP"]
```

### 既存プロジェクトへの導入初期

```toml
[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F"]
ignore = ["E501"]
```

### 品質をやや強める場合

```toml
[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]
```

## 12. 避けるべき運用

- ルールを大量に一括導入して放置する
- `ignore` を増やし続ける
- `noqa` を理由なく付ける
- チーム共通設定を個人判断で頻繁に変える
- formatter が担当する範囲と lint の範囲を混同する

## 13. 参考

- Ruff 公式ドキュメント: https://docs.astral.sh/ruff/
- Ruff Tutorial: https://docs.astral.sh/ruff/tutorial/
- Ruff Rules: https://docs.astral.sh/ruff/rules/

確認日: 2026-07-07
