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
    
    if menu == 1:
        url1 = 'https://httpbin.org/get'
        resposta = sessao.get(url1)
        print(f"""
Código_status: {resposta.status_code}
Tipo_conteudo: {resposta.headers.get["Content-Type"]}       
Server.......: {resposta.headers.get["Server"]}
Todos_headers: {resposta.headers.get}       
""")
# ==========================================================================================   

    elif menu == 2:
        url2 = 'https://httpbin.org/html'
        
        response2 = sessao.get(url2)
        print(f"""
Código_status...: {response2.status_code}
Type_text.......: {type(response2.text)}      
Type_content....: {type(response2.content)}
Response_text...: {response2.text[:100]}
Response_content: {response2.content[:100]}
""")
# ==========================================================================================   
      
    elif menu == 3:
        url3 = 'https://httpbin.org/encoding/utf8'
        
        response3 = sessao.get(url3)
        print(f"""
Código_status...: {response3.status_code}
Codificação.....: {response3.encoding}
Type_text.......: {type(response3.text)}
Response_text...: {response3.text[:100]}    
""")
        
        response3.encoding = 'utf-8'
    
        print(f"Codificação(utf-8): {response3.encoding }")
# ==========================================================================================   
    elif menu == 4:
        try:
            while True:
                opc = int(input("""
1. Procura por userId
2. Retornar ao menu anterior                                

Opção escolhida: """))
                
                if opc == 1:
                    idU_search_request = int(input("Digite o id do usuário: "))
                    url4 = 'https://jsonplaceholder.typicode.com/posts'
                                
                    param = {
                        "userId": idU_search_request
                    }
                                
                    response4 = sessao.get(url4, params= param, timeout=0.1)
                    r4 = response4.json()
                                
                    print(f"Código_status: {response4.status_code}")
                    count = 0
                                
                    for i in r4:
                        count += 1
                        print(f"Title: {i["title"]}")
                                    
                    print(f"número de posts encontrados: {count}")
                
                elif opc == 2:
                    print("Retornando ao programa anterior")
                    break
            
        except requests.exceptions.RequestException:
            print("Houve um erro na sua requisição")
    elif menu == 5:
        print("Encerrando programa")
        break