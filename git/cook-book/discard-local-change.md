# ローカル変更を捨てたい

特定ファイルだけ破棄:

```bash
git restore path/to/file
```

注意:

- 復旧できない変更があるか確認してから実行する
- 迷う場合は先に `git stash` で退避する
