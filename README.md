# TSWeb
Django

# 開発環境構築
docker-compose run django-app django-admin.py startproject [任意のプロジェクト名] .
でDjangoの開発環境を構築

# 前準備
https://console.cloud.google.com/
に自身のアカウントでログインし、Text To Speechの認証を設定しておく。

## GCPのクレデンシャルファイル名をenvに設定する
ホスト側のマシンの`$HOME/.gcp`にクレデンシャルファイルを配置する

.envファイルにGOOGLE_APPLICATION_CREDENTIALSを記載する

例)
`GOOGLE_APPLICATION_CREDENTIALS /usr/gcp/XXXX.json`

※ ホスト側の`$HOME/.gcp`がコンテナの`/usr/gcp`にマウントされているため、
上記の設定でコンテナ側の環境変数として設定される

### マイグレーション方法
・コンテナに乗り込む
docker exec -it [コンテナID] bash 
・マイグレーションファイル作成 ※Modelクラスの差分を取得
`python manage.py makemigrations convertPage`

`python manage.py migrate`
テーブルを新規作成すると
アプリ名 + _ + model名で作成される
例) convertPage_userテーブル

# 最初にやること
`python manage.py createsuperuser`
で管理者ユーザーを作成

### 音声変換ページ
http://localhost:[ポート番号]/
作成した管理者ユーザーを使用してログインする

### 管理者用ページ
http://localhost:[ポート番号]/admin/
