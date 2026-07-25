# === Exercicio 01 ===
# idade = 17
# tem_carteira = True

# if idade >= 18 and tem_carteira:
#     print("Pode dirigir!")
# else:
#     print("Não pode dirigir!")

# Resultado:
# S C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula05.py
# Pode dirigir!
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula05.py
# Não pode dirigir!

# === Exercicio 02 ===
# dia = "segunda"
# feriado = False

# if dia == 'sabado' or dia == 'domingo' or feriado == True:
#     print("É dia de descanso")
# else:
#     print("Não é :( ")

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula05.py
# É dia de descanso
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula05.py
# Não é :( 

# # === Exercicio 03 ===
# logado = False
# print (not logado)

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula05.py
# False
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula05.py
# True


# # === Desafio ===
# nome = input("Informe o seu nome: ")
# idade = int(input("Informe a sua idade: "))
# CNH = input("Posui CNH: (S ou N): ")

# if idade >= 18 and CNH == 'S':

#     print(f"""
#           Nome: {nome}
#           Idade: {idade}
#           CNH: {CNH}
#           Pode dirigir: Sim
#     """)
# elif idade < 18 or CNH == 'N':
#     print(f"""
#           Nome: {nome}
#           Idade: {idade}
#           CNH: {CNH}
#           Pode dirigir: Não
#     """)

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula05.py
# Informe o seu nome: k
# Informe a sua idade: 19
# Posui CNH: (S ou N)S

#           Nome: k
#           Idade: 19
#           CNH: S
#           Pode dirigir: Sim
    
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula05.py
# Informe o seu nome: k
# Informe a sua idade: 16
# Posui CNH: (S ou N): S

#           Nome: k
#           Idade: 16
#           CNH: S
#           Pode dirigir: Não
    
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula05.py
# Informe o seu nome: k
# Informe a sua idade: 19
# Posui CNH: (S ou N): N

#           Nome: k
#           Idade: 19
#           CNH: N
#           Pode dirigir: Não
    
