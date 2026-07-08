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


def main() -> None:
    """サンプルアプリケーションを実行する."""
    print(greet("world"))


if __name__ == "__main__":
    main()
