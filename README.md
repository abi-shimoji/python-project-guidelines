# 開発ガイドライン

このリポジトリは、開発時に参照するガイドラインをまとめるためのドキュメント集です。

Python プロジェクトの標準ツール運用と、Git を使った日常開発、履歴管理、コミットルールを管理します。
加えて、会社運用で共通参照できる情報セキュリティの基本マニュアルを管理します。

## ドキュメント構成

### 共通

会社全体で参照する共通ドキュメントです。

- `SECURITY_MANUAL.md`: 全社向けの情報セキュリティ基本マニュアル

### セキュリティ

公開サーバーなど、システムの構築・運用時に参照するセキュリティガイドです。

- `security/README.md`: セキュリティガイド群の概要
- `security/PUBLIC_SERVER_SECURITY_GUIDELINE.md`: 公開サーバーの基本的なセキュリティ方針
- `security/cook-book/`: OS やツールに応じた具体的な作業手順

### Python

Python プロジェクトの開発環境、静的解析、コメント運用に関するガイドです。

- `python/README.md`: Python ガイド群の概要
- `python/PYTHON_GUIDELINES.md`: Python 開発時の標準ツールと運用方針
- `python/RUFF_LINT_GUIDE.md`: `ruff` の lint 運用ガイド
- `python/COMMENT_GUIDE.md`: コメントと docstring の運用ガイド

### Git

Git の基本運用、よく使うコマンド、コミットメッセージ、コミット単位、ユースケース別の対処手順に関するガイドです。

- `git/README.md`: Git ガイド群の概要
- `git/GIT_GUIDELINES.md`: Git 開発時の基本方針と標準ワークフロー
- `git/GITFLOW_GUIDE.md`: Gitflow を採用する場合のブランチ構成と運用手順
- `git/GIT_COMMANDS.md`: 日常的によく使う Git コマンド集
- `git/GITHUB_INTEGRATION_GUIDE.md`: Git と GitHub の連携手順
- `git/COMMIT_MESSAGE_GUIDE.md`: Conventional Commits に基づくコミットメッセージ運用
- `git/COMMIT_UNIT_GUIDE.md`: コミット単位の分け方と `rebase` による整理方法
- `git/cook-book/`: ユースケース別の対処手順
- `git/cook-book/rebase/`: `rebase -i` による履歴整理の手順

## 使い方

新規プロジェクトや既存プロジェクトの運用ルールを揃えるときに、該当するガイドを参照します。

- Python のツール選定や開発フローを確認したい場合は `python/` を参照する
- Git の基本運用、コミット、履歴整理を確認したい場合は `git/` を参照する
- 会社全体のセキュリティ運用ルールを確認したい場合は `SECURITY_MANUAL.md` を参照する
- 公開サーバーの構築・運用時は `security/` を参照する
- 特定の状況への対処手順を探す場合は `git/cook-book/` を参照する
- 細かいコミットの整理や離れたコミットの squash は `git/cook-book/rebase/` を参照する

## 関連テンプレート

`uv`、`ruff`、`ty`、`pytest` を前提にした Python プロジェクトテンプレートは以下にあります。

https://github.com/abi-techinnovation/python-project-template
