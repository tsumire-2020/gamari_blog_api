# 概要

Djangoの環境を構築するためのリポジトリです。

## コマンド

## Djangoのコマンド

 python manage.py startapp [app_name]

## Git command

 git add .
 git commit -m "commit message"
 git push

###　DB

python manage.py makemigrations
- DBとmodels.pyを確認し、差分があればマイグレーションファイルを作成する


python manage.py migrate

- マイグレーションファイルをDBに反映する初回はこっちのみ

### 開発サーバーの実行

python manage.py runserver

python manage.py runserver 0.0.0.0:8000
実行後
http://localhost:8000/
にアクセスする

###　管理者ユーザーの作成
python manage.py createsuperuser