import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
menu = 10
while True:
    menu = int(input("""
========================
        Aula 10
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        header = {
            "Accept": "application/json"
        }
        
        conteudo = requests.get(url, headers= header)
        print(f"""
Status code: {conteudo.status_code}
Conteudo do json: {conteudo.json()}              
Content-Type: {conteudo.headers["Content-Type"]}              
""")
        
    elif menu == 2:
        header = {
            "X-API-Key": "minha-chave-123"
        }
        
        informacao = requests.get(url, headers= header)
        print(f"""
Status code: {informacao.status_code}
Conteudo do json: {informacao.json()}              
Content-Type: {informacao.headers["Content-Type"]}              
""")
        
    elif menu == 3:
        try:
            header = {
                "Accept": "application/json"
            }    
           
            valor = requests.get(url, headers= header)
            valor.raise_for_status()
            vault = valor.json()
            
            print(f"""
Status code...: {valor.status_code}
Id do post....: {vault["id"]}
Título do post: {vault["title"]}
Corpo do post.: {vault["body"]}
Id do usuário.: {vault["userId"]}
Content-Type..: {valor.headers["Content-Type"]}              
""")
                                      
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")
                        
        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
                                    
        except requests.exceptions.HTTPError:
            print("Houve um erro de HTTP.")
    elif menu == 4:
        try:
            key = input("""
========================
    Acesso à API
========================

Digite sua API Key: """)
            
            header = {
                "X-API-Key": key
            }    
                   
            server = requests.get(url, headers= header)
            server.raise_for_status()
            data = server.json()
                    
            print(f"""
Status code...: {server.status_code}
Título do post: {data["title"]}
Corpo do post.: {data["body"]}
Content-Type..: {server.headers["Content-Type"]}              
""")
                                              
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")
                                
        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
                                            
        except requests.exceptions.HTTPError:
            print("Houve um erro de HTTP.")
            
            
    elif menu == 5:
        print("Encerrando programa")
        break
    
# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula10.py

# ========================
#         Aula 10
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 1

# Status code: 200
# Conteudo do json: {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}              
# Content-Type: application/json; charset=utf-8              


# ========================
#         Aula 10
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 2

# Status code: 200
# Conteudo do json: {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}              
# Content-Type: application/json; charset=utf-8              


# ========================
#         Aula 10
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 3

# Status code...: 200
# Id do post....: 1
# Título do post: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# Corpo do post.: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
# Id do usuário.: 1
# Content-Type..: application/json; charset=utf-8              


# ========================
#         Aula 10
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 4

# ========================
#     Acesso à API
# ========================

# Digite sua API Key: 89456123

# Status code...: 200
# Título do post: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# Corpo do post.: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
# Content-Type..: application/json; charset=utf-8              


# ========================
#         Aula 10
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 4

# ========================
#     Acesso à API
# ========================

# Digite sua API Key: 798465123

# Status code...: 200
# Título do post: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# Corpo do post.: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
# Content-Type..: application/json; charset=utf-8              
