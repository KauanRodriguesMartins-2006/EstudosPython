# # == Exercicio 01 ==
# num = 1

# while True:
#     if num > 3:
#        break
#     print(num)

#     num += 1

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula07.py
# 1
# 2
# 3

# # == Exercicio 02 ==
# num = 0

# while num < 5:

#     num += 1

#     if num == 3:
#        continue

#     print(num)

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula07.py
# 1
# 2
# 4
# 5

# # == Exercicio 03 ==
# while True:
#     num = int(input(" Digite um número: "))
#     if num < 0:
#         print("Número ignorado")
#         continue
#     elif num > 0:
#         print(f"Você digitou o número: {num}")
#         continue
#     else:
#         break

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula07.py
#  Digite um número: 5
# Você digitou o número: 5
#  Digite um número: 7
# Você digitou o número: 7
#  Digite um número: -8
# Número ignorado
#  Digite um número: 0

# # == Desafio ==

# Opc = int(input(f"""
# ======== MENU ========    
      
#  1 - Olá
#  2 - Data
#  3 - Sair
      
# """))

# while Opc != 3:
#     Opc = int(input(f"""
# ======== MENU ========    
      
#  1 - Olá
#  2 - Data
#  3 - Sair
      
# """))

#     if Opc == 1: 
#        print("Olá :| ")
#     elif Opc == 2:
#        print("15/07/2026")
#     elif Opc == 3:
#        print("Encerrando Programa")
#        break
       
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\modulo-01> uv run aula07.py

# ======== MENU ========    
      
#  1 - Olá
#  2 - Data
#  3 - Sair
      
# 1

# ======== MENU ========    
      
#  1 - Olá
#  2 - Data
#  3 - Sair
      
# 2
# 15/07/2026

# ======== MENU ========    
      
#  1 - Olá
#  2 - Data
#  3 - Sair
      
# 2
# 15/07/2026

# ======== MENU ========    
      
#  1 - Olá
#  2 - Data
#  3 - Sair
      
# 1
# Olá :| 

# ======== MENU ========    
      
#  1 - Olá
#  2 - Data
#  3 - Sair
      
# 3
# Encerrando Programa