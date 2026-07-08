# AGENTS.md

このリポジトリで作業する AI / 自動化エージェントは、以下の前提に従うこと。

作業前に [DEVELOPMENT.md](./DEVELOPMENT.md) を確認し、セットアップ、実行、依存追加、品質確認、コメント・docstring、CI の運用ルールに従う。

## 基本方針

- Python プロジェクトの標準ツールとして `uv`、`ruff`、`ty`、`pytest` を使用する
- パッケージ管理、仮想環境、コマンド実行は `uv` を前提とする
- Lint は `ruff`、型チェックは `ty`、テストは `pytest` を使用する

## コマンド実行ルール

- `python` や `python3` を直接実行しない
- `pip` を直接実行しない
- Python 関連コマンドは原則として `uv` 経由で実行する

例:

```bash
uv run python -m src
uv run pytest
uv run ruff check
uv run ruff format
uv run ty check
uv add requests
uv add --dev pytest
```

## mise の利用

- 環境やツールの呼び出し状況によっては `mise x` を利用してよい
- ただし、Python 実行や依存操作の入口は `python` / `python3` 直接実行ではなく、`uv` を優先する

例:

```bash
mise x -- uv run pytest
mise x -- uv run ruff check
```

## 期待する運用

- 依存追加は `uv add` / `uv add --dev` を使う
- 実行は `uv run` を使う
- 修正後は必要に応じて `uv run ruff format`、`uv run ruff check`、`uv run ty check`、`uv run pytest` を実行する
- 開発手順やドキュメント方針に迷う場合は [DEVELOPMENT.md](./DEVELOPMENT.md) を優先する
