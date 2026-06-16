# b2bflow-python-challenge

Desafio técnico para a vaga de Estágio em Desenvolvimento Python da b2bflow.

## Objetivo

Ler contatos cadastrados no Supabase e enviar uma mensagem personalizada via Z-API.

Mensagem enviada:

```text
Olá, <nome_contato> tudo bem com você?
```

## Estrutura da tabela

Tabela: `Contacts`

| Coluna | Tipo |
|---------|---------|
| id | int8 |
| name | text |
| phone_num | text |

## Variáveis de ambiente

Crie um arquivo `.env` com:

```env
SUPABASE_URL=
SUPABASE_KEY=

INSTANCE_ID=
INSTANCE_TOKEN=
CLIENT_TOKEN=
```

## Instalação

Criar ambiente virtual:

```bash
python -m venv .venv
```

Ativar ambiente:

```bash
.venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

## Tecnologias utilizadas

- Python
- Supabase
- Z-API
- python-dotenv

## Funcionamento

![execucao](photos/screenshot.png)