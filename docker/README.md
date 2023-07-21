### Constuir imagem docker
`docker build -t aln/app-python:1.0 .`
<p>Para instalar o Docker, siga a [Documentação](https://www.docker.com)</p>

### Configurar o .env
```
HOST_DB = <IP do banco de dados>
PORT_DB = <porta>
USER_DB = <usuário>
PASSWORD_DB = <senha>
NAME_DB = <nome do banco de dados>
```

### Executar o container docker
`docker run -d -p 80:80 aln/app-python:1.0`

### Utilizando o projeto de forma local (sem docker)
- Instalando dependências
`pip install -r requirements.txt`

- Iniciando servidor
`uvicorn app.main:app --reload`
