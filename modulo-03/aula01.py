# import requests

# # == Exercicio 01 ==
# conteudo = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# print(conteudo.status_code)

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula01.py
# 200




# # == Exercicio 02 ==
# print(conteudo.json())

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula01.py
# {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}


# # == Desafio ==
# dados = conteudo.json()

# print(dados["userId"])
# print(dados["id"])
# print(dados["title"])
# print(dados["completed"])

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula01.py
# Traceback (most recent call last):
#   File "C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03\aula01.py", line 26, in <module>
#     print(item["userId"])
#           ~~~~^^^^^^^^^^
# TypeError: byte indices must be integers or slices, not str
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula01.py
# Traceback (most recent call last):
#   File "C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03\aula01.py", line 26, in <module>
#     print(item[userId])
#                ^^^^^^
# NameError: name 'userId' is not defined
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula01.py
#   File "C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03\aula01.py", line 25
#     print(dados[userId])
# IndentationError: unexpected indent
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula01.py
# Traceback (most recent call last):
#   File "C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03\aula01.py", line 25, in <module>
#     print(dados[userId])
#                 ^^^^^^
# NameError: name 'userId' is not defined
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula01.py
# 1
# 1
# delectus aut autem
# False





# # == Desafio Extra ==

# Resultado: