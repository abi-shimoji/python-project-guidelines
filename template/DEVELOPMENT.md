# Development

この文書は、このプロジェクトを開発・保守する人向けの手順をまとめたもの。

- `README.md`: プロジェクトの概要、テンプレートの使い方、最小限の開始方法
- `DEVELOPMENT.md`: セットアップ、実行、依存追加、品質確認、コメントルール、CI 運用

## Setup

`uv` を直接使う場合:

```bash
uv sync
```

`mise` 経由で `uv` を使う場合:

```bash
mise x -- uv sync
```

## Run

`uv` を直接使う場合:

```bash
uv run python -m src
uv run sample-project
```

`mise` 経由で実行する場合:

```bash
mise x -- uv run python -m src
mise x -- uv run sample-project
```

## Quality Checks

`uv` を直接使う場合:

```bash
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

通常の依存関係を追加する場合:

```bash
uv add requests
```

開発用の依存関係を追加する場合:

```bash
uv add --dev pytest
uv add --dev ruff ty
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

## Comments and Docstrings

コメントは最小限にし、コードだけでは意図が伝わりにくい箇所にだけ書く。

- 自明な代入や分岐を説明するコメントは避ける
- 実装理由、制約、注意点など、読み手がコードだけでは判断しにくい内容を書く
- 一時的な補足ではなく、保守時にも意味が残るコメントを書く

docstring は Google スタイルに統一する。

- 公開関数、公開クラス、公開メソッドには原則として docstring を付ける
- docstring では役割、引数、戻り値、必要なら例外を明記する
- `Args` では引数名ごとに期待する値や制約を記載し、型情報は関数シグネチャを前提に補足が必要な場合だけ説明する
- `Returns` では戻り値の意味を記載する
- 例外を送出する可能性がある場合は `Raises` を記載する
- 実装手順の説明ではなく、呼び出し側が知るべき契約を書く

例:

```python
def greet(name: str) -> str:
    """指定された名前に対するあいさつ文を返す.

    Args:
        name: あいさつ対象の名前を表す文字列.

    Returns:
        あいさつ文.

    Raises:
        TypeError: `name` が文字列でない場合.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string.")

    return f"Hello, {name}."
```

## Development Flow

変更後は最低限、以下を確認する。

```bash
uv run ruff format
uv run ruff check
uv run ty check
uv run pytest
```
