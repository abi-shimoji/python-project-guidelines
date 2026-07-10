# コメント・docstringガイド

この文書は、Python コードにおけるコメントと docstring の運用ルールをまとめる。

## 1. 基本方針

コメントは最小限にし、コードだけでは意図が伝わりにくい箇所にだけ書く。

- 自明な代入や分岐を説明するコメントは避ける
- 実装理由、制約、注意点など、読み手がコードだけでは判断しにくい内容を書く
- 一時的な補足ではなく、保守時にも意味が残るコメントを書く
- コメントでコードの挙動を説明しすぎず、まずコード自体を読みやすくする

## 2. docstring

docstring は Google スタイルに統一する。

- 公開関数、公開クラス、公開メソッドには原則として docstring を付ける
- docstring では役割、引数、戻り値、必要なら例外を明記する
- 実装手順の説明ではなく、呼び出し側が知るべき契約を書く
- 日本語で記載し、文末は `.` に統一する

## 3. 例外の記載

例外を送出する可能性がある場合は `Raises` を記載する。

- 送出する例外型を書く
- どの条件で例外が発生するかを書く
- 内部実装の都合ではなく、呼び出し側が扱うべき例外を中心に書く

## 4. 例

```python
def greet(name: str) -> str:
    """指定された名前に対するあいさつ文を返す.

    Args:
        name: あいさつ対象の名前.

    Returns:
        あいさつ文.

    Raises:
        TypeError: `name` が文字列でない場合.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string.")

    return f"Hello, {name}."
```

## 5. 避ける例

```python
# nameをチェックする
if not isinstance(name, str):
    raise TypeError("name must be a string.")
```

上記のようにコードを読めば分かる内容はコメントしない。必要な場合は、なぜそのチェックが必要なのかを書く。
