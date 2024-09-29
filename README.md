# swapi-api
Integração da [SWAPI](https://swapi.dev/documentation#root) com Banco de Dados utilizando Python

# Instalação

Recomendado o uso do CMD ou PowerShell, pois esses indicam o ambiente virtual do python ativo.

- Clone o repositório
    ```cmd
     git clone https://github.com/Sylvio-Cezar/swapi-api.git
    ```

- Navegue até o diretório
    ```cmd
    cd swapi-api
    ```

- Crie o ambiente virtual
    ```cmd
    python -m venv .venv
    ```

- Ative o ambiente
    ```cmd
    .venv/Scripts/activate
    ```

- Instale as dependências
    ```cmd
    pip install -r requirements.txt
    ```

# Execução

- Rode o arquivo `main.py`
    ```cmd
    python main.py
    ```

O uvicorn iniciará o servidor e os logs serão exibidos no console, se bem sucedido a mensagem será semelhante a:
```
INFO:     Started server process [6288]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Acessando a rota `/docs` será mostrado todas as rotas configuradas para a aplicação.

# Tecnologias

- Python

    Dependências
    - [FastAPI](https://fastapi.tiangolo.com/) -> Framework para construção de API's.
        
        Utilizado na construção das rotas.

    - [Requests](https://requests.readthedocs.io/en/latest/) -> Biblioteca para uso do protocolo HTTP.

        Utilizado no consumo da [SWAPI](https://swapi.dev/documentation#root)

    - [Uviconr](https://www.uvicorn.org/) -> Implementação de servidor web ASGI.

        Utilizado para criar e executar o servidor da aplicação.

    - [Sqlitemodel](https://pypi.org/project/sqlitemodel/) -> Wrapper para o banco de dados sqlite3.

        Utilizado na construção das classes do diretório `models` e permitindo a persistência dos dados no arquivo `swapi_database.db` (definido em `main.py`)
    