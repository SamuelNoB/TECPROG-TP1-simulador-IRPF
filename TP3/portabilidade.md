# Portabilidade

## Conceito

A portabilidade de um projeto está relacionada com a capacidade do mesmo ser executado em diversos sistemas operacionais de maneira com que seu funcionamento não seja afetado pelas peculiaridades de cada sistema.

Para alcançar isso o projeto deve utilizar recursos que possibilitem que as dependências externas possam ser instaladas em qualquer SO e também deve evitar trechos de códigos que utilizem recursos exclusivos de um sistema operacional de desenvolvimento.

## Implementação

Para trazer essa característica para nosso projeto foi utilizado um arquivo chamado `requirements-dev.txt` para listar as dependências externas do projeto e suas determinadas versões de maneira que utilizando o comando `pip install -r docker/requirements-dev.txt` um usuário de qualquer sistema operacional que possua o python possa executar nosso projeto da maneira correta.

Para tratar os problemas de compatibilidade entre as versões do **python** nosso grupo decidiu criar um [docker](https://www.docker.com/) para padronizar a versão do python que será usada na aplicação, desse modo todas as dependências estarão empacotadas no nosso container e possibilitará a todos os sistemas operacionais que tenham o docker executar nosso projeto.

### Arquivos

* `docker/Dockerfile`
* `docker/requirements-dev.txt`
* `docker-compose.yml`
