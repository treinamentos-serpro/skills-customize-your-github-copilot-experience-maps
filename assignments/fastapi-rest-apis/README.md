# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar livros usando o framework FastAPI. Ao concluir a atividade, você saberá criar endpoints HTTP, validar dados com modelos Pydantic e disponibilizar uma documentação interativa para a API.

## 📝 Tasks

### 🛠️ Criar os endpoints básicos

#### Descrição

Complete a aplicação inicial para criar uma API FastAPI com endpoints de apresentação e verificação de saúde do serviço.

#### Requisitos

O programa concluído deve:

- Criar uma instância de `FastAPI`.
- Implementar `GET /` retornando uma mensagem de boas-vindas.
- Implementar `GET /health` retornando `{"status": "ok"}`.
- Iniciar a aplicação com Uvicorn e permitir testes em `http://127.0.0.1:8000`.

### 🛠️ Implementar o CRUD de livros

#### Descrição

Adicione endpoints para criar, listar, consultar, atualizar e remover livros. Os dados podem ser armazenados em uma lista em memória, sem a necessidade de um banco de dados.

#### Requisitos

O programa concluído deve:

- Definir modelos Pydantic para validar os dados de entrada e saída.
- Implementar `GET /books` para listar todos os livros.
- Implementar `GET /books/{book_id}` para consultar um livro por ID e retornar `404` quando ele não existir.
- Implementar `POST /books` para criar um livro e retornar `201`.
- Implementar `PUT /books/{book_id}` e `DELETE /books/{book_id}`.
- Garantir que cada livro tenha, no mínimo, `id`, `title`, `author` e `year`.

### 🛠️ Validar e documentar a API

#### Descrição

Melhore a API para tratar entradas inválidas e descreva os endpoints para que outro desenvolvedor consiga utilizá-los pela documentação automática do FastAPI.

#### Requisitos

O programa concluído deve:

- Rejeitar títulos ou autores vazios.
- Validar que `year` seja um número inteiro positivo.
- Retornar códigos HTTP coerentes para sucesso, erro de validação e recurso não encontrado.
- Adicionar descrições ou tags aos endpoints principais.
- Disponibilizar a documentação interativa em `/docs`.

Exemplo de corpo para `POST /books`:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "year": 1937
}
```