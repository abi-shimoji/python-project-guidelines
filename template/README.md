# sample-project

`uv`、`ruff`、`ty`、`pytest` を使用する Python プロジェクト。

## 概要

このリポジトリは、Python プロジェクトを開始するための最小構成を提供する。

## 前提

このプロジェクトでは `uv` もしくは `mise` を使用する。

## uv のインストール

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## mise のインストール

```bash
curl https://mise.run | sh
```

## 開始方法

`uv` を直接使う場合:

```bash
uv sync
uv run python -m src
uv run sample-project
```

`mise` 経由で `uv` を使う場合:

```bash
mise x -- uv sync
mise x -- uv run python -m src
mise x -- uv run sample-project
```

## 構成

- `src`: アプリケーションコード
- `tests`: テストコード
- `.github/workflows/ci.yml`: CI 定義

## 開発

開発手順、依存追加、品質確認、CI の詳細は [DEVELOPMENT.md](./DEVELOPMENT.md) を参照する。
