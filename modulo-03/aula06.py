# import requests

# # == Exercicio 01 ==
# url = "https://jsonplaceholder.typicode.com/posts"

# parametros = {
#     "userId" : 1
# }

# conteudo = requests.get(url, parametros)

# resposta = conteudo.json()

# for item in resposta:
#     print(f"""
# Id....: {item["userId"]}
# Titulo: {item["title"]}
# """)

# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula06.py

# Id....: 1
# Titulo: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
                   
# Id....: 1
# Titulo: qui est esse
                   
# Id....: 1
# Titulo: ea molestias quasi exercitationem repellat qui ipsa sit aut
                    
# Id....: 1
# Titulo: eum et est occaecati
                   
# Id....: 1
# Titulo: nesciunt quas odio

# Id....: 1
# Titulo: dolorem eum magni eos aperiam quia
                  
# Id....: 1
# Titulo: magnam facilis autem

# Id....: 1
# Titulo: dolorem dolore est ipsam

# Id....: 1
# Titulo: nesciunt iure omnis dolorem tempora et accusantium

# Id....: 1
# Titulo: optio molestias id quia eum


# # == Exercicio 02 ==
# id_select = int(input("Digite o Id do usuario: "))

# parametros = {
#     "userId" : id_select
# }

# conteudo = requests.get(url, parametros)

# resposta = conteudo.json()

# for item in resposta:
#     print(f"""
# Id....: {item["userId"]}
# Titulo: {item["title"]}""")

# # Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula06.py
# Digite o Id do usuario: 5

# Id....: 5
# Titulo: non est facere

# Id....: 5
# Titulo: commodi ullam sint et excepturi error explicabo praesentium voluptas

# Id....: 5
# Titulo: eligendi iste nostrum consequuntur adipisci praesentium sit beatae perferendis
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula06.py
# Digite o Id do usuario: 7

# Id....: 7
# Titulo: voluptatem doloribus consectetur est ut ducimus

# Id....: 7
# Titulo: beatae enim quia vel

# Id....: 7
# Titulo: voluptas blanditiis repellendus animi ducimus error sapiente et suscipit


# # == Exercicio 03 ==
# try:
#     id_select = int(input("Digite o Id do usuario: "))

#     parametros = {
#     "userId" : id_select
#     }

#     conteudo = requests.get(url, parametros)
#     conteudo.raise_for_status()
#     resposta = conteudo.json()

#     for item in resposta:
#         print(f"""
# Id....: {item["userId"]}
# Titulo: {item["title"]}
# """)
        
# except requests.exceptions.ConnectionError:
#     print("Erro de conexão com o servidor.")

# except requests.exceptions.Timeout:
#     print("Requisição demorou demais.")
    
# except requests.exceptions.HTTPError:
#     print("Houve um erro de HTTP.")
    
# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula06.py
# Digite o Id do usuario: 3

# Id....: 3
# Titulo: asperiores ea ipsam voluptatibus modi minima quia sint

# Id....: 3
# Titulo: dolor sint quo a velit explicabo quia nam

# Id....: 3
# Titulo: maxime id vitae nihil numquam


# # == Desafio ==
# opc = 10

# url = "https://jsonplaceholder.typicode.com/users"
# conteudo = requests.get(url)

# resposta = conteudo.json()
# while True:
#     menu = int(input("""
# ========================
#      Consulta Usuário
# ========================

# 1 - Listar usuários
# 2 - Buscar usuário
# 3 - Sair
                                    
# Opção escolhida: """))
    
#     if menu == 1:
#         for item in resposta:
#             print(f"""
# ID...: {item["id"]}
# Nome.: {item["name"]}
# Email: {item["email"]}          
# """)
    
#     elif menu == 2:
#         id_select = int(input("Digite o Id do usuario: "))

#         parametros = {
#             "id" : id_select
#         }

#         conteudo = requests.get(url, parametros)

#         resposta = conteudo.json()
        
#         for item in resposta:
#             print(f"""
# ID...: {item["id"]}
# Nome.: {item["name"]}
# Email: {item["email"]}          
# """)
            
#     elif menu == 3:
#         print("Encerrando programa")
#         break
    
    
# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula06.py

# ========================
#      Consulta Usuário
# ========================

# 1 - Listar usuários
# 2 - Buscar usuário
# 3 - Sair
                                    
# Opção escolhida: 1

# ID...: 1
# Nome.: Leanne Graham
# Email: Sincere@april.biz          

# ID...: 2
# Nome.: Ervin Howell
# Email: Shanna@melissa.tv          

# ID...: 3
# Nome.: Clementine Bauch
# Email: Nathan@yesenia.net          

# ID...: 4
# Nome.: Patricia Lebsack
# Email: Julianne.OConner@kory.org          

# ID...: 5
# Nome.: Chelsey Dietrich
# Email: Lucio_Hettinger@annie.ca          

# ID...: 6
# Nome.: Mrs. Dennis Schulist
# Email: Karley_Dach@jasper.info          

# ID...: 7
# Nome.: Kurtis Weissnat
# Email: Telly.Hoeger@billy.biz          

# ID...: 8
# Nome.: Nicholas Runolfsdottir V
# Email: Sherwood@rosamond.me          

# ID...: 9
# Nome.: Glenna Reichert
# Email: Chaim_McDermott@dana.io          

# ID...: 10
# Nome.: Clementina DuBuque
# Email: Rey.Padberg@karina.biz          

# ========================
#      Consulta Usuário
# ========================

# 1 - Listar usuários
# 2 - Buscar usuário
# 3 - Sair
                                    
# Opção escolhida: 2
# Digite o Id do usuario: 6

# ID...: 6
# Nome.: Mrs. Dennis Schulist
# Email: Karley_Dach@jasper.info          

# ========================
#      Consulta Usuário
# ========================

# 1 - Listar usuários
# 2 - Buscar usuário
# 3 - Sair
                                    
# Opção escolhida: 3
# Encerrando programa

# # == Desafio Extra ==

# Resultado: