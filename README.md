# 🚀 Projeto FastAPI - Gerenciamento de Bandas Musicais

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-92003B)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-5E81AC?logo=uvicorn)

## 📌 Sobre o Projeto

API desenvolvida durante estudos de FastAPI para gerenciar bandas musicais e seus álbuns.  
**Objetivos**:

- Aprender os fundamentos do FastAPI
- Implementar boas práticas de validação com Pydantic
- Criar documentação interativa automática

## 📚 Conteúdo Estudado

```asciiart
  📁 AULAS/
  ├── 📄 AULA_1/
  │   ├── ⚡ Instalação do FastAPI
  │   ├── 🏗️  Criação de endpoints básicos
  │   └── 📊 Swagger UI automático
  │
  ├── 📄 AULA_2/
  │   ├── 🎯 Path Parameters
  │   ├── 🔍 Validação com Enums
  │   └── 🚦 Códigos de status HTTP
  │
  └── 📄 AULA_3/
      ├── 🏷️  Modelos Pydantic
      ├── 🧩 Dados aninhados (Band + Album)
      └── 📝 Schemas de documentação
```

## 🛠️ Tecnologias Utilizadas

```diff
+ FastAPI 0.95+
+ Python 3.10+
+ Pydantic V2
+ Uvicorn (ASGI Server)
```

## ⚙️ Como Executar

```bash
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar e instalar dependências
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
pip install fastapi uvicorn

# 3. Iniciar servidor
uvicorn main:app --reload
```

## 🌐 Endpoints Principais

| Método | Rota               | Descrição                 |
| ------ | ------------------ | ------------------------- |
| GET    | `/bands`           | Lista todas as bandas     |
| GET    | `/bands/{id}`      | Detalhes de uma banda     |
| GET    | `/bands/genre/{g}` | Filtra por gênero musical |

## 📄 Documentação Interativa

Acesse automaticamente gerada:

- Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

## 📝 Lições Aprendidas

```markdown
✓ [X] Criar APIs RESTful com FastAPI  
✓ [X] Validar dados com Python Enums  
✓ [X] Gerar documentação automática  
○ [ ] Implementar autenticação (próxima aula)
```

## 📌 Créditos

Baseado no curso [BugBytes - FastAPI](https://www.youtube.com/playlist?list=PL-2EBeDYMIbQghmnb865lpdmYyWU3I5F1)  
Adaptado para estudos pessoais por @[sxwuell](https://github.com/samuelluzsantana)
