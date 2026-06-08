# API de Controle de Rações para Pets

## Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de Laboratório de Programação Back-End.

A aplicação consiste em uma API para gerenciamento de rações para pets, permitindo realizar operações de cadastro, consulta, atualização e exclusão de registros.

O objetivo do projeto é aplicar conceitos de desenvolvimento de APIs, integração com banco de dados e conteinerização utilizando Docker.

---

## Funcionalidades

A API permite:

* Cadastrar uma nova ração
* Listar todas as rações cadastradas
* Consultar uma ração específica
* Atualizar informações de uma ração
* Excluir uma ração

---

## Estrutura do Projeto

```text
api-racao/
│
├── backend/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## Rotas da API

### Listar todas as rações

```http
GET /racoes
```

### Buscar uma ração por ID

```http
GET /racoes/{id}
```

### Cadastrar uma nova ração

```http
POST /racoes/{id}
```

Exemplo:

```json
{
  "nome": "Ração Premium",
  "marca": "Golden",
  "preco": 120
}
```

### Atualizar uma ração

```http
PUT /racoes/{id}
```

### Excluir uma ração

```http
DELETE /racoes/{id}
```

---

## Como Executar

### Pré-requisitos

* Docker Desktop instalado

### Executando o projeto

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/api-racao.git
```

Entre na pasta:

```bash
cd api-racao
```

Execute os containers:

```bash
docker compose up --build
```

A API ficará disponível em:

```text
http://localhost:8000
```

Documentação Swagger:

```text
http://localhost:8000/docs
```

---

## Testes Realizados

Foram realizados testes das operações CRUD utilizando a interface Swagger disponibilizada pelo FastAPI.

Operações testadas:

* Cadastro (POST)
* Consulta (GET)
* Atualização (PUT)
* Exclusão (DELETE)


