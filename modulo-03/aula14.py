import requests

url = 'https://jsonplaceholder.typicode.com/posts'
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
        contador = 0
        param = {
            'userId': 1
        }
        
        userGet = sessao.get(url, params= param)
        ug = userGet.json()
        print(f"""
Código_status: {userGet.status_code}
Resultado_url: {userGet.url}     
""")
        for item in ug:
            contador += 1
            print(f"""
Id_post...: {item["id"]}
Title.....: {item["title"]}
Id_usuario: {item["userId"]}
""")
        
        print(f"O número de posts encontrados foram: {contador}")
            
# ==========================================================================================        
    elif menu == 2:
        params = {
                    'userId': 2,
                    'id': 11
                }
        
        idGet = sessao.get(url, params= params)
        ig = idGet.json()
        
        print(f"""
Código_status: {idGet.status_code}
Resultado_url: {idGet.url}
Id_post......: {ig[0]['id']}
Id_usuario...: {ig[0]['userId']}
Titulo.......: {ig[0]['title']}
Corpo........: {ig[0]['body']}  
""")
# ==========================================================================================        
    elif menu == 3:
        contador1 = 0
        id_search = int(input("Digite o id do usuario que deseja verificar os posts: "))
        
        param_search = {
            "userId": id_search
        }
        
        search_get = sessao.get(url, params= param_search)
        sg = search_get.json()
        
        print(f"""
Código_status: {search_get.status_code}
Resultado_url: {search_get.url}     
""")
        for item in sg:
            contador1 += 1
            print(f"""
Id_post...: {item["id"]}
Title.....: {item["title"]}
Id_usuario: {item["userId"]}
""")
        
        print(f"O número de posts encontrados foram: {contador1}")
# ==========================================================================================
    elif menu == 4:
        try:
            opc = 9
            while True:
                opc = int(input("""
    ========================
    Gerenciador Posts
    ========================

    1 - Consultar posts por usuário
    2 - Consultar post específico
    3 - Consultar posts com dois filtros
    4 - Sair

    Opção escolhida: """))
                
                if opc == 1:
                    userId_search = int(input("Digite o ID do usuário: "))
                    user_param = {
                        "userId": userId_search
                    }
                    
                    user_check = sessao.get(url , params= user_param)
                    uc = user_check.json()
                    
                    cont = 0
                    
                    for i in uc:
                        cont += 1
                        print(f"""
    Código_status: {user_check.status_code}
    Resultado_url: {user_check.url}
    Id_usuario...: {i['userId']}
    Título.......: {i['title']}    
    """)
                    print(f"O número de posts encontrados foram: {cont}")
                    
                elif opc == 2:
                    id_check = int(input("Digite o id do post: "))
                    
                    url_search = f'https://jsonplaceholder.typicode.com/posts/{id_check}'
                    
                    get_check = sessao.get(url_search)
                    gc = get_check.json()
                    
                    print(f"""
    Código_status: {get_check.status_code}
    Id_post......: {gc["id"]}
    Id_usuario...: {gc['userId']}
    Título.......: {gc['title']}    
    Corpo........: {gc['body']}    
    """)
                
                elif opc == 3:
                    UId = int(input("Digite o id do usuários: "))
                    PId = int(input("Digite o id do post: "))
                    
                    params = {
                        'userId': UId,
                        'id': PId
                            }
                            
                    UPId = sessao.get(url, params= params)
                    UPi = UPId.json()
                            
                    print(f"""
    Código_status: {UPId.status_code}
    Resultado_url: {UPId.url}
    Id_post......: {UPi[0]['id']}
    Id_usuario...: {UPi[0]['userId']}
    Titulo.......: {UPi[0]['title']}
    Corpo........: {UPi[0]['body']}  
    """)   
                elif opc == 4:
                    print("Retornando ao menu anterior")
                    break
                     
        except requests.exceptions.HTTPError:
            print("Houve um erro de código de status com a requisição ")
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")
                                                                                                        
        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
    elif menu == 5:
        print("Encerrando programa")
        break