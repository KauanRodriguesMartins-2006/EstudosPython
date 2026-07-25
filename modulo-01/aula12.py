# # == Exercicio 01 ==
# def cumprimentar(nome):
#     print(f"Olá, {nome}")

# cumprimentar("Kauan")
# cumprimentar("Daniel")
# cumprimentar("Gabriel")
# cumprimentar("Sarah")

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula12.py
# Olá, Kauan
# Olá, Daniel
# Olá, Gabriel
# Olá, Sarah




# # == Exercicio 02 ==
# def quadrado(numero):
#     print(numero * numero)

# quadrado(5)
# quadrado(12)
# quadrado(11)
# quadrado(-44)

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula12.py
# 25
# 144
# 121
# 1936




# # == Exercicio 03 ==
# def mostrar_idade(nome, idade):
#     print(f"""
#     Nome: {nome}
#     Idade: {idade}
# """)

# mostrar_idade("Kauan", 19)
# mostrar_idade("João", 21)

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula12.py

#     Nome: Kauan
#     Idade: 19

#     Nome: João
#     Idade: 21


# # == Desafio ==
# def boletim(nome, nota1, nota2):
#     media = (nota1 + nota2) / 2
#     print(f"""
# ====================
# Boletim

# Aluno: {nome}

# Nota 1: {nota1}
# Nota 2: {nota2}

# Média: {media}
# ====================

# """)
    
# boletim("Lima", 8.5, 9.8)

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula12.py

# ====================
# Boletim

# Aluno: Lima

# Nota 1: 8.5
# Nota 2: 9.8

# Média: 9.15
# ====================



# # == Desafio Extra ==
# def maior(num1, num2):
#     if num1 > num2:
#         print(f"{num1} é maior que {num2}")
#     elif num1 == num2:
#         print(f"{num1} é igual ao {num2}")
#     else:
#         print(f"{num2} é maior que {num1}")

# maior(5, 8)
# maior(8, 3)
# maior(7, 7)

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula12.py
# 8 é maior que 5
# 8 é maior que 3
# 7 é igual ao 7