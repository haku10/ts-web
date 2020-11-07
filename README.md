# TSWeb
Django

# 開発環境構築
docker-compose run django-app django-admin.py startproject [任意のプロジェクト名] .
でDjangoの開発環境を構築

# 前準備
https://console.cloud.google.com/
に自身のアカウントでログインし、Text To Speechの認証を設定しておく。


### 音声変換ページ
http://localhost:[ポート番号]/convertPage/
### 管理者用ページ
http://localhost:[ポート番号]/admin/

### マイグレーション方法
・コンテナに乗り込む
docker exec -it [コンテナID] bash 
・マイグレーションファイル作成 ※Modelクラスの差分を取得
`python manage.py makemigrations convertPage`

``
You are trying to add a non-nullable field 'author' to user without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 
Please enter some code, or 'exit' (with no quotes) to exit.
>>> 1
``

`python manage.py migrate`
テーブルを新規作成すると
アプリ名 + _ + model名で作成される
例) convertPage_userテーブル

# 最初にやること
`python manage.py createsuperuser`
で管理者ユーザーを作成
