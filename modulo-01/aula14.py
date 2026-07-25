# # == Exercicio 01 ==
# def mensagem():
#     texto = "Olá"

#     print(texto)

# mensagem()
# Resultado:
# ++Resultado que eu espero que vai acontecer:
#     vai imprimir a palavra Olá
# ++Resultado do código:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula14.py
# Olá



# # == Exercicio 02 ==
# nome = "Python"

# def mostrar():
#     print(nome)

# mostrar()
# Resultado:
# ++Resultado que eu espero que vai acontecer:
#     vai imprimir a palavra Python
# ++Resultado do código:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula14.py
# Python


# # == Exercicio 03 ==
# cidade = "Salvador"

# def trocar():
#     cidade = "São Paulo"
#     print(cidade)

# trocar()

# print(cidade)

# Resultado:
# ++Resultado que eu espero que vai acontecer:
    # Ele vai imprimir primeiro são paulo e depois salvador, pois uma variavel local não é afetada pela global e 
    # e como a baixo o print depois do trocar não esta dentro do def ele não vai imprimir a variavel cidade do def e
    # sim a global (espero que eu tenho conseguido explicar o que eu quis dizer)
# ++Resultado do código:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula14.py
# São Paulo
# Salvador


# # == Desafio ==
# empresa = "OpenAI"

# def saudacoes():
#     print(f"Bem-vindo á {empresa}")
    
# saudacoes()

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula14.py
# Bem-vindo á Anthropic




# # == Desafio Extra ==
# def ErrorTest():
#     cargo = 538
    
# print(cargo)

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula14.py
# Traceback (most recent call last):
#   File "C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01\aula14.py", line 73, in <module>
#     print(cargo)
#           ^^^^^
# NameError: name 'cargo' is not defined