# import json

# # == Exercicio 01 ==
# filme = [
#     {
#         "título": "Interestelar",
#         "ano": 2014,
#         "diretor": "Christopher Nolan"
#     }
# ]

# for item in filme:
#     print(f"""
# Título: {item["título"]}      
# Ano: {item["ano"]}      
# Diretor: {item["diretor"]}      
#           """)
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula05.py

# Título: Interestelar      
# Ano: 2014      
# Diretor: Christopher Nolan 




# # == Exercicio 02 ==
# filmes = [
#     {
#         "título": "Avengers: Doomsday",
#         "ano": 2026,
#         "diretor": "Anthony e Joe Russo"
#     },
#     {
#         "título": "Godzilla II: Rei dos Monstros",
#         "ano": 2019,
#         "diretor": "Michael Dougherty"
#     },
#     {
#         "título": "Círculo de Fogo",
#         "ano": 2013,
#         "diretor": "Guillermo del Toro"
#     }
# ]

    
# for filme in filmes:
#     print("Título: ",filme["título"],"\n","Ano: ",filme["ano"],"\n","Diretor: ",filme["diretor"])

# # Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula05.py
# Título:  Avengers: Doomsday 
#  Ano:  2026 
#  Diretor:  Anthony e Joe Russo
# Título:  Godzilla II: Rei dos Monstros 
#  Ano:  2019 
#  Diretor:  Michael Dougherty
# Título:  Círculo de Fogo 
#  Ano:  2013 
#  Diretor:  Guillermo del Toro




# # == Exercicio 03 ==
# filme = {
#           "título": "Transformers: A Era da Extinção",
#           "ano": 2014,
#           "diretor": "Michael Bay"
#          }
    

# resultado = json.dumps(filme)

# print(resultado)

#  Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula05.py
# {"t\u00edtulo": "Transformers: A Era da Extin\u00e7\u00e3o", "ano": 2014, "diretor": "Michael Bay"}




# # == Desafio ==
# livros = [
#     {
#         "título": "O Pequeno Príncipe",
#         "ano": 1943,
#         "autor": "Antoine de Saint-Exupéry"
#     },
#     {
#         "título": "Dom Casmurro",
#         "ano": 1899,
#         "autor": "Machado de Assis"
#     },
#     {
#         "título": "O Senhor dos Anéis: A Sociedade do Anel",
#         "ano": 1954,
#         "autor": "J.R.R. Tolkien"
#     }
# ]

# resultado = json.dumps(livros)
# print(resultado)
        
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula05.py
# [{"t\u00edtulo": "O Pequeno Pr\u00edncipe", "ano": 1943, "autor": "Antoine de Saint-Exup\u00e9ry"}, {"t\u00edtulo": "Dom Casmurro", "ano": 1899, "autor": "Machado de Assis"}, {"t\u00edtulo": "O Senhor dos An\u00e9is: A Sociedade do Anel", "ano": 1954, "autor": "J.R.R. Tolkien"}]


# # == Desafio Extra ==

# Resultado: