# PlebServe


```sh
pip install -U langchain-cli
```




view a demo

```sh
langchain-cli app new langserve-demo --package pirate-speak
```




```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```