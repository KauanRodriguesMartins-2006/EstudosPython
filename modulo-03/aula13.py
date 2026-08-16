import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
sessao = requests.Session()
sessao.headers.update({
    "Accept": "application/json"
})
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
        reGet = sessao.get(url)
        
        if reGet.ok:
            rg = reGet.json()
            print(f"""
Código_status: {reGet.status_code}
Id...........: {rg["id"]}
Title........: {rg["title"]}    
""")
        else:
            print(f"""
Código_status: {reGet.status_code}
Houve um erro e a requisição falhou   
""")
# ==========================================================================================
    elif menu == 2:
        try:
            errorUrl = 'https://jsonplaceholder.typicode.com/posts/9999'
            errorGet = sessao.get(errorUrl)
            errorGet.raise_for_status()
            
            print("Requisição funcionou ??")
            
        except requests.exceptions.HTTPError:
            print(f"""
Código_status: {errorGet.status_code}
Houve um erro de código de status com a requisição 
""")
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")
                                                                        
        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
# ==========================================================================================
    elif menu == 3:
        try:
            id_test = int(input("Digite o id do post: "))
            dynamic_url = f'https://jsonplaceholder.typicode.com/posts/{id_test}'
            
            testGet = sessao.get(dynamic_url)
            testGet.raise_for_status()
            tg = testGet.json()
            
            print(f"""
Código_status: {testGet.status_code}
Id...........: {tg["id"]}
Title........: {tg["title"]}   
Body.........: {tg["body"]} 
""")
            
        except requests.exceptions.HTTPError:
            print(f"""
Código_status: {testGet.status_code}
Houve um erro de código de status com a requisição 
        """)
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")
                                                                                
        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
# ==========================================================================================
    elif menu == 4:
        while True:
            choice = int(input("""
    ========================
        Gerenciador Posts
    ========================

    1 - Consultar post
    2 - Criar post
    3 - Alterar título
    4 - Excluir post
    5 - Sair                        
                            
    Opção escolhida: """))
            
            if choice == 1:
                try:
                    id_check = int(input("Digite o id do post: "))
                    dynamic_url = f'https://jsonplaceholder.typicode.com/posts/{id_check}'
                            
                    choiceGet = sessao.get(dynamic_url)
                    choiceGet.raise_for_status()
                    cg = choiceGet.json()
                            
                    print(f"""
Código_status: {choiceGet.status_code}
Id...........: {cg["id"]}
Title........: {cg["title"]}   
Body.........: {cg["body"]} 
    """)                       
                except requests.exceptions.HTTPError:
                    print(f"""
    Código_status: {choiceGet.status_code}
    Houve um erro de código de status com a requisição 
    """)
                except requests.exceptions.ConnectionError:
                    print("Erro de conexão com o servidor.")
                                                                                                
                except requests.exceptions.Timeout:
                    print("Requisição demorou demais.")
                    
            elif choice == 2:
                post_url = 'https://jsonplaceholder.typicode.com/posts'
                
                title_post = input("Digite o novo título: ")
                body_post = input("Digite o novo corpo: ")
                userId_post = int(input("Digite o novo id de usuario: "))
                
                dcPost = {
                    "title": title_post,
                    "body": body_post,
                    "userId": userId_post
                }
                
                mailman_post = sessao.post(post_url, json= dcPost)
                mp = mailman_post.json()
                
                print(f"""
Código_status: {mailman_post.status_code}
userId...........: {mp["userId"]}
Title............: {mp["title"]}   
Body.............: {mp["body"]} 
""")
         
            elif choice == 3:
                try:
                    id_change = int(input("Insira o Id do post que você quer mudar o título: ")) 
                    title_change = input("Digite o novo título: ") 
                    change_url = f'https://jsonplaceholder.typicode.com/posts/{id_change}'
                    
                    dcPatch = {
                        "title": title_change
                    }
                    
                    change_patch = sessao.patch(change_url, json= dcPatch)
                    change_patch.raise_for_status()
                    cpatch = change_patch.json()
                    
                    print(f"""
New_Title: {cpatch["title"]}                     
""")
                except requests.exceptions.HTTPError:
                     print(f"""
Código_status: {choiceGet.status_code}
Houve um erro de código de status com a requisição 
""")        
                     
            elif choice == 4:
                del_id = int(input("Digite o Id do post a ser deletado: "))
                del_url = f'https://jsonplaceholder.typicode.com/posts/{del_id}'
                                                
                delete = sessao.delete(del_url)
                dl = delete.json()
                print(f"""
=========================
        Delete
=========================
Status_code.........: {delete.status_code}                  
Id..................: {dl}
""")          
            elif choice == 5:
                print("Retornando ao menu anterior")
                break
    # ==========================================================================================

    elif menu == 5:
        print("Encerrando programa")
        break