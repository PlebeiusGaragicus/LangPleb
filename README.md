# LangChain / General AI study
 - [Read papers](https://python.langchain.com/v0.2/docs/additional_resources/arxiv_references/)
 - [Keep studying LangChain](https://python.langchain.com/v0.2/docs/versions/v0_2/)
 - [Keep practicing LangGraph implementations](https://langchain-ai.github.io/langgraph/)
 - [Read LangChain how-to guides](https://python.langchain.com/v0.2/docs/how_to/)

# Self-host constructs
 - [Read docs for LangServe](https://python.langchain.com/v0.1/docs/langserve/)
 - [Self host LangServe?](https://langfuse.com/docs/deployment/self-host)

# Open WebUI pipelines
 - [Reverse engineer pipelines](https://github.com/open-webui/pipelines/tree/main#-quick-start-with-docker)
 - [Consider how I can host Open WebUI pipelines SAFELY](https://github.com/open-webui/pipelines/blob/main/config.py)
 - [How does event emitter work???](https://github.com/open-webui/open-webui/pull/3615)

# LangFuse - monitoring
 - [self host LangFuse for monitoring](https://langfuse.com/docs/deployment/self-host)
 - [LangFuse guide](https://langfuse.com/docs/integrations/langchain/tracing)

# ...
 - https://github.com/open-webui/pipelines/blob/main/examples/pipelines/integrations/applescript_pipeline.py


---


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