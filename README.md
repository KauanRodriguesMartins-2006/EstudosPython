Roadmap de Estudos — Python → APIs → SQLite → POO → Playwright → RPA

Objetivo: desenvolver uma base sólida em Python para automação, consumo de APIs, bancos de dados e RPA, terminando com projetos práticos para o GitHub.

Status:

✅ Concluído
🟨 Em andamento
⬜ Ainda não iniciado
Módulo 1 — Fundamentos do Python ✅
Aula 1 ✅
Variáveis
print()
Tipos de dados
input()
Aula 2 ✅
Operadores matemáticos
Conversão de tipos
Cálculos
Aula 3 ✅
if
else
elif
Operadores relacionais
Aula 4 ✅
Operadores lógicos
and
or
not
Aula 5 ✅
while
Loops
Contadores
Aula 6 ✅
break
continue
Loops controlados
Aula 7 ✅
for
range()
Aula 8 ✅
Strings
len()
upper()
lower()
strip()
replace()
Operador in
Aula 9 ✅
Listas
append()
Alteração de elementos
Percorrendo listas
Aula 10 ✅
Funções
def
Reutilização de código
Aula 11 ✅
Parâmetros
Múltiplos parâmetros
Aula 12 ✅
return
Funções que retornam valores
Aula 13 ✅
Escopo
Variáveis locais
Variáveis globais
Projeto Final ✅
Sistema Escolar
Cadastro de alunos
Listas
Funções
Menu
while
Módulo 2 — Estruturas de Dados, Arquivos e Erros ✅
Aula 1 ✅
Tuplas
Tuplas
Acesso aos elementos
Imutabilidade
Aula 2 ✅
Dicionários
Chave e valor
Acesso
Alteração
Adição
Percorrendo dicionários
Aula 3 ✅
Lista de dicionários
Estruturas de dados compostas
Percorrendo listas de dicionários
Manipulação dos dados
Aula 4 ✅
Arquivos
.txt
open()
read()
write()
append()
with
Aula 5 ✅
JSON
json.dumps()
json.loads()
Estrutura JSON
Aula 6 ✅
JSON + arquivos
json.dump()
json.load()
Persistência de dados
Aula 7 ✅
Tratamento de erros
try
except
finally
FileNotFoundError
ValueError
KeyError
Aula 8 ✅
Módulos
import
from ... import ...
Bibliotecas do Python
Projeto Final ✅
Sistema de Cadastro

Utilizando:

Listas
Dicionários
JSON
Arquivos
Tratamento de erros
Funções
Módulos
Módulo 3 — Requests e APIs ✅
Aula 1 ✅
Introdução às APIs
O que é uma API
Cliente x servidor
HTTP
Requisições
Respostas
Status codes
Aula 2 ✅
Biblioteca Requests
requests
requests.get()
requests.post()
URLs
Parâmetros
Aula 3 ✅
Trabalhando com JSON
response.json()
Listas e dicionários vindos de APIs
Processamento das respostas
Aula 4 ✅
APIs públicas
JSONPlaceholder
BrasilAPI
Consulta de dados
Aula 5 ✅
Session
requests.Session()
Headers
Cookies
Persistência entre requisições
Aula 6 ✅
Respostas HTTP
response.status_code
response.headers
response.text
response.content
response.encoding
Aula 7 ✅
Tratamento de erros em Requests
raise_for_status()
HTTPError
ConnectionError
Timeout
RequestException
Aula 8 ✅
Organização com funções
Parâmetros
return
Funções para consultas
Separação de responsabilidades
Projeto Final ✅
Consultor API

Aplicação CLI capaz de:

Consultar dados de usuários
Consultar posts de usuários
Consultar posts individuais
Analisar posts
Gerar estatísticas
Utilizar requests.Session()
Utilizar tratamento de erros
Utilizar ambiente virtual
Organizar o código em funções
Módulo 4 — SQLite3 🟨

Objetivo: aprender a armazenar e manipular dados de forma persistente usando banco de dados.

