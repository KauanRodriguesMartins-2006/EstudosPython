import json
import os

# # == Exercicio 01 ==
# produto =  {
#     "titulo": "Coca-Cola 2L",
#     "valor": 8.00   
# }

# with open("produto.json", "w") as arquivo:
#     json.dump(produto, arquivo)


# # == Exercicio 02 ==
# with open("produto.json", "r") as arquivo:
#    conteudo = json.load(arquivo)
   
# print(conteudo)

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula06.py
# {'titulo': 'Coca-Cola 2L', 'valor': 8.0}




# # == Exercicio 03 ==
# alunos = [
#     {
#         "titulo": "Kauan",
#         "idade": 19
#     },
#     {
#         "titulo": "Artur",
#         "idade": 20
#     },
#     {
#         "titulo": "Maria",
#         "idade": 19 
#     }
# ]

# with open("alunos.json", "w") as arquivo:
#     json.dump(alunos, arquivo)
    
# with open("alunos.json", "r") as arquivo:
#     conteudo = json.load(arquivo)
    
# for item in conteudo:
#     print(f"""
# titulo: {item["titulo"]}
# Idade: {item["idade"]}        
#           """)


# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02\aula06-Arquivo_salvo_json> uv run aula06.py

# titulo: Kauan
# Idade: 19        
          
# titulo: Artur
# Idade: 20        
          
# titulo: Maria
# Idade: 19 




# # == Desafio ==

# Titulo = """
# ========================
#    Cadastro de filme         
# ========================\
# """

# Opc = 4


# while (True):
    
#     Opc = int(input(f"""
# {Titulo}
# 1- Adicione um filme
# 2- Mostrar filme
# 3- Sair
  
# """))
    
#     if Opc == 1:
#         filmes = []
        
#         if os.path.isfile("filmes.json"):
#           titulo = input("Digite o título do filme: ")
#           ano = int(input("Ano de lançamento: "))
#           diretor = input("Diretor: ")
                      
#           filme = {
#             "titulo": titulo,
#             "ano": ano,
#             "diretor": diretor    
#           }
             
#           with open("filmes.json", "r") as arquivo:
#                 conteudo = json.load(arquivo)    
          
#           conteudo.append(filme)
          
#           with open("filmes.json", "w") as arquivo:
#                 json.dump(conteudo, arquivo) 
          
            
#         else:       
#           titulo = input("Digite o título do filme: ")
#           ano = int(input("Ano de lançamento: "))
#           diretor = input("Diretor: ")
                                   
#           filme = {
#             "titulo": titulo,
#             "ano": ano,
#             "diretor": diretor    
#           }
#           filmes.append(filme)
                                   
#           with open("filmes.json", "w") as arquivo:
#              json.dump(filmes, arquivo)  
               
                 
#     elif Opc == 2:
#         with open("filmes.json", "r") as arquivo:
#             conteudo = json.load(arquivo)
    
#         for item in conteudo:
#             print(f"""
#         titulo.: {item["titulo"]}
#         Ano....: {item["ano"]}      
#         Diretor: {item["diretor"]}  
#                   """) 
        
#     elif Opc == 3:
#         print("Encerrando o programa")
#         break
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02\aula06-Arquivo_salvo_json> uv run aula06.py


# ========================
#    Cadastro de filme         
# ========================
# 1- Adicione um filme
# 2- Mostrar filme
# 3- Sair
  
# 1
# Digite o título do filme: Kung Fu Panda  
# Ano de lançamento: 2008
# Diretor: John Stevenson e Mark Osborne


# ========================
#    Cadastro de filme         
# ========================
# 1- Adicione um filme
# 2- Mostrar filme
# 3- Sair
  
# 2

#         titulo.: Kung Fu Panda  
#         Ano....: 2008      
#         Diretor: John Stevenson e Mark Osborne  
                  


# ========================
#    Cadastro de filme         
# ========================
# 1- Adicione um filme
# 2- Mostrar filme
# 3- Sair
  
# 1
# Digite o título do filme: Como Treinar o Seu Dragão
# Ano de lançamento: 2010
# Diretor: Chris Sanders e Dean DeBlois


# ========================
#    Cadastro de filme         
# ========================
# 1- Adicione um filme
# 2- Mostrar filme
# 3- Sair
  
# 2

#         titulo.: Kung Fu Panda  
#         Ano....: 2008      
#         Diretor: John Stevenson e Mark Osborne  
                  

#         titulo.: Como Treinar o Seu Dragão
#         Ano....: 2010      
#         Diretor: Chris Sanders e Dean DeBlois  
                  


# ========================
#    Cadastro de filme         
# ========================
# 1- Adicione um filme
# 2- Mostrar filme
# 3- Sair
  
# 3
# Encerrando o programa




# # == Desafio Extra ==

# Resultado: