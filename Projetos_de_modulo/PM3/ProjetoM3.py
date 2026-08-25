import requests
sessao = requests.Session()
sessao.headers.update({
    "Accept": "application/json"
})


def consultar_dados_usuario(user_check: int):
    try:
        url1 = f'https://jsonplaceholder.typicode.com/users/{user_check}'
        
        user_get = sessao.get(url1)
        user_get.raise_for_status()
        ug = user_get.json()
        
        if ug:
            return ug
        else:
            print("Não existe nenhum usuário com esse Id")
            return []
        
    except requests.exceptions.HTTPError:
        print("Houve um erro de código de status com a requisição.")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão com o servidor.")                                                                                            
    except requests.exceptions.Timeout:
        print("Requisição demorou demais.")
    except requests.exceptions.RequestException:
        print("Houve um erro na sua requisição.")
        
    return[]
        
def consultar_post_user(user_posts):
    try:
        param = {
            "userId": user_posts
        }
        
        url2 = 'https://jsonplaceholder.typicode.com/posts'
        
        posts_get = sessao.get(url2, params= param)
        posts_get.raise_for_status()
        pg = posts_get.json()
        
        if pg:
            return pg
        else:
            print("Nenhum post com esse Id de usuário encontrado")
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

def consultar_post_unico(post_id):
    try:
        param = {
            "id": post_id
        }
    
        url3 = 'https://jsonplaceholder.typicode.com/posts'
    
        post_unico = sessao.get(url3, params= param)
        post_unico.raise_for_status()
        pu = post_unico.json()
    
        if pu:
            return pu
        else:
            print("Post não encontrado")
            return[]    
    except requests.exceptions.HTTPError:
                print("Houve um erro de código de status com a requisição.")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão com o servidor.")                                                                                            
    except requests.exceptions.Timeout:
        print("Requisição demorou demais.")
    except requests.exceptions.RequestException:
        print("Houve um erro na sua requisição.")   
    

def analise_usuario(user_info):
    try:
        param = {
           "userId": user_info
       }
    
        url4 = 'https://jsonplaceholder.typicode.com/posts'
    
        analise_user = sessao.get(url4, params= param)
        analise_user.raise_for_status()
        au = analise_user.json() 
        
        if au:
            return au
        else:
            print("Usuário não encontrado")
            return []
        
    except requests.exceptions.HTTPError:
        print("Houve um erro de código de status com a requisição.")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão com o servidor.")                                                                                            
    except requests.exceptions.Timeout:
        print("Requisição demorou demais.")
    except requests.exceptions.RequestException:
        print("Houve um erro na sua requisição.") 
    
    
def estatisticas_gerais():
    try:
        url5 = 'https://jsonplaceholder.typicode.com/posts'
        status_geral = sessao.get(url5)
        status_geral.raise_for_status()
        sg = status_geral.json()
        
        if sg:
            return sg
        else:
            print("Não existe nenhum post")
            return []
        
    except requests.exceptions.HTTPError:
        print("Houve um erro de código de status com a requisição.")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão com o servidor.")                                                                                            
    except requests.exceptions.Timeout:
        print("Requisição demorou demais.")
    except requests.exceptions.RequestException:
        print("Houve um erro na sua requisição.")    

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

while True:
    menu = int(input("""
=========================
    Consultor de Api      
=========================

1. Consultar dados de usuário
2. Consultar posts de um usuário
3. Consultar um post expecifico  
4. Analisar um usuário
5. Estatísticas gerais
6. Sair

Opção escolhida: """))
    
    if menu == 1:
        check_user = int(input("Digite o id do usuário: "))
        chUser = consultar_dados_usuario(check_user)
        
        if chUser:
            print(f"""
Id do usuário....: {chUser['id']}
Nome do usuário..: {chUser['name']}
Username.........: {chUser['username']}
Email do usuário.: {chUser['email']}
Cidade do usuário: {chUser['address']['city']}
""")
        else:
            print("Nenhum dado retornado")
# ================================================================
    elif menu == 2:
        user_id = int(input("Digite o id do usuário: "))
        ui = consultar_post_user(user_id)
        cont = 0
        
        for i in ui:
            cont += 1
            print(f"""
Id do post....: {i['id']}
Titulo do post: {i['title']}                  
""")
            print(f"Quantidade de posts desse usuário: {cont}")
            
# ================================================================
    elif menu == 3:
        id_post = int(input("Digite o id do post: "))
        ip = consultar_post_unico(id_post)
        
        if ip:
            print(f"""
Id do post....: {ip[0]['id']}
Id de usuário.: {ip[0]['userId']}   
Título do post: {ip[0]['title']}
Corpo do post.: {ip[0]['body']}
""")
        else:
            print("Nenhum dado retornado")
# ================================================================
    elif menu == 4:
        user_check = int(input("Digite o id do usuário: "))
        uc = analise_usuario(user_check)
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
# ================================================================
    elif menu == 5:
        PC = estatisticas_gerais()
                
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
# ================================================================
    elif menu == 6:
        print("Encerrando o programa")
        break
    
