import requests
menu = 10
url = 'https://jsonplaceholder.typicode.com/posts/1'
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
        
        conteudo = requests.get(url)
        
        if conteudo.status_code == 200:
            Mailman = conteudo.json()
        
            print("\n--- Dados encontrados com Sucesso ---")
            print(f"ID do Post: {Mailman['id']}")
            print(f"Título: {Mailman['title']}")
            print(f"Corpo: {Mailman['body']}")
            print(f"ID do Usuário: {Mailman['userId']}")
        else:
            print("Erro ao atualizar: Verifique se a URL está correta!")
                
    elif menu == 2:
      
        mail = {
            "title": "TEST 11",
            "body": "11th test of sending information",
            "userId": 1
        }
        
        content = requests.put(url, json= mail)
        print(content.status_code)
        
        if content.status_code == 200:
            Mailman = content.json()

            print("\n--- Dados Atualizados com Sucesso ---")
            print(f"ID do Post: {Mailman['id']}")
            print(f"Título: {Mailman['title']}")
            print(f"Corpo: {Mailman['body']}")
            print(f"ID do Usuário: {Mailman['userId']}")
        else:
            print("Erro ao atualizar: Verifique se a URL está correta!")
        
          
    elif menu == 3:
        try:
            erase = requests.delete(url)
            print(erase.status_code)
            print(erase.text)
            
            erase.raise_for_status()
            
            
        except requests.exceptions.ConnectionError:
            print("Erro de conexão com o servidor.")

        except requests.exceptions.Timeout:
            print("Requisição demorou demais.")
            
        except requests.exceptions.HTTPError:
            print("Houve um erro de HTTP.")
    elif menu == 4:
        opc = 9
        
        while True:
            opc = int(input("""
========================
    Gerenciador Posts
========================

1 - Consultar post
2 - Atualizar post
3 - Excluir post
4 - Sair
Opção escolhida: """))
            if opc == 1:
                iD = int(input("\nDigite o id do post: "))
                exUrl =f'https://jsonplaceholder.typicode.com/posts/{iD}'  
                
                conteudo = requests.get(url)
                dados = conteudo.json()  
                
                print("\n--- Dados encontrados com Sucesso ---")
                print(f"ID do Post: {dados['id']}")
                print(f"Título: {dados['title']}")
                print(f"Corpo: {dados['body']}")
                print(f"ID do Usuário: {dados['userId']}")
                
                
            elif opc == 2:
                title = input("Digite o titulo do post: ")
                body = input("Digite o corpo do post: ")
                userId = int(input("Digite o id do usuario: "))
                
                
                mail = {
                    "title": title,
                    "body": body,
                    "userId": userId
                }
                        
                content = requests.put(url, json= mail)
                print(content.status_code)
                        
                if content.status_code == 200:
                    Mailman = content.json()
                
                    print("\n--- Dados Atualizados com Sucesso ---")
                    print(f"ID do Post: {Mailman['id']}")
                    print(f"Título: {Mailman['title']}")
                    print(f"Corpo: {Mailman['body']}")
                    print(f"ID do Usuário: {Mailman['userId']}")
                else:
                    print("Erro ao atualizar: Verifique se a URL está correta!")
            elif opc == 3:
                iD = int(input("\nDigite o id do post a ser deletado: "))
                delUrl =f'https://jsonplaceholder.typicode.com/posts/{iD}' 
                
                try:
                    erase = requests.delete(delUrl)
                    print(erase.status_code)
                    print(erase.text)
                            
                    erase.raise_for_status()
                            
                            
                except requests.exceptions.ConnectionError:
                    print("Erro de conexão com o servidor.")
                
                except requests.exceptions.Timeout:
                    print("Requisição demorou demais.")
                            
                except requests.exceptions.HTTPError:
                    print("Houve um erro de HTTP.")
            elif opc == 4:
                print("Encerrando programa")
                break
    elif menu == 5:
        print("Encerrando programa")
        break
    
# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula09.py

# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 1

# --- Dados encontrados com Sucesso ---
# Título: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# Corpo: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
# ID do Usuário: 1

# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 2
# 200

# --- Dados Atualizados com Sucesso ---
# ID do Post: 1
# Título: TEST 11
# Corpo: 11th test of sending information
# ID do Usuário: 1

# ========================
#         Aula 08
# ========================    

# 1. Exercicio 1
# 2. Exercicio 2
# 3. Exercicio 3
# 4. Desafio  
# 5. Sair  
                                   
# Opção escolhida: 3
# 200
# {}

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
# 2 - Atualizar post
# 3 - Excluir post
# 4 - Sair
# Opção escolhida: 1

# Digite o id do post: 1

# --- Dados encontrados com Sucesso ---
# ID do Post: 1
# Título: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# Corpo: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
# ID do Usuário: 1

# ========================
#     Gerenciador Posts
# ========================

# 1 - Consultar post
# 2 - Atualizar post
# 3 - Excluir post
# 4 - Sair
# Opção escolhida: 2
# Digite o titulo do post: TEST 13
# Digite o corpo do post: 13th test of communication
# Digite o id do usuario: 1
# 200

# --- Dados Atualizados com Sucesso ---
# ID do Post: 1
# Título: TEST 13
# Corpo: 13th test of communication
# ID do Usuário: 1

# ========================
#     Gerenciador Posts
# ========================

# 1 - Consultar post
# 2 - Atualizar post
# 3 - Excluir post
# 4 - Sair
# Opção escolhida: 3

# Digite o id do post a ser deletado: 1
# 200
# {}

# ========================
#     Gerenciador Posts
# ========================

# 1 - Consultar post
# 2 - Atualizar post
# 3 - Excluir post
# 4 - Sair
# Opção escolhida: 4
# Encerrando programa

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