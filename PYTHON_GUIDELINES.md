# Pythonガイドライン

このガイドラインでは、Pythonプロジェクトの標準ツールとして `uv`、`ruff`、`ty` を使用する。

- `uv`: Python本体、仮想環境、依存関係、実行を管理する
- `ruff`: LintとFormatを担当する
- `ty`: 型チェックを担当する

ツールを分けて役割を明確にしつつ、日常運用では `uv run` 経由で統一して実行する。

## 1. 基本方針

- パッケージ管理と実行環境は `uv` に統一する
- コード整形は `ruff format` に統一する
- 静的解析は `ruff check` に統一する
- 型検査は `ty check` に統一する
- 個別インストールより、プロジェクトの開発依存として管理する
- コマンドの実行は、グローバル環境ではなくプロジェクト環境で行う

## 2. ツール概要

### 2.1 uv

`uv` は Astral 製の Python パッケージ・プロジェクトマネージャーで、依存関係管理、仮想環境、Python バージョン管理、ツール実行をまとめて扱える。

従来の `pip`、`venv`、`pip-tools`、`pipx`、`poetry` の役割を広くカバーできるため、Python 開発の入口を `uv` に一本化しやすい。

主な用途:

- プロジェクト作成
- 仮想環境作成
- 依存関係追加・更新
- 開発ツールの実行
- Python バージョンの固定

### 2.2 ruff

`ruff` は Astral 製の高速な Linter / Formatter で、Flake8 系のチェック、import 整理、フォーマットを一つのツールで扱える。

主な用途:

- 未使用 import などの静的チェック
- 自動修正
- コードフォーマット
- ルールの段階的導入

### 2.3 ty

`ty` は Astral 製の高速な型チェッカー兼 Language Server。型エラー検出を主目的に使う。

主な用途:

- 型整合性の確認
- 型エラーの早期検出
- 変更監視による再チェック
- エディタ連携

## 3. 導入手順

### 3.1 uvのインストール

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

インストール確認:

```bash
uv
```

### 3.2 プロジェクト作成

新規プロジェクト作成:

```bash
uv init my-project
cd my-project
```

ライブラリプロジェクトとして作る場合:

```bash
uv init --lib my-library
cd my-library
```

使用する Python バージョンを指定して作る場合:

```bash
uv init --python 3.12 my-project
cd my-project
```

ライブラリプロジェクトを Python バージョン指定で作る場合:

```bash
uv init --lib --python 3.12 my-library
cd my-library
```

### 3.3 開発ツール追加

`ruff` と `ty` は開発依存として追加する。

```bash
uv add --dev ruff ty
```

## 4. 日常運用コマンド

### 4.1 依存関係管理

依存関係追加:

```bash
uv add requests
```

開発依存追加:

```bash
uv add --dev pytest
```

ロックファイル更新:

```bash
uv lock
```

環境同期:

```bash
uv sync
```

### 4.2 コマンド実行

プロジェクト環境で Python を実行:

```bash
uv run python
```

スクリプト実行:

```bash
uv run python main.py
```

### 4.3 Ruff

Lint 実行:

```bash
uv run ruff check
```

特定ディレクトリだけチェック:

```bash
uv run ruff check src tests
```

自動修正付き Lint:

```bash
uv run ruff check --fix
```

Format 実行:

```bash
uv run ruff format
```

差分確認用途の Format:

```bash
uv run ruff format --check
```

### 4.4 ty

型チェック実行:

```bash
uv run ty check
```

特定パスだけ型チェック:

```bash
uv run ty check src tests
```

変更監視:

```bash
uv run ty check --watch
```

自動修正が可能なものを修正:

```bash
uv run ty check --fix
```

## 5. 推奨設定

設定は原則として `pyproject.toml` に集約する。

例:

```toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.12"

[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "UP"]

[tool.ty]
```

補足:

- `requires-python` はサポート対象の下限を明示する
- `ruff` の `target-version` は実行対象 Python に合わせる
- `ruff` のルールは最初は狭く始め、必要に応じて拡張する
- `ty` の詳細設定が必要な場合も、まずは `pyproject.toml` ベースで管理する

## 6. 推奨ワークフロー

日常開発では次の順で確認する。

1. 実装する
2. `uv run ruff format`
3. `uv run ruff check --fix`
4. `uv run ty check`
5. 必要に応じて `uv run pytest`

コミット前の最小確認:

```bash
uv run ruff format --check
uv run ruff check
uv run ty check
```

## 7. 運用ルール

- `python` や `pip` を直接叩く運用は避け、原則 `uv run` と `uv add` を使う
- Lint エラーを安易に ignore せず、まず修正可能か確認する
- `ruff check --fix` で直せるものは自動修正を使う
- 型アノテーションは公開 API と複雑なロジックを優先して付与する
- `ty` の警告抑制は最小限にする
- ツール設定は個人ローカルではなく `pyproject.toml` に集約する

## 8. 最低限覚えるコマンド一覧

```bash
uv init my-project
uv add requests
uv add --dev ruff ty pytest
uv sync
uv run python main.py
uv run ruff format
uv run ruff check --fix
uv run ty check
```

## 9. 参考

- uv 公式ドキュメント: https://docs.astral.sh/uv/
- ty 公式ドキュメント: https://docs.astral.sh/ty/
- Ruff 公式ドキュメント: https://docs.astral.sh/ruff/

確認日: 2026-07-07
