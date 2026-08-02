from math import sqrt
import random

# # == Exercicio 01 ==
# print(math.sqrt(81))

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula08.py   
# 9.0




# # == Exercicio 02 ==
# print(sqrt(144))
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula08.py
# 12.0




# # == Exercicio 03 ==
# print(random.randint(1, 100))

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula08.py
# 65
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula08.py
# 1
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula08.py
# 36




# # == Desafio ==
# opc = 10

# while True:
#  try:
#         opc = int(input("""
# 1 - Número aleatório
# 2 - Raiz quadrada
# 3 - Sair                  
                
# Opção escolhida: """))
         
#         if opc == 1:
#             num = int(input("Digite um número: "))
#             num2 = int(input("Digite um segundo número: "))
#             print(random.randint(num, num2))
             
#         elif opc == 2:
#             num = int(input("Digite um número: "))
#             print(sqrt(num))
             
#         elif opc == 3:
#             print("Encerrando programa! ")
#             break
#  except ValueError:
#      print("Opções aceitas 1 a 3! ")
    
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula08.py

# 1 - Número aleatório
# 2 - Raiz quadrada
# 3 - Sair                  
                
# Opção escolhida: 1
# Digite um número: 5
# Digite um segundo número: 8
# 7

# 1 - Número aleatório
# 2 - Raiz quadrada
# 3 - Sair                  
                
# Opção escolhida: 2
# Digite um número: 5873
# 76.6355009117837

# 1 - Número aleatório
# 2 - Raiz quadrada
# 3 - Sair                  
                
# Opção escolhida: 3
# Encerrando programa! 



# # == Desafio Extra ==
# print(random.random())

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula08.py
# 0.338802229297268