# Projeto ALFA2-BD

## Subindo o banco de dados localmente

Para subir o banco de dados localmente, é necessário ter o Docker Compose instalado. Assim, basta dar `docker-compose up db-alfa2bd-time2` para subir o banco de dados do time 2. O acesso ao banco é obtido pela porta 5432.

Caso dê algum problema na porta 5432 sendo usada no Linux, basta pegar o ID de quem usa a porta com `sudo netstat -lpn | grep :5432` e rodar `sudo kill -9` nesse ID.
