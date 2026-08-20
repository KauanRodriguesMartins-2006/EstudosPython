import requests

url = 'https://httpbin.org/cookies/set'
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
        cookie_param = {
            "usuario": "pessoa",
            "curso": "python"
        }
        
        cookie_request = sessao.get(url, params= cookie_param)
        
        urlTest = 'https://httpbin.org/cookies'
        new_request = sessao.get(urlTest)
        nr = new_request.json()
        
        print(f"""
Código_status: {new_request.status_code}
Resposta_json: {new_request.json()}
Cookies......: {sessao.cookies}              
""")
# ==========================================================================================   
    elif menu == 2:
        new_session = requests.Session()
        new_session.cookies.update({
            "usuario": "individuo",
            "nivel": "iniciante"
        })
        
        urlC = 'https://httpbin.org/cookies'
        
        urlReq = new_session.get(urlC)
        
        print(f"""
Código_status: {urlReq.status_code}
Resposta_json: {urlReq.json()}
Cookies......: {sessao.cookies}              
        """)
# ==========================================================================================   
    elif menu == 3:    
        url_definir = 'https://httpbin.org/cookies'

        response1 = requests.get(url_definir, cookies={"meu_cookie": "valor1"})
        print("Cookies ativos na sessão:", response1.json())
        
# *****************************************************************
        
        
        cookie_definir = 'https://httpbin.org/set/cookie_da_sessao/valor2'
        sessao.get(cookie_definir)
                

        cookie_verificar = 'https://httpbin.org/cookies'
        resposta2 = sessao.get(cookie_verificar)


        try:
            print("Cookies ativos na sessão:", resposta2.json())
        except Exception:
            print("\n--- DETALHES DO ERRO ---")
            print("O código quebrou porque o site NÃO devolveu um JSON.")
            print("URL real que foi acessada:", resposta2.url)
            print("Código de status do site:", resposta2.status_code)
            print("O que veio escrito no site (primeiros 300 caracteres):")
            print(resposta2.text[:300])
            print("------------------------\n")
# ==========================================================================================   
    elif menu == 4:
        url_auth = 'https://httpbin.org/basic-auth/usuario/senha'
        try_auth = ('usuario', 'senha')
        autentic = sessao.get(url_auth, auth= try_auth )
        
        if autentic.status_code == 200:
            print(f"Retorno_json.: {autentic.json()}")
        else:
            print("Falha na autenticação ou página não encontrada.")
            print(f"Texto retornado pelo servidor: {autentic.text}")
    elif menu == 5:
        print("Encerrando programa")
        break