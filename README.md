# Payment Scheduler API

A Payment Scheduler API é uma aplicação web construída com Django, projetada para gerenciar agendamentos de pagamento. A API permite criar, listar, detalhar e deletar agendamentos de forma simples e eficiente.

## Funcionalidades

- **Criar Agendamentos**: Permite o registro de novos agendamentos de pagamento.
- **Listar Agendamentos**: Recupera uma lista de todos os agendamentos registrados.
- **Detalhar Agendamentos**: Fornece detalhes de um agendamento específico.
- **Deletar Agendamentos**: Remove um agendamento existente.

## Pré-requisitos

- Python 
- Django 
- SQLite 

## Instalação


1. **Instale as dependências**:

   ```bash
   pip install django
   ```

2. **Configure o banco de dados** (opcional, se estiver usando outro banco):

   Edite o arquivo `settings.py` conforme necessário para conectar ao seu banco de dados.

3. **Execute as migrações**:

   ```bash
   python manage.py migrate
   ```

4. **Inicie o servidor**:

   ```bash
   python manage.py runserver
   ```

## Endpoints

### 1. Criar Agendamento de Pagamento

- **Método**: `POST`
- **URL**: `/agendamentos/`
- **Corpo da Requisição**:
  
  ```json
  {
      "data_pagamento": "2024-09-15",
      "permite_recorrencia": true,
      "quantidade_recorrencia": 5,
      "intervalo_recorrencia": 30,
      "status_recorrencia": "ativa",
      "agencia": 1234,
      "conta": 567890,
      "valor_pagamento": 100.50
  }
  ```

### 2. Listar Agendamentos

- **Método**: `GET`
- **URL**: `/agendamentos/`

### 3. Detalhar Agendamento de Pagamento

- **Método**: `GET`
- **URL**: `/agendamentos/<id>/`

### 4. Deletar Agendamento de Pagamento

- **Método**: `DELETE`
- **URL**: `/agendamentos/deletar/<id>/`

## Exemplo de Uso com Postman

Você pode usar o [Postman](https://www.postman.com/) para testar a API. Abaixo estão alguns exemplos de requisições:

### Criar Agendamento

1. Abra o Postman.
2. Selecione o método `POST`.
3. Cole a URL: `http://localhost:8000/agendamentos/`.
4. No corpo da requisição, selecione **raw** e escolha **JSON**, e cole o JSON do exemplo acima.
5. Clique em **Send**.

### Listar Agendamentos

1. Selecione o método `GET`.
2. Cole a URL: `http://localhost:8000/agendamentos/`.
3. Clique em **Send**.

### Detalhar Agendamento

1. Selecione o método `GET`.
2. Cole a URL: `http://localhost:8000/agendamentos/1/` (substitua `1` pelo ID desejado).
3. Clique em **Send**.

### Deletar Agendamento

1. Selecione o método `DELETE`.
2. Cole a URL: `http://localhost:8000/agendamentos/deletar/1/` (substitua `1` pelo ID desejado).
3. Clique em **Send**.
