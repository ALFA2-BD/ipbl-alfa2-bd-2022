# Projeto ALFA2-BD

## Explicação da Estrutura

Na pasta `dataset/` está o modelos, scripts SQL para criar as tabelas. O arquivo `ScriptsSQL.py` é uma classe python responsável por executar scripts SQL diretamente no banco.

Para executar esse script, pode-se usar o arquivo `setup.py`.

Na pasta `front_alfa2bd/` é o local no qual será desenvolvido o front-end.

Dentro dessa pasta tem o arquivo `mock_dataset.py`, que é responsável por popular o banco de dados de forma genérica.

## Subindo o banco de dados localmente

Para subir o banco de dados localmente, é necessário ter o Docker Compose instalado. Assim, basta executar

```shell
docker-compose up db-alfa2bd
```

para subir o banco de dados do time 2. O acesso ao banco está configurado na porta padrão 5432.

Caso dê problema na porta 5432 já sendo usada no Linux, basta pegar o ID de quem usa a porta com

```shell
sudo netstat -lpn | grep :5432
```

e rodar o seguinte comando no ID:

```shell
sudo kill -9
```

## Configurando ambiente python

Antes de usar o ambiente, crie um ambiente virtual. Recomendo o [virtualenv](https://pypi.org/project/virtualenv/).

```shell
pip install virtualenv
```

Para criar o ambiente virtual, execute:

```shell
virtualenv venv
```

Para ativar o ambiente virtual, use:

```shell
source venv/bin/activate
```

Uma vez ativado o ambiente virtual, instale os pacotes:

```shell
pip install -r requirements.txt
```

Sempre que for instalado um novo pacote é nesse arquivo que será colocado as mudanças.

## Criando Modelo Script SQLs

Para criar o modelo usando script SQL basta executar o código python `setup.py`.

```shell
python setup.py
```

Ele executará os scripts SQL usando python.

## Usando o Django

Para usar o Django há alguns comandos principais que podem ajudar no desenvolvimento.

O comando `django-admin startproject [anithing_project]` criar um novo projeto Django.

O comando `python manage.py runserver` executa o servidor Django.


O comando `python manage.py migrate` ajusta as tabelas do Django ao banco de dados.

## Usando o Django Admin

Para visualzar o banco e ter controle sobre os dados o Django disponibiliza uma tela de admin para ter como auxílio. Ela está no link [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

Antes de acessar ela é importante criar um usuário admin. Para fazer isso, basta executar o comando `python manage.py createsuperuser`.

Depois disso, basta entrar no link e visualizar a tela de admin.
