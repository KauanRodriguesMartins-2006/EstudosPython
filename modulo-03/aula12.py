import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
menu = 10
while True:
    menu = int(input("""
========================
        Aula 08
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        sessao = requests.Session()
        
        sessao.headers.update({
            "Accept": "application/json"
        })
        
        resposta1 = sessao.get(url)
        resposta2 = sessao.get(url)
        
        dados1 = resposta1.json()
        dados2 = resposta2.json()
        
        print(f"""
=========================
     Dados 1 & 2
=========================

Código_status01: {resposta1.status_code}
Código_status02: {resposta2.status_code}

Title01........: {dados1["title"]}
Title02........: {dados2["title"]}

Body01........: {dados1["body"]}
Body02........: {dados2["body"]}
""")
# ==================================================================        
    elif menu == 2:
        sessao = requests.Session()
                
        sessao.headers.update({
            "Accept": "application/json",
            "X-API-Key": "minha-chave-123"
        })
        
        dados = {
            "title": "Teste com Session",
            "body": "Primeiro POST utilizando uma Session",
            "userId": 11
        } 
        
        response1 = sessao.get(url)
        response2 = sessao.post(url, json= dados)
                
        data1 = response1.json()
        data2 = response2.json()
                
        print(f"""
=========================
        Data 1 & 2
=========================
        
Código_status01.......: {response1.status_code}
Código_status02.......: {response2.status_code}
        
Title01...............: {data1["title"]}
Retorno_json02........: {response2.json()}
        
Content-Type01........: {response1.headers["Content-Type"]}
Content-Type02........: {response2.headers["Content-Type"]}
        """)
        
# ==================================================================
    elif menu == 3:
        try:
            sessao = requests.Session()
            
            sessao.headers.update({
                "Accept": "application/json"
            })
            
            answer = sessao.get(url)
            answer.raise_for_status()
            content = answer.json()
            
            print(f"""
=========================
        Check 1
=========================
        
Código_status01.......: {answer.status_code}

Id01..................: {content["id"]}
Title01...............: {content["title"]}
Body01................: {content["body"]}
        
Content-Type01........: {answer.headers["Content-Type"]}

""")           
            new_title = input("Digite um novo título: ")    
            
            newT = {
                "title": new_title
            }
            p_change = sessao.patch(url, json= newT)
            p_change.raise_for_status()
            
            ch = p_change.json()
            
            print(f"""
=========================
        Check 2
=========================
        
Código_status01.......: {p_change.status_code}

Id01..................: {ch["id"]}
Title01...............: {ch["title"]}
Body01................: {ch["body"]}
        
Content-Type01........: {p_change.headers["Content-Type"]}

""") 
                
               
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")
                                                                
        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
                                                                            
        except requests.exceptions.HTTPError:
            print("Houve um erro de HTTP.")
            
# ==================================================================         
    elif menu == 4:
        section = requests.Session()
        section.headers.update({
    "Accept": "application/json"
})
        
        try:
            while True:
                        opc = (int(input("""
========================
    Gerenciador Posts
========================

1 - Consultar post
2 - Criar post
3 - Alterar título
4 - Excluir post
5 - Sair

Opção escolhida: """)))
        
                        if opc == 1:
                                id_search = int(input("Digite o id do usuario: "))
                                
                                get_url = f'https://jsonplaceholder.typicode.com/posts/{id_search}'
                                
                                search = section.get(get_url)
                                se = search.json()
                                
                                print(f"""
=========================
        Check 
                    =========================
                            
Id..................: {se["id"]}
Title...............: {se["title"]}
Body................: {se["body"]}
User_Id.............: {se["userId"]}
""") 
                        elif opc == 2:
                                post_url = 'https://jsonplaceholder.typicode.com/posts'
                                new_title1 = input("Digite um novo título: ")   
                                new_body = input("Digite um novo corpo: ")   
                                new_userId= int(input("Digite um novo id de usuario: "))  
                                
                                dc = {
                                    "title": new_title1,
                                    "body": new_body,
                                    "userId": new_userId
                                }
                                
                                mailman = section.post(post_url, json= dc)
                                mail = mailman.json()
                                
                                print(f"""
=========================
        Send
=========================
Status_code.........: {mailman.status_code}                  
Id..................: {mail["id"]}
Title...............: {mail["title"]}
Body................: {mail["body"]}
User_Id.............: {mail["userId"]}
""") 
                            
                        elif opc == 3:
                                sub1 = int(input("Digite o id do post: ")) 
                                sub2 = input("Digite o novo título: ")
                                
                                sub_url = f'https://jsonplaceholder.typicode.com/posts/{sub1}'
                                
                                sub_dc ={
                                    "title": sub2
                                }
                                
                                switch = section.patch(sub_url, json= sub_dc)
                                sw = switch.json()
                                
                                print(f"""
=========================
        Change
=========================
Status_code.........: {switch.status_code}                  
Id..................: {sw["id"]}
Title...............: {sw["title"]}
Body................: {sw["body"]}
User_Id.............: {sw["userId"]}
""") 
                    
                        elif opc == 4:  
                                del_id = int(input("Digite o Id do post a ser deletado: "))
                                del_url = f'https://jsonplaceholder.typicode.com/posts/{del_id}'
                                
                                delete = section.delete(del_url)
                                dl = delete.json()
                                print(f"""
=========================
        Delete
=========================
Status_code.........: {delete.status_code}                  
Id..................: {dl}
""") 
                            
                        elif opc == 5:
                                print("retornando ao menu anterior")
                                break   
                
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
#     (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula12.py

# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 1

# =========================
#      Dados 1 & 2
# =========================

# Código_status01: 200
# Código_status02: 200

# Title01........: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# Title02........: sunt aut facere repellat provident occaecati excepturi optio reprehenderit

# Body01........: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
# Body02........: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto


# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 2

# =========================
#         Data 1 & 2
# =========================
        
# Código_status01.......: 200
# Código_status02.......: 404
        
# Title01...............: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# Retorno_json02........: {}
        
# Content-Type01........: application/json; charset=utf-8
# Content-Type02........: application/json; charset=utf-8
        

# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 3

# =========================
#         Check 1
# =========================
        
# Código_status01.......: 200

# Id01..................: 1
# Title01...............: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# Body01................: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
        
# Content-Type01........: application/json; charset=utf-8


# Digite um novo título: novo titulo

# =========================
#         Check 2
# =========================
        
# Código_status01.......: 200

# Id01..................: 1
# Title01...............: novo titulo
# Body01................: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
        
# Content-Type01........: application/json; charset=utf-8



# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 4

# ========================
#     Gerenciador Posts
# ========================

# 1 - Consultar post
# 2 - Criar post
# 3 - Alterar título
# 4 - Excluir post
# 5 - Sair

# Opção escolhida: 1
# Digite o id do usuario: 1

# =========================
#         Check 
#                     =========================
                            
# Id..................: 1
# Title...............: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# Body................: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
# User_Id.............: 1


# ========================
#     Gerenciador Posts
# ========================

# 1 - Consultar post
# 2 - Criar post
# 3 - Alterar título
# 4 - Excluir post
# 5 - Sair

# Opção escolhida: 2 
# Digite um novo título: hhtbgrvafscd
# Digite um novo corpo: eytbstqvfbhrgtkrfmmjksbgtrfmkç v
# Digite um novo id de usuario: 8945612

# =========================
#         Send
# =========================
# Status_code.........: 201                  
# Id..................: 101
# Title...............: hhtbgrvafscd
# Body................: eytbstqvfbhrgtkrfmmjksbgtrfmkç v
# User_Id.............: 8945612


# ========================
#     Gerenciador Posts
# ========================

# 1 - Consultar post
# 2 - Criar post
# 3 - Alterar título
# 4 - Excluir post
# 5 - Sair

# Opção escolhida: 3
# Digite o id do post: 1
# Digite o novo título: novo titititulo

# =========================
#         Change
# =========================
# Status_code.........: 200                  
# Id..................: 1
# Title...............: novo titititulo
# Body................: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
# User_Id.............: 1


# ========================
#     Gerenciador Posts
# ========================

# 1 - Consultar post
# 2 - Criar post
# 3 - Alterar título
# 4 - Excluir post
# 5 - Sair

# Opção escolhida: 4
# Digite o Id do post a ser deletado: 1

# =========================
#         Delete
# =========================
# Status_code.........: 200                  
# Id..................: {}


# ========================
#     Gerenciador Posts
# ========================

# 1 - Consultar post
# 2 - Criar post
# 3 - Alterar título
# 4 - Excluir post
# 5 - Sair

# Opção escolhida: 5
# retornando ao menu anterior

# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 5
# Encerrando programa