# 🧩 WebAPI Users — CRUD de Usuários com FastAPI

API REST desenvolvida com **FastAPI**, **SQLAlchemy** e **SQLite**, com objetivo de demonstrar a criação de um CRUD completo (Create, Read, Update, Delete) em Python moderno.

Este projeto faz parte do meu portfólio como desenvolvedor backend, com foco em APIs e boas práticas de estrutura de código.

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python 3.12**
- ⚡ **FastAPI** — framework moderno para APIs REST
- 🗄️ **SQLAlchemy** — ORM para interação com banco de dados
- 💾 **SQLite** — banco de dados leve e local
- 🧱 **Pydantic v2** — validação e serialização de dados
- 🧪 **Uvicorn** — servidor ASGI para desenvolvimento

---

📁 Estrutura do projeto
webapi_users_fastapi/
├──App/
   ├── main.py
   ├── models.py
   ├── schemas.py
   ├── database.py
   ├── crud.py
├── users.db
└── requirements.txt

## ⚙️ Como executar o projeto

### 1 Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/webapi_users_fastapi.git
cd webapi_users_fastapi

2 Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

3 Instalar dependências
pip install -r requirements.txt

4️⃣ Executar a API
uvicorn main:app --reload

Acesse no navegador:
👉 http://127.0.0.1:8000/docs

para abrir a interface interativa do Swagger.

🧠 Funcionalidades

✅ Criar um novo usuário
✅ Listar todos os usuários cadastrados
✅ Buscar usuário por ID
✅ Atualizar dados de um usuário existente
✅ Remover um usuário do banco de dados

💡 Aprendizados e Objetivo

Este projeto foi criado para consolidar conhecimentos em:

Estruturação de API moderna com FastAPI

Uso do ORM SQLAlchemy para persistência de dados

Definição de modelos e esquemas (Model x Schema)

Integração entre FastAPI, Pydantic e SQLite

Boas práticas para portfólio backend

📸 Interface de Testes

O projeto inclui a interface Swagger UI gerada automaticamente pelo FastAPI:



🧑‍💻 Autor

Everson Coelho Magalhães
Desenvolvedor Backend Python | Experiência com PHP, Delphi e WordPress
🐝 Projeto criado como parte de meu portfólio

📬 Perfil no LinkedIn

🐙 GitHub

📜 Licença

Este projeto é distribuído sob a licença MIT.
Sinta-se livre para usar e modificar para fins de aprendizado. 🎓
⭐ Se este projeto te ajudou, deixe uma estrela no repositório!
