# 📘 Atividade: Construindo uma aplicação web com FastAPI e Jinja2

## 🎯 Objetivo

Construa uma aplicação web em Python para listar e cadastrar livros usando FastAPI e templates Jinja2. Ao concluir a atividade, você saberá conectar rotas do servidor a uma página HTML e processar dados enviados por formulários.

## 📝 Tarefas

### 🛠️ Renderizar a lista de livros

#### Descrição

Complete a rota principal para carregar os livros armazenados em memória e renderizá-los no template `templates/index.html`.

#### Requisitos

O programa concluído deve:

- Criar uma aplicação FastAPI e configurar `Jinja2Templates` para a pasta `templates`.
- Implementar `GET /` retornando uma resposta HTML.
- Enviar a lista de livros e o objeto `request` para o template.
- Exibir título, autor e ano de cada livro na página.
- Iniciar com Uvicorn em `http://127.0.0.1:8000`.

### 🛠️ Processar o formulário de cadastro

#### Descrição

Adicione um formulário HTML para cadastrar novos livros e implemente a rota que recebe os dados enviados pelo navegador.

#### Requisitos

O programa concluído deve:

- Exibir campos para título, autor e ano de publicação.
- Implementar `POST /books` usando parâmetros de formulário do FastAPI.
- Criar um ID para cada livro novo e armazená-lo na lista em memória.
- Redirecionar para `GET /` depois de um cadastro bem-sucedido.
- Mostrar o livro recém-cadastrado na lista.

### 🛠️ Validar entradas e melhorar a experiência

#### Descrição

Torne o cadastro mais confiável e informe o resultado da operação ao usuário por meio da página HTML.

#### Requisitos

O programa concluído deve:

- Rejeitar títulos e autores vazios ou formados apenas por espaços.
- Validar que o ano seja um número inteiro positivo.
- Exibir uma mensagem de erro na página sem perder os dados digitados quando o formulário for inválido.
- Usar os códigos HTTP adequados para sucesso e erro de validação.
- Organizar o template com uma estrutura HTML válida, labels associados aos campos e uma mensagem visível quando não houver livros.

Para executar a aplicação, instale as dependências com:

```bash
pip install fastapi uvicorn jinja2 python-multipart
```

Depois, execute:

```bash
uvicorn starter-code:app --reload
```
