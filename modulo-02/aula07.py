# # == Exercicio 01 ==
# try:
#     number = int(input("put a number here: "))
# except:
#     print("Oi dickehead i told ya to say a number and not a text you wanka")
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula07.py
# put a number here: 45
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula07.py
# put a number here: fsd
# Oi dickehead i told ya to say a number and not a text you wanka




# # == Exercicio 02 ==
# try:
#     number1 = int(input("put the first number here: "))
#     number2 = int(input("put the second number here: "))
    
#     result = number1 + number2
    
#     print(result)
# except:
#     print("Oi dickehead i told ya to put two numbers and not a text you wanka")
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula07.py
# put the first number here: 5
# put the second number here: a
# Oi dickehead i told ya to put two numbers and not a text you wanka
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula07.py
# put the first number here: 5
# put the second number here: 8
# 13




# # == Exercicio 03 ==
# try:
#     number = int(input("put a number here: "))
# except:
#     print("Número invalido")
# else:
#     print("Número valido")
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula07.py
# put a number here: as
# Número invalido
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula07.py
# put a number here: 5
# Número valido




# # == Desafio ==
# titulo = print ("""
# ===================
#     Calculadora       
# ===================                
#                 """)

# Opc = 10

# while True:
#     Opc = int(input(f"""
# {titulo}       
                    
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair         
# """))
    
#     if Opc == 1:
#         try:
#             num1 = int(input("Digite o primeiro número: "))
#             num2 = int(input("Digite o segundo número: "))
            
#             soma = num1 + num2
            
#             print(soma)
#         except ValueError:
#             print("Digite um número não um texto !!!")
#     elif Opc == 2:
#          try:
#             num1 = int(input("Digite o primeiro número: "))
#             num2 = int(input("Digite o segundo número: "))
                     
#             subtracao = num1 - num2
                     
#             print(subtracao)
#          except ValueError:
#             print("Digite um número não um texto !!!")
#     elif Opc == 3:
#         try:
#             num1 = int(input("Digite o primeiro número: "))
#             num2 = int(input("Digite o segundo número: "))
                    
#             multiplicacao = num1 * num2
                    
#             print(multiplicacao)
#         except ValueError:
#             print("Digite um número não um texto !!!")
#     elif Opc == 4:
#         try:
#             num1 = int(input("Digite o primeiro número: "))
#             num2 = int(input("Digite o segundo número: "))
                    
#             divisao = num1 / num2
                    
#             print(divisao)
#         except ValueError:
#             print("Digite um número não um texto !!!")
#         except ZeroDivisionError:
#             print("Não se pode dividir por 0")
#     elif Opc == 5:
#         print("Encerrando o programa")
#         break    
        
        
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula07.py

# ===================
#     Calculadora       
# ===================                
                

# None       
                    
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair            
#                     1
# Digite o primeiro número: 5
# Digite o segundo número: 8
# 13

# None       
                    
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair            
#                     2
# Digite o primeiro número: 5
# Digite o segundo número: 2
# 3

# None       
                    
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair            
#                     3
# Digite o primeiro número: 5
# Digite o segundo número: 5
# 25

# None       
                    
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair            
#                     4
# Digite o primeiro número: 4
# Digite o segundo número: 0
# Não se pode dividir por 0

# None       
                    
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair            
#                     4
# Digite o primeiro número: das
# Digite um número não um texto !!!

# None       
                    
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair            
#                     3
# Digite o primeiro número: csadc
# Digite um número não um texto !!!

# None       
                    
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair            
#                     2
# Digite o primeiro número: csd
# Digite um número não um texto !!!

# None       
                    
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair            
#                     1
# Digite o primeiro número: cdcs
# Digite um número não um texto !!!

# None       
                    
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair   




# # == Desafio Extra ==

# Resultado: