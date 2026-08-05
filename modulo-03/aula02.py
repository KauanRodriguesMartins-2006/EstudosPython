import requests

# # == Exercicio 01 ==
# conteudo = requests.get("https://brasilapi.com.br/api/cep/v1/42810582")

# dados = conteudo.json()

# print(dados["cep"])
# print(dados["city"])
# print(dados["state"])

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula02.py
# 42810582
# Camaçari
# BA


# # == Exercicio 02 ==
# us_cep = input("Digite um cep: ")

# conteudo = requests.get(f"https://brasilapi.com.br/api/cep/v1/{us_cep}")

# dados = conteudo.json()

# print(dados["street"])
# print(dados["neighborhood"])
# print(dados["city"])
# print(dados["state"])

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula02.py
# Digite um cep: 01001000
# Praça da Sé
# Sé
# São Paulo
# SP



# # == Exercicio 03 ==
# us_cep = input("Digite um cep: ")

# conteudo = requests.get(f"https://brasilapi.com.br/api/cep/v1/{us_cep}")

# dados = conteudo.json()

# if conteudo.status_code == 200:
#     print(dados["street"])
#     print(dados["neighborhood"])
#     print(dados["city"])
#     print(dados["state"])
# else:
#     print("Cep invalido")

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula02.py
# Digite um cep: 42810582
# Rua Cora Coralina 01
# Parque Verde III
# Camaçari
# BA
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula02.py
# Digite um cep: 80024922
# Cep invalido




# # == Desafio ==
# while True:
#     opc = int(input("""
# ==================
# Consulta CEP
# ==================

# 1. Consulta Cep
# 2. Sair

# Opção selecionada: """))
    
#     if opc == 1:
#         dg_cep = input("Digite um Cep: ")
        
#         conteudo = requests.get(f"https://brasilapi.com.br/api/cep/v1/{dg_cep}")

#         dados = conteudo.json()

#         if conteudo.status_code == 200:
#             print(f"""
# CEP........: {dados["cep"]}
# Rua........: {dados["street"]}
# Bairro.....: {dados["neighborhood"]}
# Cidade.....: {dados["city"]}
# Estado.....: {dados["state"]}
#             """)
#         else:
#             print("Cep invalido")
            
#     elif opc == 2:
#         print("Encerrando programa")
#         break

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula02.py

# ==================
# Consulta CEP
# ==================

# 1. Consulta Cep
# 2. Sair

# Opção selecionada: 42810582

# ==================
# Consulta CEP
# ==================

# 1. Consulta Cep
# 2. Sair

# Opção selecionada: 1
# Digite um Cep: 42810582

# CEP........: 42810582
# Rua........: Rua Cora Coralina 01
# Bairro.....: Parque Verde III
# Cidade.....: Camaçari
# Estado.....: BA
            

# ==================
# Consulta CEP
# ==================

# 1. Consulta Cep
# 2. Sair

# Opção selecionada: 1
# Digite um Cep: 798645312
# Cep invalido

# ==================
# Consulta CEP
# ==================

# 1. Consulta Cep
# 2. Sair

# Opção selecionada: 2
# Encerrando programa




# # == Desafio Extra ==

# Resultado: