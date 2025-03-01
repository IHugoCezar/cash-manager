# 🚀 Django Cash-Manager
# Docker não foi testado antes do envio

Este é um **API de Carteira Django**, containerizado com **Docker**. A aplicação fornece funcionalidades para gerenciar carteiras de usuários e converter saldos entre moedas dinamicamente usando a **API Fixer.io**.

---

## 📌 Recursos
- **API REST baseada em Django** para gerenciamento de carteiras
- **Banco de dados SQLite** (armazenado como um volume)
- **Conversão de moeda** usando **API Fixer.io**
- **Gunicorn para servidor WSGI pronto para produção**
- **Variáveis de ambiente para credenciais de API seguras**
- **Aplicação Dockerizada** para fácil implantação

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.11**
- **Django 5.1**
- **Gunicorn** (para servidor WSGI)
- **SQLite** (banco de dados padrão)
- **API Fixer.io** (conversão de moedas)
- **Docker & Docker Compose**

---

## 📂 Estrutura do Projeto
```
/project_root/
│── /wallet/            # Pasta do aplicativo Django
│── /templates/         # Templates HTML do Django
│── db.sqlite3          # Banco de dados SQLite (montado como volume)
│── .env                # Variáveis de ambiente
│── Dockerfile          # Arquivo de configuração do Docker
│── docker-compose.yml  # Configuração do Docker Compose
│── requirements.txt    # Dependências do Python
│── manage.py           # Script de gerenciamento do Django
```

---

## 🔧 Configuração e Instalação

### 1️⃣ **Clonar o Repositório**
```sh
git clone https://github.com/IHugoCezar/cash-manager
cd django-wallet-api
```

### 2️⃣ **Criar um Arquivo `.env`**
Crie um arquivo `.env` no diretório raiz do projeto e adicione:
```ini
FIXER_API_KEY=sua_chave_da_api_fixer
```

### 3️⃣ **Construir e Executar os Contêineres Docker**
```sh
docker-compose up --build -d
```

### 4️⃣ **Acessar a Aplicação**
- Abrir a API: **`http://127.0.0.1:8000/`**
- Acessar Django Admin: **`http://127.0.0.1:8000/admin/`**

---

## 🖥️ Executando Sem Docker (Opcional)
Se preferir executar sem Docker:

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🚀 Endpoints da API
| **Endpoint** | **Método** | **Descrição** |
|-------------|-----------|----------------|
| `/wallets/` | `GET` | Lista todas as carteiras |
| `/wallets/novo/` | `POST` | Cria uma nova carteira |
| `/wallets/<id>/editar/` | `PUT/PATCH` | Atualiza uma carteira |
| `/wallets/<id>/deletar/` | `DELETE` | Exclui uma carteira |

---

## 🏗️ Explicação do Dockerfile
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "manager.wsgi:application"]
```
🔹 **Usa Gunicorn** para servir a aplicação Django de forma eficiente.
🔹 **Expõe a porta 8000** para acesso à API.

---

## 📜 Licença
Este projeto está licenciado sob a **Licença MIT**.

---

## 👨‍💻 Autor
**Seu Nome** - [GitHub](https://github.com/IHugoCezar)

---

## 🎯 Próximos Passos
- ✅ Adicionar PostgreSQL em vez de SQLite
- ✅ Implementar autenticação (JWT ou OAuth2)
- ✅ Melhorar logs e monitoramento

🚀 **Feliz Codificação!** 😊

