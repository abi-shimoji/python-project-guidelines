# Development

この文書は、このプロジェクトを開発・保守する人向けの手順をまとめたもの。

- `README.md`: プロジェクトの概要と開始方法
- `DEVELOPMENT.md`: 開発手順、依存追加、品質確認、CI 運用

## Setup

```bash
uv sync
```

## Common Commands

```bash
uv run python -m src
uv run sample-project
uv run ruff format
uv run ruff check
uv run ty check
uv run pytest
```

## Task Execution

`Makefile` を使う場合:

```bash
make help
make format
make lint
make typecheck
make test
make check
make all
```

`mise` task を使う場合:

```bash
mise run help
mise run format
mise run lint
mise run typecheck
mise run test
mise run check
mise run all
```

## Add Dependencies

```bash
uv add requests
uv add --dev pytest
uv add --dev ruff ty
```

## mise

`mise` を利用する場合は、`uv` を `mise x` 経由で実行してよい。

```bash
mise x -- uv sync
mise x -- uv run ruff check
mise x -- uv run ty check
mise x -- uv run pytest
```

## GitHub Actions

GitHub Actions の定義は `.github/workflows/ci.yml` にある。

`push` と `pull_request` を契機に、以下を実行する。

```bash
uv sync
uv run ruff format --check
uv run ruff check
uv run ty check
uv run pytest
```

CI では `uv` をセットアップしたうえで Python 3.12 をインストールしている。

## Development Flow

変更後は最低限、以下を確認する。

```bash
uv run ruff format
uv run ruff check
uv run ty check
uv run pytest
```
