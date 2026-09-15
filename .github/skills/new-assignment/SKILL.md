---
name: new-assignment
description: "Use when creating, adding, structuring, or generating a programming assignment, exercise, or homework for students."
---

# Criar Nova Tarefa de Programação

Use esta skill para criar uma assignment completa no portal educacional. As assignments ficam em `assignments/<id>/`, e o site lê `config.json` para exibi-las.

## Fluxo

### 1. Definir o conteúdo

Se o usuário não especificar o conceito, peça o tema principal da assignment. Leia [references/assignment-guide.md](references/assignment-guide.md) antes de definir dificuldade, escopo e necessidade de arquivos auxiliares.

### 2. Criar a assignment

1. Escolha um identificador em `kebab-case`.
2. Crie `assignments/<id>/README.md` seguindo [templates/assignment-template.md](../../../templates/assignment-template.md).
3. Inclua `starter-code.py`, `data.csv` ou outros arquivos somente quando forem necessários para a atividade.
4. Mantenha os cabeçalhos e a estrutura exigidos pelas instruções de `assignments/**/*.md`.

### 3. Registrar no site

Não edite `config.json` manualmente. Execute:

```bash
node .github/skills/new-assignment/scripts/update-config.js <id> "<title>" "<description>"
```

Para cada arquivo auxiliar, registre um attachment:

```bash
node .github/skills/new-assignment/scripts/add-attachment.js <id> "<display-name>" <filename> <type>
```

Tipos comuns: `python`, `csv`, `json`, `txt` e `html`.

### 4. Verificar

Confirme que:

- `assignments/<id>/README.md` existe e segue o template;
- todos os arquivos referenciados como attachments existem;
- `config.json` contém a assignment e seus attachments;
- os scripts terminaram sem erros.