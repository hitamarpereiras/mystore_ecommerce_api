# API de E-commerce

Uma API Django REST para gerenciar usuários, clientes, lojas, categorias, produtos e pedidos.

## Visão geral

- Projeto baseado em **Django 6** com **Django REST Framework**.
- Autenticação via **JWT** (`rest_framework_simplejwt`).
- Banco de dados padrão em **SQLite** (`ecommerce.sqlite3`).
- O campo de pedidos `itens` é um **JSON** que representa uma lista de produtos.

## Arquitetura da API

- Base URL: `/api/v1/`
- Rotas principais:
  - `/api/v1/authentication/token/`
  - `/api/v1/authentication/token/refresh/`
  - `/api/v1/accounts/`
  - `/api/v1/customers/`
  - `/api/v1/stores/`
  - `/api/v1/categories/`
  - `/api/v1/products/`
  - `/api/v1/orders/`

## Instalação

1. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute migrações:

```bash
python manage.py migrate
```

4. Crie um superusuário (opcional):

```bash
python manage.py createsuperuser
```

5. Rode a aplicação:

```bash
python manage.py runserver
```

## Configuração

- O arquivo de configuração principal é `core/settings.py`.
- O modelo de usuário customizado está definido em `apps/accounts/models.py`.
- O banco SQLite padrão é `ecommerce.sqlite3`.
- `AUTH_USER_MODEL = 'accounts.User'`.

## Autenticação

A API utiliza JWT para autenticação.

### Obter token de acesso

**POST** `/api/v1/authentication/token/`

Corpo:

```json
{
  "email": "usuario@example.com",
  "password": "senha123"
}
```

Resposta esperada:

```json
{
  "access": "<jwt-access-token>",
  "refresh": "<jwt-refresh-token>"
}
```

### Atualizar token

**POST** `/api/v1/authentication/token/refresh/`

Corpo:

```json
{
  "refresh": "<jwt-refresh-token>"
}
```

Resposta esperada:

```json
{
  "access": "<jwt-access-token-novo>"
}
```

> Para chamadas protegidas, envie o cabeçalho `Authorization: Bearer <token>`.

## Recursos disponíveis

### Accounts

- **GET** `/api/v1/accounts/` — lista usuários (apenas para superusuários ou usuário próprio).
- **GET** `/api/v1/accounts/{id}/` — recuperar usuário.
- **POST** `/api/v1/accounts/` — criar usuário som pouco uso interno.
- **PUT/PATCH** `/api/v1/accounts/{id}/` — atualizar usuário.
- **DELETE** `/api/v1/accounts/{id}/` — remover usuário.

Campos relevantes:

- `id`
- `email`
- `first_name`
- `last_name`
- `is_active`
- `telephone`

### Customers

- **POST** `/api/v1/customers/register/` — registrar cliente.
- **GET** `/api/v1/customers/` — lista cliente(s) do usuário autenticado.
- **GET** `/api/v1/customers/{id}/` — recuperar cliente.
- **PUT/PATCH** `/api/v1/customers/{id}/` — atualizar cliente.
- **DELETE** `/api/v1/customers/{id}/` — excluir cliente.

Campos relevantes:

- `id`
- `first_name`
- `last_name`
- `telephone`
- `address`
- `house_number`
- `coins`
- `premium`
- `avatar_url`
- `avatar_path`

### Stores

- **GET** `/api/v1/stores/` — lista lojas. Público para `list` e `retrieve`.
- **GET** `/api/v1/stores/{id}/` — recuperar loja.
- **POST** `/api/v1/stores/` — criar loja (autenticado).
- **PUT/PATCH** `/api/v1/stores/{id}/` — atualizar loja (autenticado).
- **DELETE** `/api/v1/stores/{id}/` — remover loja (autenticado).

Campos relevantes:

- `id`
- `owner`
- `name`
- `phone`
- `address`
- `cnpj`
- `avatar_url`
- `avatar_path`
- `instagram_url`
- `facebook_url`
- `other_url`
- `color_palette`

### Categories

- **GET** `/api/v1/categories/` — listar categorias. Público.
- **GET** `/api/v1/categories/{id}/` — recuperar categoria. Público.
- **POST** `/api/v1/categories/` — criar categoria (autenticado).
- **PUT/PATCH** `/api/v1/categories/{id}/` — atualizar categoria (autenticado).
- **DELETE** `/api/v1/categories/{id}/` — remover categoria (autenticado).

Campos relevantes:

- `id`
- `owner`
- `name`
- `description`

### Products

- **GET** `/api/v1/products/` — lista produtos.
- **GET** `/api/v1/products/{id}/` — recuperar produto.
- **POST** `/api/v1/products/` — criar produto (autenticado).
- **PUT/PATCH** `/api/v1/products/{id}/` — atualizar produto (autenticado).
- **DELETE** `/api/v1/products/{id}/` — remover produto (autenticado).

Filtros suportados:

- `?store=<store_id>`
- `?category=<category_id>`
- `?price=<preco>`
- `?name=<nome>`

Campos relevantes:

- `id`
- `owner`
- `store`
- `name`
- `category`
- `description`
- `price`
- `stock`
- `image_url`
- `image_path`
- `crop_x`
- `crop_y`
- `crop_width`
- `crop_height`

> O campo `image` é aceito como `multipart/form-data` na criação/atualização, mas é removido antes da persistência.

### Orders

- **GET** `/api/v1/orders/` — lista pedidos do cliente autenticado.
- **GET** `/api/v1/orders/{id}/` — recuperar pedido.
- **POST** `/api/v1/orders/` — criar pedido.
- **PUT/PATCH** `/api/v1/orders/{id}/` — atualizar pedido.
- **DELETE** `/api/v1/orders/{id}/` — remover pedido.

Campos do pedido:

- `id`
- `store`
- `customer`
- `name_customer`
- `phone`
- `observation`
- `address`
- `latitude`
- `longitude`
- `house_number`
- `total`
- `subtotal`
- `remaining`
- `payment_method`
- `rate_delivery`
- `code`
- `created_at`
- `itens`
- `status`

### Detalhes do campo `itens`

O campo `itens` é um `JSONField` e deve ser enviado como uma **lista** de objetos representando produtos.

Cada item deve conter ao menos:

- `id`: ID do produto
- `name`: nome do produto
- `quantity`: quantidade do produto

Exemplo válido:

```json
"itens": [
  {
    "id": 1,
    "name": "Camiseta",
    "quantity": 2
  },
  {
    "id": 4,
    "name": "Caneca",
    "quantity": 1
  }
]
```

### Como o `signal` de pedido funciona

- O sinal está em `apps/orders/signals.py`.
- Ele escuta `pre_save` do modelo `Order`.
- Quando um pedido existente muda de `status: false` para `status: true`, o estoque do produto é decrementado.
- O sinal usa:
  - `item['id']` para buscar o produto.
  - `item['quantity']` para reduzir o estoque.

> Se `itens` for uma `str`, o código tenta converter com `json.loads`. Se for um `dict`, converte em lista.

## Observações importantes

- A entidade `Customer` está ligada a `User` via `OneToOneField`.
- A entidade `Store` usa `id` customizado gerado por `services.idgenerator_svc.generate_idStore`.
- As rotas públicas são `stores` e `categories` para listagem/recuperação.
- A maioria das demais rotas exige autenticação JWT.

## Estrutura de pastas relevante

- `apps/accounts/` — usuário e autenticação.
- `apps/customers/` — clientes e registro.
- `apps/stores/` — lojas.
- `apps/categories/` — categorias de produto.
- `apps/products/` — produtos.
- `apps/orders/` — pedidos e regra de estoque.
- `core/` — configurações, URLs e permissões.

## Executando em desenvolvimento

```bash
python manage.py runserver
```

A API ficará disponível em `http://127.0.0.1:8000/api/v1/`.

## Notas finais

- Use sempre `Authorization: Bearer <token>` nas requisições autenticadas.
- Valide o JSON de `itens` para garantir `id`, `name` e `quantity` presentes.
- O campo `status` de pedido controla o disparo do ajuste de estoque.
