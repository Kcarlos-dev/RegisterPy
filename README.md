
# RegisterPy

RegisterPy é uma API RESTful para sistema de pedidos e cadastro, construída com **Flask**. A API oferece endpoints para gerenciamento de usuários, itens de menu e pedidos, com **autenticação JWT** e **controle de acesso baseado em função**.

---

## 🔥 Funcionalidades

- **🔐 Autenticação de Usuário:** Registro e login com geração de tokens JWT.
- **🛡️ Controle de Acesso por Função:** Middleware para restringir rotas com base no tipo de usuário (`admin`, `user`, `stockist`).
- **🍔 Gerenciamento de Itens:** CRUD de itens de menu, com permissões específicas para admins e estoquistas.
- **🛒 Gerenciamento de Pedidos:** Criação de pedidos e atualização automática de estoque.
- **🧱 Migrações de Banco:** Usando `Flask-Migrate` para versionamento do schema.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python, Flask  
- **Banco de Dados:** MySQL, SQLAlchemy  
- **Autenticação:** Flask-JWT-Extended  
- **Migrações:** Flask-Migrate, Alembic  
- **Servidor WSGI:** Gunicorn

---

## 📁 Estrutura do Projeto

```
RegisterPy/
├── app/
│   ├── __init__.py         # Inicialização da app e extensões
│   ├── extensions.py       # Instâncias: db, migrate, jwt
│   ├── middleware/
│   │   └── auth.py         # Middleware de controle de acesso por função
│   ├── models/
│   │   ├── user.py         # Modelo do usuário
│   │   ├── menu_item.py    # Modelo dos itens do menu
│   │   └── order.py        # Modelo dos pedidos
│   └── routes/
│       ├── auth_routes.py  # Rotas de login/registro
│       ├── item_routes.py  # Rotas dos itens
│       └── order_routes.py # Rotas dos pedidos
├── migrations/             # Migrações com Alembic
├── .env.example            # Exemplo de .env
├── .gitignore              # Arquivos ignorados pelo Git
├── config.py               # Configuração Flask
├── requirements.txt        # Dependências Python
└── wsgi.py                 # Entry point do Gunicorn
```

---

## 🚀 Configuração e Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Kcarlos-dev/MyLoc.git
cd RegisterPy
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

Copie o `.env.example` e edite com suas configs:

```env
DB_HOST=seu_host_de_bd
DB_PORT=sua_porta_de_bd
DB_DATABASE=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
SECRET_KEY=sua_chave_flask
JWT_SECRET_KEY=sua_chave_jwt
```

### 5. Execute as migrações

```bash
flask db upgrade
```

### 6. Inicie a aplicação

Modo dev:

```bash
flask run
```


## 📡 Endpoints da API

### 🔐 Autenticação

| Método | Rota                | Descrição                              | Acesso      |
|--------|---------------------|----------------------------------------|-------------|
| POST   | `/api/users/register` | Cadastra novo usuário                  | Público     |
| POST   | `/api/users/login`    | Realiza login e retorna token JWT      | Público     |
| GET    | `/api/users/me`       | Dados do usuário autenticado           | Autenticado |

---

### 🍔 Itens do Menu

| Método | Rota                   | Descrição                          | Acesso           |
|--------|------------------------|------------------------------------|------------------|
| POST   | `/api/items/register`  | Registra novo item                 | admin, stockist  |
| GET    | `/api/items`           | Lista todos os itens do menu      | user, admin      |

---

### 🛒 Pedidos

| Método | Rota                    | Descrição                        | Acesso   |
|--------|-------------------------|----------------------------------|----------|
| POST   | `/api/orders/register`  | Registra um novo pedido          | user, admin |
| GET    | `/api/orders`           | Lista todos os pedidos           | admin    |

---



Apenas converti um repositorio meu usando ia. Repositorio original:. https://github.com/Kcarlos-dev/MyLoc