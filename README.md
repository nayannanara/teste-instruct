# Teste Técnico Desenvolvedor(a) Python Júnior [REMOTO]

## PROBLEMA

A companhia de marketing Vough tem trabalhado cada vez mais para empresas de tecnologia que disponibilizam código aberto.

Com o aumento das demandas surgiu a necessidade de rankear seus atuais e potenciais clientes por um nível de prioridade, de modo a dar preferência a projetos de empresas maiores e mais influentes no meio open source.

## SOLUÇÃO

Para auxiliar a Vough, foi desenvolvida uma API que calcula o valor de prioridade de cada cliente e retorna uma lista de clientes ordenandos por prioridade.

Na versão inicial da API, o valor de prioridade é calculado com base em dados encontrados no Github, através da seguinte fórmula:

`prioridade = <quantidade de membros públicos da organização no Github> + <quantidade de repositórios públicos da organização no Github>`

Contém os seguintes endpoints

- Retorna dados de uma organização através da API do Github
:login: login da organização no Github

```
GET /api/orgs/<login>/
```

Apresentar os dados no seguinte formato:

```
{
    "login": "string",
    "name": "string",
    "score": int
}
```

Onde o `score` é o nível de prioridade da organização.

```
GET /api/orgs/
```
- Possui um endpoint para a listagem de todas as organizações já consultadas através da API:

Apresentar os dados no seguinte formato:

```
[
  {
    "login": "string",
    "name": "string",
    "score": int
  },
  {
    "login": "string",
    "name": "string",
    "score": int
  },
  ...
]
```

As organizações listadas aqui estão ordenadas pela prioridade (`score`), da maior para a menor.

- Possui um endpoint para a remoção de organizações da listagem:

```
DELETE /api/orgs/<login>/
```

## EXECUTAR APLICAÇÃO

- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements-dev.txt` 
- `python manage.py migrate`
- `python manage.py runserver`

Acessivel em (http://localhost:8000/) e (https://api-instruct-nay.herokuapp.com/docs/)

## EXECUTAR TESTE ABERTO
Você pode executar esses testes com o [k6](https://k6.io/). Para instalar o k6 basta [baixar o binário](https://github.com/loadimpact/k6/releases) para o seu sistema operacional (Windows, Linux ou Mac).

E para rodar os testes abertos, especifique a variável de ambiente "API_BASE" com o endereço base da API testada.

Exemplo de aplicação rodando no localhost na porta 8000:
`k6 run -e API_BASE='http://localhost:8000/' tests-open.js`
