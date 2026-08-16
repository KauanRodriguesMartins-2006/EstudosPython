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
        dados = {
            "title": "Título atualizado utilizando o Patch"
        }
        
        change = requests.patch(url, json= dados)
        ch = change.json()
        print(f"""
status_code..: {change.status_code} 
resposta_json: {change.json()}
titulo.......: {ch["title"]}
    """)
# ======================================================================        
    elif menu == 2:
        header = {
    "Accept": "application/json"
        }
        
        dados = {
            "body": "Conteúdo do body atualizado utilizando o Patch"
        }
        
        change = requests.patch(url, json= dados, headers= header)
    
        ch = change.json()
        print(f"""
status_code..: {change.status_code} 
resposta_json: {change.json()}
titulo.......: {ch["title"]}
corpo........: {ch["body"]}
tipo_conteudo: {change.headers["Content-Type"]}
    """)
# ======================================================================       
    elif menu == 3:
        try:
            header = {
                "Accept": "application/json"
            }
            
            opc = int(input("""
========================
   Atualizar Post
========================

1 - Alterar título
2 - Alterar corpo                        
                                                  
Opção escolhida: """))
            
            if opc == 1:
                new_title = input("Digite um novo título: ")
                
                dados = {
                            "title": new_title
                        }
                        
                change = requests.patch(url, json= dados, headers= header)
                change.raise_for_status()
                
                ch = change.json()
                print(f"""
status_code..: {change.status_code} 
resposta_json: {change.json()}
titulo.......: {ch["title"]}
tipo_conteudo: {change.headers["Content-Type"]}
             """)
                
            elif opc == 2:
                new_body = input("Digite um novo corpo: ")
                
                dados = {
                    "body": new_body
                }
                        
                change = requests.patch(url, json= dados, headers= header)
                change.raise_for_status()
                
                ch = change.json()
                print(f"""
status_code..: {change.status_code} 
resposta_json: {change.json()}
corpo........: {ch["body"]}
tipo_conteudo: {change.headers["Content-Type"]}
            """)
                                                      
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")
                                        
        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
                                                    
        except requests.exceptions.HTTPError:
            print("Houve um erro de HTTP.")
# ======================================================================
    elif menu == 4:
        while True:
            try:
                header = {
                    "Accept": "application/json"
                }
                            
                opc = int(input("""
        ========================
        Atualizar Post
        ========================
                
        1 - Alterar título
        2 - Alterar corpo    
        3 - Alterar id de usuario
        4 - sair                    
                                                                
        Opção escolhida: """))
                            
                if opc == 1:
                    new_title = input("Digite um novo título: ")
                                
                    dados = {
                        "title": new_title
                            }
                                        
                    change = requests.patch(url, json= dados, headers= header)
                    change.raise_for_status()
                        
                    ch = change.json()
                    print(f"""
status_code..: {change.status_code} 
resposta_json: {change.json()}
titulo.......: {ch["title"]}
tipo_conteudo: {change.headers["Content-Type"]}
                            """)
                                
                elif opc == 2:
                    new_body = input("Digite um novo corpo: ")
                                
                    dados = {
                        "body": new_body
                    }
                                        
                    change = requests.patch(url, json= dados, headers= header)
                    change.raise_for_status()
                        
                    ch = change.json()
                    print(f"""
status_code..: {change.status_code} 
resposta_json: {change.json()}
corpo........: {ch["body"]}
tipo_conteudo: {change.headers["Content-Type"]}
                        """)
                        
                elif opc == 3:
                    new_user = input("Digite um novo id de usuario: ")
                                
                    dados = {
                        "userId": new_user
                    }
                                        
                    change = requests.patch(url, json= dados, headers= header)
                    change.raise_for_status()
                        
                    ch = change.json()
                    print(f"""
status_code..: {change.status_code} 
resposta_json: {change.json()}
Id de usuario........: {ch["userId"]}
tipo_conteudo: {change.headers["Content-Type"]}
                        """)
                
                elif opc == 4:
                    print("Retornando ao menu anterior")
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