Aula 1
Introdução a Bancos de Dados
O que é banco de dados
Tabelas
Registros
Colunas
Chave primária
Banco relacional
SQL
SQLite
SQLite x MySQL/MariaDB
CRUD
Aula 2
SQLite no Python
Biblioteca sqlite3
connect()
cursor()
execute()
commit()
close()
Aula 3
Criando tabelas
CREATE TABLE
Tipos de dados
PRIMARY KEY
NOT NULL
Estrutura de tabelas
Aula 4
Inserindo dados
INSERT
Parâmetros com ?
Inserção através do Python
commit()
Aula 5
Consultando dados
SELECT
WHERE
fetchone()
fetchall()
Filtros
Aula 6
Alterando e removendo dados
UPDATE
DELETE
Condições com WHERE
Aula 7
Tratamento de erros com SQLite
Exceções do sqlite3
Tratamento de erros
Conexão segura
Organização das operações
Aula 8
Organizando o acesso ao banco
Funções para banco de dados
Separação de responsabilidades
Reutilização de código
Projeto Final
Sistema de Cadastro com SQLite

Aplicação CLI utilizando:

Python
SQLite
CRUD
Funções
Tratamento de erros
Persistência de dados
Módulo 5 — Programação Orientada a Objetos (POO) ⬜
Aula 1
Conceitos de POO
Classes
Objetos
Atributos
Métodos
Aula 2
Criando classes
class
__init__
self
Aula 3
Métodos e atributos
Métodos de instância
Modificação de atributos
Organização
Aula 4
Encapsulamento
Atributos privados
property
Getters e setters
Aula 5
Organização com POO
Divisão de responsabilidades
Classes trabalhando juntas
Projeto Final
Sistema utilizando POO + SQLite
Módulo 6 — Bibliotecas e Organização de Projetos ⬜
Aula 1
pathlib
Caminhos
Arquivos
Diretórios
Aula 2
os
Sistema operacional
Diretórios
Variáveis de ambiente
Operações com arquivos
Aula 3
Ambientes e dependências
.venv
pyproject.toml
uv
Dependências
Aula 4
Organização de projetos
Estrutura de diretórios
Módulos
__init__.py
Separação de responsabilidades
README
Projeto
Ferramenta de gerenciamento de arquivos
Módulo 7 — Playwright ⬜
Aula 1
Introdução ao Playwright
O que é automação web
Instalação
Navegadores
Aula 2
Navegação
Abrir sites
URLs
Navegação entre páginas
Aula 3
Elementos
Localizadores
Inputs
Botões
Textos
Aula 4
Interação
Preenchimento de formulários
Cliques
Seleções
Aula 5
Esperas
Elementos
Carregamento
Sincronização
Aula 6
Arquivos
Download
Upload
Aula 7
Screenshots
Captura de tela
Evidências de execução
Projeto Final
Automação de um site real
Módulo 8 — RPA ⬜
Automação completa
Organização de automações
Logs
Tratamento de erros
Configurações
Arquivos
APIs
Banco de dados
Playwright
Projetos
Robô de consulta
Robô de cadastro
Robô de coleta de informações
Robô de processamento de arquivos
Automação API + SQLite + Playwright
Módulo 9 — Projetos para GitHub ⬜

Projetos completos para portfólio:

Consulta CEP
Consulta CNPJ
Agenda
Controle financeiro
Sistema escolar
Cadastro de clientes
Web Scraper
Automação de Login
Automação de Downloads
API + SQLite
Dashboard em terminal
RPA completo

Cada projeto poderá incluir:

README
.venv / dependências
Código organizado
Tratamento de erros
Git
GitHub
🎯 Objetivo Final

Ao concluir o roadmap, você deverá ser capaz de:

✅ Criar programas em Python

✅ Estruturar programas usando funções e POO

✅ Trabalhar com arquivos e JSON

✅ Consumir APIs

✅ Tratar erros de aplicações e requisições

✅ Utilizar bancos de dados SQLite

✅ Integrar APIs + banco de dados

✅ Automatizar sites com Playwright

✅ Criar automações RPA

✅ Organizar projetos profissionais

✅ Criar projetos completos para o GitHub

✅ Ter uma base sólida para posteriormente estudar frameworks como FastAPI, Flask ou Django

🚀 Progresso Atual
✅ Módulo 1 — Fundamentos do Python
✅ Módulo 2 — Estruturas de Dados, Arquivos e Erros
✅ Módulo 3 — Requests e APIs
🟨 Módulo 4 — SQLite3
⬜ Módulo 5 — POO
⬜ Módulo 6 — Bibliotecas e Organização
⬜ Módulo 7 — Playwright
⬜ Módulo 8 — RPA
⬜ Módulo 9 — Projetos para GitHub
📌 Observação

Este roadmap representa minha evolução nos estudos de Python. Os módulos e projetos serão atualizados conforme novos conhecimentos forem adquiridos e novas necessidades surgirem.
