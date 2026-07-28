import os.path

# # == Exercicio 01 ==
# arquivo = open("nomes.txt","w")

# arquivo.write("Kauan, ")
# arquivo.write("Daniel, ")
# arquivo.write("Sarah, ")
# arquivo.write("Gabriel")

# Resultado:





# # == Exercicio 02 ==
# with open("nomes.txt", "r") as arquivo:
#     conteudo = arquivo.read()

# print(conteudo)

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula04.py
# Kauan, Daniel, Sarah, Gabriel




# # == Exercicio 03 ==
# arquivo = open("nomes.txt", "a")
# arquivo.write(", Lima")

# with open("nomes.txt", "r") as arquivo:
#     conteudo = arquivo.read()
    
# print(conteudo)
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula04.py
# Kauan, Daniel, Sarah, Gabriel, Lima




# # == Desafio ==

# Titulo = """
# ========================
#    Cadastro de frases         
# ========================\
# """

# Opc = 4


# while (True):
    
#     Opc = int(input(f"""
# {Titulo}
# 1- Adicione um frase
# 2- Mostrar frases
# 3- Sair
  
# """))
    
#     if Opc == 1:
#         frase = input("Digite uma frase: ")
        
#         if os.path.isfile("frases.txt"):
#             arquivo = open("frases.txt", "a")
#             arquivo.write("\n")
#             arquivo.write(frase)
#         else:
#             arquivo = open("frases.txt", "w")
#             arquivo.write("\n")
#             arquivo.write(frase)     
                 
#     elif Opc == 2:
#         with open("frases.txt", "r") as arquivo:
#             conteudo = arquivo.read()
        
#         print(conteudo)
        
#     elif Opc == 3:
#         print("Encerrando o programa")
#         break
    

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula04.py


# ========================
#    Cadastro de frases         
# ========================
# 1- Adicione um frase
# 2- Mostrar frases
# 3- Sair
  
# 1
# Digite uma frase: - Teste se esta funcionando


# ========================
#    Cadastro de frases         
# ========================
# 1- Adicione um frase
# 2- Mostrar frases
# 3- Sair
  
# 2

# - Teste se esta funcionando


# ========================
#    Cadastro de frases         
# ========================
# 1- Adicione um frase
# 2- Mostrar frases
# 3- Sair
  
# 1
# Digite uma frase: - Esta funcionando os simbolos(-) sou eu que estou colocando não o programa 


# ========================
#    Cadastro de frases         
# ========================
# 1- Adicione um frase
# 2- Mostrar frases
# 3- Sair
  
# 2

# - Teste se esta funcionando
# - Esta funcionando os simbolos(-) sou eu que estou colocando não o programa 


# ========================
#    Cadastro de frases         
# ========================
# 1- Adicione um frase
# 2- Mostrar frases
# 3- Sair
  
# 3
# Encerrando o programa




# # == Desafio Extra ==

# Resultado: