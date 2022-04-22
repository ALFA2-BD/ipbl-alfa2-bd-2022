# Projeto ALFA2-BD

## Subindo o banco de dados localmente

Para subir o banco de dados localmente, é necessário ter o Docker Compose instalado. Assim, basta dar `docker-compose up db-alfa2bd-time2` para subir o banco de dados do time 2. O acesso ao banco é obtido pela porta 5432.

Caso dê algum problema na porta 5432 sendo usada no Linux, basta pegar o ID de quem usa a porta com `sudo netstat -lpn | grep :5432` e rodar `sudo kill -9` nesse ID.

## Configurando ambiente python

Antes de usar o ambiente, crie um ambiente virtual. Recomendo o [virtualenv](https://pypi.org/project/virtualenv/).

```shell
pip install virtualenv
```

Para criar o ambiente virtual, execute:

```shell
virtualenv venv
```

Uma vez ativado o ambiente virtual, instale os pacotes:

```shell
pip install -r requirements.txt
```

Sempre que for instalado um novo pacote é nesse arquivo que será colocado as mudanças.

## Criando modelo script SQls

Para criar o modelo usando script SQL basta executar o código python `add_model_db.py`.

```shell
python add_model_db.py
```

Ele executará o script python da pasta `scripts_sql/`.