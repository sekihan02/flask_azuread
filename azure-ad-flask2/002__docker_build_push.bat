@REM ローカルで試す場合、Dockerfileをaci_flask_movetestとしてbuild
@REM docker build -t slack_bot:0.1 .
@REM build後動作するかを確認 Slackの設定で、Slash Commandsを作成して、リクエストをこのアプリケーションのURLに転送するように設定してください。 http://<your_server_ip>:5000/weather
@REM docker run -p 5000:5000 --rm slack_bot:0.1

@REM Dockerイメージのビルドとプッシュを--registryで指定したコンテナレジストリに--imageで指定した名前とタグで登録
az acr build --registry CResistry --image ad_ui_bot:1.2 .

@REM az containerapp create --name my-flask-app --resource-group myResourceGroup --env DOCKER_REGISTRY_SERVER_URL=<azure-container-registry-name>.azurecr.io --env DOCKER_REGISTRY_SERVER_USERNAME=<registry-username> --env DOCKER_REGISTRY_SERVER_PASSWORD=<registry-password> --docker-image-name <azure-container-registry-name>.azurecr.io/ad_ui_bot:1.0 --target-port 5000 --num-replicas 1 --dns-zone "example.com" --fqdn "myapp.example.com"

@REM az containerapp create --name my-flask-app --resource-group myResourceGroup --env DOCKER_REGISTRY_SERVER_URL=cresistry.azurecr.io --env DOCKER_REGISTRY_SERVER_USERNAME=<registry-username> --env DOCKER_REGISTRY_SERVER_PASSWORD=<registry-password> --docker-image-name cresistry.azurecr.io/ad_ui_bot:1.0 --target-port 5000 --num-replicas 1 --dns-zone "example.com" --fqdn "myapp.example.com"

@REM {
@REM     "sku": {
@REM         "name": "Basic",
@REM         "tier": "Basic"
@REM     },
@REM     "type": "Microsoft.ContainerRegistry/registries",
@REM     "id": "/subscriptions/8e561244-40fc-4403-a5ce-c6e315f30b49/resourceGroups/resorce-group/providers/Microsoft.ContainerRegistry/registries/CResistry",
@REM     "name": "CResistry",
@REM     "location": "japaneast",
@REM     "tags": {},
@REM     "properties": {
@REM         "loginServer": "cresistry.azurecr.io",
@REM         "creationDate": "2023-05-13T08:06:36.2136842Z",
@REM         "provisioningState": "Succeeded",
@REM         "adminUserEnabled": true,
@REM         "policies": {
@REM             "quarantinePolicy": {
@REM                 "status": "disabled"
@REM             },
@REM             "trustPolicy": {
@REM                 "type": "Notary",
@REM                 "status": "disabled"
@REM             },
@REM             "retentionPolicy": {
@REM                 "days": 7,
@REM                 "lastUpdatedTime": "2023-05-13T08:06:40.1600798+00:00",
@REM                 "status": "disabled"
@REM             }
@REM         }
@REM     }
@REM }

@REM az containerapp create --name my-flask-app --resource-group myResourceGroup --env DOCKER_REGISTRY_SERVER_URL=<azure-container-registry-name>.azurecr.io --env DOCKER_REGISTRY_SERVER_USERNAME=<registry-username> --env DOCKER_REGISTRY_SERVER_PASSWORD=<registry-password> --docker-image-name <azure-container-registry-name>.azurecr.io/ad_ui_bot:1.0 --target-port 5000 --num-replicas 1 --dns-zone "example.com" --fqdn "myapp.example.com"
az containerapp create --name my-flask-app --resource-group myResourceGroup --env DOCKER_REGISTRY_SERVER_URL=CResistry.azurecr.io --env DOCKER_REGISTRY_SERVER_USERNAME=<registry-username> --env DOCKER_REGISTRY_SERVER_PASSWORD=<registry-password> --docker-image-name <azure-container-registry-name>.azurecr.io/ad_ui_bot:1.0 --target-port 5000 --num-replicas 1 --dns-zone "example.com" --fqdn "myapp.example.com"



@REM 実行するとビルドに必要なファイルをACRに転送してACR上でイメージのビルドが開始されます
@REM 最後のログにRun ID: xxx was successfulと表示されていれば成功です
