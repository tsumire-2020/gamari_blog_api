git init   
git add .      
 git commit -m "first commit "   
ここまででローカルのリポジトリの対応

Githubで同じ名前のリポジトリを作成した後
 git remote add origin https://github.com/tsumire-2020/gamari_blog_api.git
>> git branch -M main
>> git push -u origin main

これをコピーして実行するとできる

ビルドしたときのみ変わる
変更したら再ビルドをする必要があるdocker-compose build
> interpritor　で使用するPython環境を変更することを忘れないように
FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt←ここに入れたやつを読み込む

COPY . /code/
requirements.txt

venvとかで仮想環境を立ち上げなくてもうまくいく


managed.py が環境の立ち上げやDBの反映やマイグレーションをしてくれるところ

config プロジェクトの設定ファイル（DBとのつなげ方や複数のアプリケーションの受け入れ設定などもここで対応する

認証：jWt　Json形式で認証を渡す
ステートレス

発行される方法（どっちを発行しているか）
セッション認証　ステートフル（バックで保存するため）
JWT認証（最近の主流）

と認証プロセス
メールアドレスなど

メールアドレス認証×トークン方式を採用

djangorestframework-simplejwt==5.2.2が自動的にやってくれる

'djoser' 認証用のURLを用意しているもの
jwtにはログアウト機能はなく、あれはあくまでもWeb側で削除処理をしたときに
抜かれた時にログアウト機能がないのでどうやってログアウトするのかという脆弱性があるといわれているが
サーバーでjwtの生成を切り替える（リスタート）ことで回避可能
jwtにユーザー情報をうまいこと暗号化して組み込むことで管理できるように

 python manage.py migrate


一つのプロジェクト（config)に対して複数のアプリケーションを作る(同じフォルダ階層に作られる)

ディレクトリ操作をする場合blog.app.BlogConfigのように/の代わりにディレクトリを指定する必要がある。

DjangoはUserが必ず一つ定義されていて、authの中にいるUserがデフォルトのユーザとして利用したい

仮想のテーブルと現状のテーブルを比較して、差分があればまいグレーション時に差分を追加する
Djangomigrationｓテーブルの履歴にない対応のみを実行（たまにバグる）