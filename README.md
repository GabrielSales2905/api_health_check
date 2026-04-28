## Mission 1: API de Integridade com FastAPI e Docker

Este projeto consiste em uma API desenvolvida em FastAPI para validação de integridade de serviços, integrando um banco de dados PostgreSQL orquestrado via Docker Compose e testes automatizados com Pytest.

## Arquitetura do projeto

Tecnologias Utilizadas:
- Python 3.11+
- FastAPI (Framework web)
- PostgreSQL (Banco de dados relacional)
- Docker & Docker Compose (Containerização)
- Pytest (Testes unitários)

## Como executar o projeto

Para subir o ambiente completo (API + Banco de Dados):

```docker-compose up --build```

Após a inicialização, a API estará disponível em:
- Endpoint Health: http://localhost:8000/health
- Documentação Swagger: http://localhost:8000/docs

## Testes automatizados

O projeto utiliza Pytest para garantir a confiabilidade dos endpoints.

Execução via docker:

```docker-compose exec app pytest```

Execução local:

```pytest```

# Estrtutura de diretórios

.
├── api/
│   └── routes/
│       └── health.py        # Definição da rota de verificação de integridade
├── tests/
│   └── test_health.py     # Testes automatizados para o endpoint /health
├── main.py                # Inicialização do FastAPI e inclusão dos roteadores
├── conftest.py            # Configurações e fixtures globais do Pytest
├── Dockerfile             # Manifesto de construção da imagem da aplicação
├── docker-compose.yml     # Orquestração dos serviços (App + PostgreSQL)
├── requirements.txt       # Listagem de dependências do projeto
├── .gitignore             # Filtro de arquivos e diretórios ignorados pelo Git
└── readme.md              # Documentação técnica do projeto

# Autor - Gabriel Sales
# Data Elaboração - 28/04/2026