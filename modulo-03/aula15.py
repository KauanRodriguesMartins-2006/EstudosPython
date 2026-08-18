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

1. Exercicio 1 (Quantidade de post de usuário)
2. Exercicio 2 (Procurar post por id)
3. Exercicio 3 (Procurar post por id e id de usuário)
4. Desafio (Procurar post pot título)
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        idlt = int(input("Digite o id do usuario: "))
        
        dadoUID = {
            "userId": idlt
        }
        
        getTest = sessao.get(url, params= dadoUID)
        dT = getTest.json()
        cont = 0
        if dT:
            for i in getTest:
                cont += 1
            
            print(f"""
Código_status...: {getTest.status_code}
Quantidade_posts: {cont}
                  """)
        else:
            print("Nenhum usuário com esse id foi encontrado")
                
# ==========================================================================================        
    elif menu == 2:
        post_id = int(input("Digite o id do post que deseja: "))
        
        post_search = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
        
        post_get = sessao.get(post_search)
        pG = post_get.json()
        
        if pG:
            print(f"""
Id_post...: {pG['id']}
Id_usuario: {pG["userId"]}
Título....: {pG["title"]}
Corpo.....: {pG["body"]}                 
""")
        else:
            print("Nenhum post com esse id foi encontrado") 
# ========================================================================================== 
    elif menu == 3:
        id_param = int(input("Digite o Id do post: "))
        Uid_param = int(input("Digite o Id do usuário: "))
        
        filtro = {
            "id": id_param,
            "userId": Uid_param
        }
        
        getParam = sessao.get(url, params= filtro)
        gP = getParam.json()
        
        print(f"Código status: {getParam.status_code}")
        
        if gP:
            post = gP[0]
            print(f"""
Id_post...: {post["id"]}
Id_usuario: {post["userId"]}
Título....: {post["title"]}
Corpo.....: {post["body"]}                 
            """)
        else:
            print("Nenhum post corresponde a esses paramentros")
# ==========================================================================================
    elif menu == 4:
        title_search = input("Digite o título do(s) post(s) que deseja: ")
        filter = {
            "title_like": title_search
        }
        
        titleGet = sessao.get(url, params= filter)
        tG = titleGet.json()
        cont_title = 0
        
        if tG:
            for i in tG:
                cont_title += 1
                print(f"""
Id_post...: {i["id"]}
Id_usuario: {i["userId"]}
Título....: {i["title"]}
Corpo.....: {i["body"]}                 
""")
            
            print(f"Número de posts com o título encontrados: {cont_title}")
    elif menu == 5:
        print("Encerrando programa")
        break