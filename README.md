# Projeto ALFA2-BD

## Subindo o banco de dados localmente

Para subir o banco de dados localmente, é necessário ter o Docker Compose instalado. Assim, basta executar

```shell
docker-compose up db-alfa2bd-time2
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

## Criando modelo script SQLs

Para criar o modelo usando script SQL basta executar o código python `add_model_db.py`.

```shell
python add_model_db.py
```

Ele executará o script python da pasta `scripts_sql/`.
