# import requests

# # == Exercicio 01 ==
# try:
#     conteudo = requests.get("https://jsonplaceholder.typicode.com/rota-que-nao-existe", timeout= 30)
#     conteudo.raise_for_status()
#     print(conteudo.status_code)
    
# except requests.exceptions.ConnectionError:
#     print("Erro de conexão com o servidor.")

# except requests.exceptions.Timeout:
#     print("Requisição demorou demais.")
    
# except requests.exceptions.HTTPError:
#     print("Houve um erro de HTTP.")
    
# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula05.py                                                                        
# 200   
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula05.py
# Requisição demorou demais.
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula05.py
# Houve um erro de HTTP.


# # == Desafio ==

# while True:
#     opc = int(input("""
# ==================
# Consulta CEP
# ==================

# 1. Consulta Cep
# 2. Sair

# Opção selecionada: """))
    
#     if opc == 1:
#        try:
#             dg_cep = input("Digite um Cep: ")
                   
#             conteudo = requests.get(f"https://brasilapi.com.br/api/cep/v1/{dg_cep}", timeout= 15)
           
#             dados = conteudo.json()
           
#             if conteudo.status_code == 200:
#                        print(f"""
# CEP........: {dados["cep"]}
# Rua........: {dados["street"]}
# Bairro.....: {dados["neighborhood"]}
# Cidade.....: {dados["city"]}
# Estado.....: {dados["state"]}
#                        """)
#             else:
#                 print("Cep invalido")
#        except requests.exceptions.ConnectionError:
#            print("Erro de conexão com o servidor.")

#        except requests.exceptions.Timeout:
#            print("Requisição demorou demais.")
    
#        except requests.exceptions.HTTPError:
#            print("Houve um erro de HTTP.")
            
#     elif opc == 2:
#         print("Encerrando programa")
#         break
    
# Resultado:
# (modulo-03) PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-03> uv run aula05.py

# ==================
# Consulta CEP
# ==================

# 1. Consulta Cep
# 2. Sair

# Opção selecionada: 1
# Digite um Cep: 41347278 

# CEP........: 41347278
# Rua........: Rua Geraldo Brasil
# Bairro.....: Cajazeiras XI
# Cidade.....: Salvador
# Estado.....: BA
                       

# ==================
# Consulta CEP
# ==================

# 1. Consulta Cep
# 2. Sair

# Opção selecionada: 2
# Encerrando programa




# # == Desafio Extra ==

# Resultado: