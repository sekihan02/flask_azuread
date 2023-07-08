@REM Dockerイメージのビルドとプッシュを--registryで指定したコンテナレジストリに--imageで指定した名前とタグで登録
az acr build --registry CResistry --image flask_bot:latest .
@REM 実行するとビルドに必要なファイルをACRに転送してACR上でイメージのビルドが開始されます
@REM 最後のログにRun ID: xxx was successfulと表示されていれば成功です