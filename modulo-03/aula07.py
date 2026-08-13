import requests

# # == Exercicio 01 ==
# url = 'https://jsonplaceholder.typicode.com/posts'

# dados = {
#     "title": "Post 1",
#     "body": "Primeiro post teste da atividade",
#     "userId": 11
# }

# resposta = requests.post(url, json= dados)

# print(resposta.status_code)
# print(resposta.json())

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula07.py                                                                        
# 201                                                                
# {'title': 'Post 1', 'body': 'Primeiro post teste da atividade', 'userId': 11, 'id': 101}


# # == Exercicio 02 ==
# url = 'https://jsonplaceholder.typicode.com/posts'

# titulo = input("Digite o titulo do post: ")
# corpo = input("Digite o dados do post: ")
# id = int(input("Digite o ID do usuario: "))

# dados = {
#     "titulo": titulo,
#     "corpo": corpo,
#     "id": id
# }

# resposta = requests.post(url, json= dados)

# print(resposta.json())

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula07.py
# Digite o titulo do post: TESTE 02
# Digite o dados do post: Segundo teste de envio de informação
# Digite o ID do usuario: 11
# {'titulo': 'TESTE 02', 'corpo': 'Segundo teste de envio de informação', 'id': 101}


# # == Exercicio 03 ==
# try:
#     url = 'https://jsonplaceholder.typicode.com/posts'
    
#     titulo = input("Digite o titulo do post: ")
#     corpo = input("Digite o conteudo do post: ")
#     id = int(input("Digite o ID do post: "))
#     userId = int(input("Digite o ID do usuario: "))

#     dados = {
#         "titulo": titulo,
#         "corpo": corpo,
#         "id": id,
#         "userId": userId
#     }
    
#     resposta = requests.post(url, json= dados)
    
#     print(resposta.status_code)
    
    
    
#     print(f"""
# ID do post...: {dados["id"]}
# ID do usuario...: {dados["userId"]}
# título.......: {dados["titulo"]}
# conteúdo.....: {dados["corpo"]}
#           """)
    
    
# except requests.exceptions.ConnectionError:
#     print("Erro de conexão com o servidor.")

# except requests.exceptions.Timeout:
#     print("Requisição demorou demais.")
    
# except requests.exceptions.HTTPError:
#     print("Houve um erro de HTTP.")


# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula07.py
# Digite o titulo do post: TESTE 03
# Digite o conteudo do post: Terceiro teste de envio de informações
# Digite o ID do post: 3                                     
# Digite o ID do usuario: 11
# 201

# ID do post...: 3
# ID do usuario...: 11
# título.......: TESTE 03
# conteúdo.....: Terceiro teste de envio de informações


# # == Desafio ==
# userId_search = int(input("Digite o Id do usuario: "))
# url = 'https://jsonplaceholder.typicode.com/posts'

# conteudo = requests.get(url, params= {"userId": userId_search})

# dados = conteudo.json()

# for item in dados:
#     print(f"""
# Id....: {item["id"]}
# Titulo: {item["title"]}    
# """)

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula07.py
# Digite o Id do usuario: 10

# Id....: 91
# Titulo: aut amet sed    

# Id....: 92
# Titulo: ratione ex tenetur perferendis    

# Id....: 93
# Titulo: beatae soluta recusandae    

# Id....: 94
# Titulo: qui qui voluptates illo iste minima    

# Id....: 95
# Titulo: id minus libero illum nam ad officiis    

# Id....: 96
# Titulo: quaerat velit veniam amet cupiditate aut numquam ut sequi    

# Id....: 97
# Titulo: quas fugiat ut perspiciatis vero provident    

# Id....: 98
# Titulo: laboriosam dolor voluptates    

# Id....: 99
# Titulo: temporibus sit alias delectus eligendi possimus magni    

# Id....: 100
# Titulo: at nam consequatur ea labore ea harum 
