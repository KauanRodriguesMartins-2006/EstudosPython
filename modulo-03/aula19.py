import requests
sessao = requests.Session()
sessao.headers.update({
    "Accept": "application/json"
})

Url = 'https://jsonplaceholder.typicode.com/posts'

def buscar_postsUid(userId : int):
    try:
        param = {
            "userId": userId
        }
                       
        getUser = sessao.get(Url, params= param)
        getUser.raise_for_status()
        gU = getUser.json()
        
        if gU:
            return gU      
        else:
            print("Este id de usuário não existe")
            return []
            
    except requests.exceptions.HTTPError:
        print("Houve um erro de código de status com a requisição.")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão com o servidor.")                                                                                            
    except requests.exceptions.Timeout:
        print("Requisição demorou demais.")
    except requests.exceptions.RequestException:
        print("Houve um erro na sua requisição.")
        
    return []


def buscar_postsId (PosTid: int):
    try:
        param = {
            "id": PosTid
        }
        
        getId = sessao.get(Url, params= param)
        getId.raise_for_status()
        gI = getId.json()
        
        if gI:
            return gI
        else:
            print("Nenhum post com esse Id encontrado")
            return[]
        
    except requests.exceptions.HTTPError:
        print("Houve um erro de código de status com a requisição.")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão com o servidor.")                                                                                            
    except requests.exceptions.Timeout:
        print("Requisição demorou demais.")
    except requests.exceptions.RequestException:
        print("Houve um erro na sua requisição.")
    
    return[]

def buscar_DoubleId (IDuser: int, IDpost: int):
    try:
        param = {
            "userId": IDuser,
            "id": IDpost
        }
            
        getPost = sessao.get(Url, params= param)
        getPost.raise_for_status()
        gP = getPost.json()
    
        if gP:
            return gP
        else:
            print("Nenhum post desse usuário com ess Id foi encontrado")
            return[]
        
    except requests.exceptions.HTTPError:
        print("Houve um erro de código de status com a requisição.")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão com o servidor.")                                                                                            
    except requests.exceptions.Timeout:
        print("Requisição demorou demais.")
    except requests.exceptions.RequestException:
        print("Houve um erro na sua requisição.")
        
    return[]

def post_analise1(userCheck):
    try:
        param = {
            "userId": userCheck
        }
           
        CheckPostUid = sessao.get(Url, params= param)
        CPU = CheckPostUid.json()
        
        if CPU:
            return CPU
        else:
            print("nenhum post encontrado desse usuário")
            return[]
    
    except requests.exceptions.HTTPError:
        print("Houve um erro de código de status com a requisição.")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão com o servidor.")                                                                                            
    except requests.exceptions.Timeout:
        print("Requisição demorou demais.")
    except requests.exceptions.RequestException:
        print("Houve um erro na sua requisição.")
            
    return[]
    
def post_analise2():
    try:
        postCheck = sessao.get(Url)
        pc = postCheck.json()
        
        if pc:
            return pc
        else:
            print("nenhum post encontrado")
            return[]
    except requests.exceptions.HTTPError:
            print("Houve um erro de código de status com a requisição.")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão com o servidor.")                                                                                            
    except requests.exceptions.Timeout:
        print("Requisição demorou demais.")
    except requests.exceptions.RequestException:
        print("Houve um erro na sua requisição.")
                
    return[]
    
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
        UId_select = int(input("Digite o id do usuário: "))
        user_posts = buscar_postsUid(UId_select)
        
        if user_posts:
            for i in user_posts:
                print(f"""
Id_post......: {i['id']}
Id_usuário...: {i['userId']}
Título.......: {i['title']}
Corpo........: {i['body']}                    
""")
    elif menu == 2:
        Id_select = int(input("Digite o id do post: "))
        id_posts = buscar_postsId(Id_select)
        
        print(f"""
Id_post......: {id_posts[0]['id']}
Id_usuário...: {id_posts[0]['userId']}
Título.......: {id_posts[0]['title']}
Corpo........: {id_posts[0]['body']}                    
                    """)
    elif menu == 3:
        User = int(input("Digite o id do usuário: "))
        Post = int(input("Digite o id do post: "))      
        DID = buscar_DoubleId(User, Post)
        
        if DID:
            post_unico = DID[0]
            print(f"""
Id_post......: {post_unico['id']}
Id_usuário...: {post_unico['userId']}
Título.......: {post_unico['title']}
Corpo........: {post_unico['body']}                    
""")
        
    elif menu == 4:
        while True:
            opc = int(input("""
========================
   ANALISADOR DE POSTS
========================

1 - Analisar usuário
2 - Analisar todos os posts
3 - Sair
                       
Opção escolhida: """))
            
            if opc == 1:
                user_check = int(input("Digite o id do usuário: "))
                uc = post_analise1(user_check)
                cont_post = 0
                cont_word = 0
                
                if uc:
                    for i in uc:
                        cont_post += 1
                        
                    maior_titulo = max(uc, key=lambda post: len(post["title"])) 
                    menor_titulo = min(uc, key=lambda post: len(post["title"])) 
                    
                    word = input("Digite uma palavra que os títulos possuem: ")
                    for i in uc:
                        if word.lower() in i["title"].lower():
                            cont_word += 1
                            
                    print(f"""
Quantidade_post...: {cont_post}
Maior_título......: {maior_titulo}
Menor_título......: {menor_titulo}
Quantidade_palavra: {cont_word}                      
""")      
                
                
            elif opc == 2:
                PC = post_analise2()
                
                quantidade_total = len(PC)
                
                usuarios = set(post["userId"] for post in PC)
                quantidade_usuarios = len(usuarios)
                
                post_maior_id = max(PC, key=lambda post: post["id"])
                usuario_maior_id = post_maior_id["userId"]
                
                media_caracteres = round(sum(len(post["title"]) for post in PC) / len(PC))
                
                print(f"""
Quantidade_posts_total...: {quantidade_total}
Quantidade_usuarios_posts: {quantidade_usuarios}
Usuario_post_maiorId.....: {usuario_maior_id}
Media_caracteres_titulo..: {media_caracteres}
""")
            elif opc == 3:
                print("Retornando ao menu anterior")
                break
    elif menu == 5:
        print("Encerrando programa")
        break