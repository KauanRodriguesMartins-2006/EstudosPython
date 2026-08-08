import requests

# # == Exercicio 01 ==
db_bancos = requests.get("https://brasilapi.com.br/api/banks/v1")

dados = db_bancos.json()

# for item in dados:
#     print(item["name"])

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula04.py                                                       
# BCO DO BRASIL S.A.                                                                  
# BRB - BCO DE BRASILIA S.A.
# Selic
# Bacen
# SANTINVEST S.A. - CFI
# CCR SEARA
# AGK CC S.A.
# UNICRED DO BRASIL
# SEFER INVESTIMENTOS DTVM LTDA - EM LIQUIDAÇÃO EXTRAJUDICIAL
# CAIXA ECONOMICA FEDERAL
# STN
# FINAMAX S.A. CFI
# BANCO INTER
# COLUNA S.A. DTVM
# BCO RIBEIRAO PRETO S.A.
# ...



# # == Exercicio 02 ==
# cod = int(input("Digite o código do banco: "))

# for banco in dados:
#     if banco["code"] == cod:
#         print(f"""
# Nome..: {banco["name"]}
# Código: {banco["code"]}
# ISPB..: {banco["ispb"]}
# """)
#         break  
# else:
#     print("Banco não encontrado")

        
        
# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula04.py
# Digite o código do banco: 539

# Nome..: SANTINVEST S.A. - CFI
# Código: 539
# ISPB..: 00122327

# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula04.py
# Digite o código do banco: 55555
# Banco não encontrado




# # == Desafio ==
# opc = 9

# while True:
#     opc = int(input("""
# ====================
# Consulta Bancos
# ====================

# 1 - Listar todos

# 2 - Buscar por código

# 3 - Buscar por nome

# 4 - Sair 
                           
# Opção escolhida: """))
    
#     if opc == 1:
#         for banco in dados:
#             print(f"Banco: {banco['name']} | Código: {banco['code']} | Ispb: {banco["ispb"]}\n")
            
#     elif opc == 2:
#         cod = int(input("Digite o código do banco: "))

#         for banco in dados:
#             if banco["code"] == cod:
#                 print(f"""
#         Nome..: {banco["name"]}
#         Código: {banco["code"]}
#         ISPB..: {banco["ispb"]}
#         """)
#                 break  
#         else:
#             print("Banco não encontrado")
            
#     elif opc == 3:
#         nome = input("Digite o nome do banco: ")
        
#         for banco in dados:
#             if nome.lower() in banco["name"].lower():
#                 print(f"""
# Nome..: {banco["name"]}
# Código: {banco["code"]}
# ISPB..: {banco["ispb"]}
#                   """)
#                 break  
#         else:
#             print("Banco não encontrado")    
            
#     elif opc == 4:
#         print("Encerrando programa!")
#         break
    
# Resultado:
# \====================

# Consulta Bancos

# \====================



# 1 - Listar todos



# 2 - Buscar por código



# 3 - Buscar por nome



# 4 - Sair 

                           

# Opção escolhida: 1

# Banco: BCO DO BRASIL S.A. | Código: 1 | Ispb: 00000000



# Banco: BRB - BCO DE BRASILIA S.A. | Código: 70 | Ispb: 00000208



# Banco: Selic | Código: None | Ispb: 00038121



# Banco: Bacen | Código: None | Ispb: 00038166



# Banco: SANTINVEST S.A. - CFI | Código: 539 | Ispb: 00122327



# Banco: CCR SEARA | Código: 430 | Ispb: 00204963



# Banco: AGK CC S.A. | Código: 272 | Ispb: 00250699



# Banco: UNICRED DO BRASIL | Código: 136 | Ispb: 00315557



# Banco: SEFER INVESTIMENTOS DTVM LTDA - EM LIQUIDAÇÃO EXTRAJUDICIAL | Código: 407 | Ispb: 00329598



# Banco: CAIXA ECONOMICA FEDERAL | Código: 104 | Ispb: 00360305



# Banco: STN | Código: None | Ispb: 00394460



# Banco: FINAMAX S.A. CFI | Código: 714 | Ispb: 00411939



# \====================

# Consulta Bancos

# \====================



# 1 - Listar todos

# 2 - Buscar por código

# 3 - Buscar por nome

# 4 - Sair

# Opção escolhida: 2
# Digite o código do banco: 539

# ```
#     Nome..: SANTINVEST S.A. - CFI
#     Código: 539
#     ISPB..: 00122327
    
# ```

# \====================

# Consulta Bancos

# \====================



# 1 - Listar todos

# 2 - Buscar por código

# 3 - Buscar por nome

# 4 - Sair

# Opção escolhida: 3
# Digite o nome do banco: inter

# Nome..: BANCO INTER
# Código: 77
# ISPB..: 00416968



# \====================

# Consulta Bancos

# \====================



# 1 - Listar todos

# 2 - Buscar por código

# 3 - Buscar por nome

# 4 - Sair

# Opção escolhida: 4
# Encerrando programa!




# # == Desafio Extra ==

# Resultado: