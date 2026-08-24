import requests

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
    print("\n")
    
    if menu == 1:
       try:
            url1 = 'https://jsonplaceholder.typicode.com/posts'
            UId = int(input("\nDigite o id do usuário: "))
            
            Uparam = {
                "userId": UId
            }
            
            Uget = sessao.get(url1, params= Uparam)
            Uget.raise_for_status()
            User = Uget.json()
            
            if User:
                cont = 0
                print(f"Código_status: {Uget.status_code}")
                for i in User:
                    cont += 1
                    print(f"Titulo: {i["title"]}")
            else:
                cont = 0
                print("Nenhum post com esse id de usuário encontrado")
            
            print(f"Número de posts encontrados: {cont}")
                
       except requests.exceptions.HTTPError:
            print("Houve um erro de código de status com a requisição ")
       except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")                                                                                            
       except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
# ==========================================================================================
    elif menu == 2:
        try:
            url2 = input("\nDigite a url desejada: ")
            
            UrlGet = sessao.get(url2, timeout= 5)
            UrlGet.raise_for_status()
            
            print(f"Requisição feita com sucesso | Código_status: {UrlGet.status_code}")
            
        except requests.exceptions.HTTPError:
            print("Houve um erro de código de status com a requisição.")
            print(f"Código_status: {UrlGet.status_code}.")
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")                                                                                            
        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
        except requests.exceptions.RequestException:
            print("Houve um erro na sua requisição.")   
# ==========================================================================================
    elif menu == 3:
        try:
            url3 = 'https://jsonplaceholder.typicode.com/posts'
            
            get_uid = int(input("Digite o Id do usuário: "))    
            Guid = {
                "userId": get_uid
            }
            
            getUser = sessao.get(url3, params= Guid)
            getUser.raise_for_status()
            gu = getUser.json()
            
            if gu:
                cont = 0
                print(f"Código_status: {getUser.status_code}")
                for i in gu:
                    cont += 1
                    print(f"Titulo: {i["title"]}")
            else:
                cont = 0
                print("Nenhum post com esse id de usuário encontrado")
                        
            print(f"Número de posts encontrados: {cont}")
                    
        except requests.exceptions.HTTPError:
            print("Houve um erro de código de status com a requisição.")
            print(f"Código_status: {getUser.status_code}.")
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")                                                                                            
        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
        except requests.exceptions.RequestException:
            print("Houve um erro na sua requisição.")   
# ==========================================================================================
    elif menu == 4:
        Url4 = 'https://jsonplaceholder.typicode.com/posts'
        
        try:
            while True:
                opc = int(input("""
========================
     CONSULTOR API
========================

1 - Buscar posts por usuário
2 - Buscar post por ID
3 - Sair
            
Opção escolhida: """))
                print("\n")
            
                if opc == 1:
                    user_search = int(input("Digite o Id do usuário: "))
                    
                    paUser = {
                        "userId": user_search
                    }
                    
                    Guser = sessao.get(Url4, params= paUser)
                    Guser.raise_for_status()
                    Guser_json = Guser.json()
                    
                    if Guser_json:
                        cont = 0
                        print(f"Código_status: {Guser.status_code}")
                        for i in Guser_json:
                            cont += 1
                            print(f"Titulo: {i["title"]}")
                    else:
                        cont = 0
                        print("Nenhum post com esse id de usuário encontrado")
                                            
                    print(f"Número de posts encontrados: {cont}")
                
                elif opc == 2:
                    post_search = int(input("Digite o id do post: "))
                    
                    paPost = {
                        "id": post_search
                    }
                    
                    Gpost = sessao.get(Url4, params= paPost)
                    Gpost_json = Gpost.json()
                    
                    if Gpost_json:
                        print(f"""
Código_status...: {Gpost.status_code}
Id_post.........: {Gpost_json[0]["id"]}
Id_usuário......: {Gpost_json[0]["userId"]}
Título..........: {Gpost_json[0]["title"]}
Corpo...........: {Gpost_json[0]["body"]}
""")
                    else:
                        print("Nenhum post com esse id encontrado")
                        
                elif opc == 3:
                    print("Retornando ao menu anterior")
                    break
                    
                    
        except requests.exceptions.HTTPError:
            print("Houve um erro de código de status com a requisição.")
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")                                                                                            
        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
        except requests.exceptions.RequestException:
            print("Houve um erro na sua requisição.")  
# ==========================================================================================
    elif menu == 5:
        print("Encerrando programa")
        break