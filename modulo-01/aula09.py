# # == Exercicio 01 ==
# nome = "Python"
# print(nome [0])
# print(nome [5])

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula09.py                                                 
# P
# n

# # == Exercicio 02 ==
# nome = input("Digite o seu nome: ")

# print(len(nome))
# print(nome.upper())
# print(nome.lower())

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula09.py
# Digite o seu nome: Kauan
# 5
# <built-in method upper of str object at 0x000002544D6EB930>
# <built-in method lower of str object at 0x000002544D6EB930>
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula09.py
# Digite o seu nome: Kauan
# 5
# KAUAN
# kauan

# # == Exercicio 03 ==
# frase = input("Digite uma frase: ")

# print("Python" in frase)

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula09.py
# Digite uma frase: Dreams falling down like shooting stars
# False
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula09.py
# Digite uma frase: Eu estou estudando Python
# True

# # == Desafio ==
# nomeCompleto = input("Digite o seu nome completo: ")

# print(nomeCompleto)
# print(nomeCompleto.strip())
# print(nomeCompleto.upper())
# print(nomeCompleto.lower())
# print(len(nomeCompleto))

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula09.py
# Digite o seu nome completo:            Kauan Rodrigues Martins              
#            Kauan Rodrigues Martins              
# Kauan Rodrigues Martins
#            KAUAN RODRIGUES MARTINS              
#            kauan rodrigues martins              
# 48

# # == Desafio Extra ==
# frase = input("Digite uma frase que contenha a palavra Python: ")

# print(frase.replace("Python","16252081514"))

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula09.py
# Digite uma frase que contenha a palavra python: Eu estou estudando Python
# Eu estou estudando 16252081514

