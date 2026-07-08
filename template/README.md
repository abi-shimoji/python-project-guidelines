# sample-project

`uv`、`ruff`、`ty`、`pytest` を使用する Python プロジェクトテンプレートです。

## 概要

このリポジトリは、Python プロジェクトをすぐに開始するための最小構成を提供します。

含まれるもの:

- `uv` による Python・依存関係・実行環境の管理
- `ruff` による lint と format
- `ty` による型チェック
- `pytest` によるテスト
- `Makefile` と `mise` task による共通コマンド
- GitHub Actions による CI

## このテンプレートの使い方

GitHub の `Use this template` から新しいリポジトリを作成します。

作成後、最低限以下をプロジェクトに合わせて変更します。

- `README.md` のプロジェクト名と説明
- `pyproject.toml` の `project.name`
- `pyproject.toml` の `project.description`
- `pyproject.toml` の `project.scripts`
- 必要に応じて `src/` 配下のパッケージ構成

## 前提

このプロジェクトでは `uv` を使用します。

`mise` は任意です。利用する場合は `uv` の実行や開発タスクを `mise` 経由にできます。

## クイックスタート

```bash
uv sync
uv run python -m src
uv run pytest
```

セットアップ、実行、依存追加、品質確認、CI の詳細は [DEVELOPMENT.md](./DEVELOPMENT.md) を参照してください。

## 構成

- `src/`: アプリケーションコード
- `tests/`: テストコード
- `DEVELOPMENT.md`: 開発手順、コメントルール、品質確認、CI 運用
- `pyproject.toml`: プロジェクト設定、依存関係、各種ツール設定
- `Makefile`: 開発タスク
- `mise.toml`: `mise` 用タスク定義
- `.github/workflows/ci.yml`: CI 定義
