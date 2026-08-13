import requests
menu = 10
url = 'https://jsonplaceholder.typicode.com/posts'

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
        
        dados = {
            "title": "TESTE 04",
            "body": "Quarto teste de envio de informações",
            "userId": 11
        }
        
        envio = requests.post(url, json= dados)
        
        print(envio.text)
        print(envio.json())
# ================================================================
    elif menu == 2:

        dados = {
            "title": "TESTE 05",
            "body": "Quinto teste de envio de informações",
            "userId": 11
        }
        
        header = {
            "Content-Type": "application/json"
        }
        
        envio = requests.post(url, json= dados, headers= header)
        
        print(envio.status_code)
        
        conteudo = envio.json()
        print(conteudo)
        
        print(envio.headers["Content-Type"])
# ================================================================       
    elif menu == 3:
        try:
            
            titulo = input("Digite o titulo do post: ")
            corpo = input("Digite o conteudo do post: ")
            userId = input("Digite o id do usuario: 0", "\n")
            
            dados = {
                'title': titulo,
                'body': corpo,
                'userId': userId
            }
            header = {
                "Content-Type": "application/json"
            }
            
            envio = requests.post(url, json= dados, headers= header)
            envio.raise_for_status()
            print(envio.status_code)
            conteudo = envio.json()
            
            print(conteudo['id'])
            print(conteudo['title'])
            print(conteudo['body'])
            print(conteudo['userId'])
            
            
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")

        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
            
        except requests.exceptions.HTTPError:
            print("Houve um erro de HTTP.")
            
    elif menu == 4:
        opc = 't'
        while True:
            keep_going = input("Deseja fazer um post ? (s/n)").lower()
            
            if keep_going == 's':
                titulo = input("Digite o titulo do post: ")
                corpo = input("Digite o conteudo do post: ")
                userId = input("Digite o id do usuario: \n")
                            
                dados = {
'title': titulo,
'body': corpo,
'userId': userId
                 }
                header = {
"Content-Type": "application/json"
                }
                            
                envio = requests.post(url, json= dados, headers= header)
                envio.raise_for_status()
                print(envio.status_code)
                conteudo = envio.json()
                            
                print(conteudo['id'])
            elif keep_going == 'n':
                break
            
    elif menu == 5:
        print("Encerrando programa")
        break
    
# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula08.py

# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio    
# 5. Sair                                
# Opção escolhida: 1


# {
#   "title": "TESTE 04",
#   "body": "Quarto teste de envio de informações",
#   "userId": 11,
#   "id": 101
# }
# {'title': 'TESTE 04', 'body': 'Quarto teste de envio de informações', 'userId': 11, 'id': 101}

# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio    
# 5. Sair                                
# Opção escolhida: 2


# 201
# {'title': 'TESTE 05', 'body': 'Quinto teste de envio de informações', 'userId': 11, 'id': 101}
# application/json; charset=utf-8

# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio    
# 5. Sair                                
# Opção escolhida: 3


# Digite o titulo do post: TESTE 08
# Digite o conteudo do post: Oitavo teste de envio de informações
# Digite o id do usuario: 
# 11
# 201
# 101
# TESTE 08
# Oitavo teste de envio de informações
# 11

# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio    
# 5. Sair                                
# Opção escolhida: 4


# Deseja fazer um post ? (s/n)s
# Digite o titulo do post: TESTE 09
# Digite o conteudo do post: Nono teste de envio de informações  
# Digite o id do usuario: 
# 11
# 201
# 101
# Deseja fazer um post ? (s/n)s
# Digite o titulo do post: TESTE 10
# Digite o conteudo do post: Decimo teste de envio de informações
# Digite o id do usuario: 
# 11      
# 201
# 101
# Deseja fazer um post ? (s/n)n

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