import json
import os

while True:
    opc = int(input("""
==========================
      Biblioteca
==========================

1 - Cadastrar livro
2 - Listar livros
3 - Buscar livro
4 - Remover livro
5 - Sair               

Opção selecionada: """))

    if opc == 1:
        livros = []

        if os.path.isfile("livros.json"):
            titulo = input("Digite o título do livro: ")
            ano = int(input("Ano de lançamento: "))
            autor = input("Autor: ")

            livro = {"titulo": titulo, "ano": ano, "autor": autor}

            with open("livros.json", "r") as arquivo:
                conteudo = json.load(arquivo)

            conteudo.append(livro)

            with open("livros.json", "w") as arquivo:
                json.dump(conteudo, arquivo)

        else:
            titulo = input("Digite o título do livro: ")
            ano = int(input("Ano de lançamento: "))
            autor = input("Autor: ")

            livro = {"titulo": titulo, "ano": ano, "autor": autor}
            livros.append(livro)

            with open("livros.json", "w") as arquivo:
                json.dump(livros, arquivo)

    elif opc == 2:
        with open("livros.json", "r") as arquivo:
            conteudo = json.load(arquivo)

        for item in conteudo:
            print(f"""
            titulo.: {item["titulo"]}
            Ano....: {item["ano"]}      
            Autor..: {item["autor"]}  
        """)

    elif opc == 3:
        BuscaLivro = input("Digite o nome do livro: ")

        with open("livros.json", "r") as arquivo:
            conteudo = json.load(arquivo)

        for item in conteudo:
            if item["titulo"] == BuscaLivro:
                print("Livro encontrado!")
                print(f"""
                    titulo.: {item["titulo"]}
                    Ano....: {item["ano"]}      
                    Autor: {item["autor"]}  
                """)
                break
            else:
                print("Livro não encontrado!")

    elif opc == 4:
        BuscaLivro = input("Digite o nome do livro: ")

        with open("livros.json", "r") as arquivo:
            conteudo = json.load(arquivo)

        for item in conteudo:
            if item["titulo"] == BuscaLivro:
                conteudo.remove(item)
                break
            else:
                print("Livro não encontrado!")

        with open("livros.json", "w") as arquivo:
            json.dump(conteudo, arquivo)
    elif opc == 5:
        print("encerrando programa")
        break
    
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\Projetos_de_modulo\PM2> uv run ProjetoM2.py

# ==========================
#       Biblioteca
# ==========================

# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Buscar livro
# 4 - Remover livro
# 5 - Sair               

# Opção selecionada: 1
# Digite o título do livro: O pequeno principe
# Ano de lançamento: 1943
# Autor: Antoine de Saint-Exupéry

# ==========================
#       Biblioteca
# ==========================

# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Buscar livro
# 4 - Remover livro
# 5 - Sair               

# Opção selecionada: 1
# Digite o título do livro: Os santos
# Ano de lançamento: 2023
# Autor: Leandro Assis e Triscila Oliveira

# ==========================
#       Biblioteca
# ==========================

# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Buscar livro
# 4 - Remover livro
# 5 - Sair               

# Opção selecionada: 2

#             titulo.: O pequeno principe
#             Ano....: 1943      
#             Autor: Antoine de Saint-Exupéry  
        

#             titulo.: Os santos
#             Ano....: 2023      
#             Autor: Leandro Assis e Triscila Oliveira  
        

# ==========================
#       Biblioteca
# ==========================

# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Buscar livro
# 4 - Remover livro
# 5 - Sair               

# Opção selecionada: 3
# Digite o nome do livro: O pequeno principe
# Livro encontrado!

#                     titulo.: O pequeno principe
#                     Ano....: 1943      
#                     Autor: Antoine de Saint-Exupéry  
                
# Livro não encontrado!

# ==========================
#       Biblioteca
# ==========================

# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Buscar livro
# 4 - Remover livro
# 5 - Sair               

# Opção selecionada: 4
# Digite o nome do livro: 
# Livro não encontrado!
# Livro não encontrado!

# ==========================
#       Biblioteca
# ==========================

# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Buscar livro
# 4 - Remover livro
# 5 - Sair               

# Opção selecionada: 4
# Digite o nome do livro: 2
# Livro não encontrado!
# Livro não encontrado!

# ==========================
#       Biblioteca
# ==========================

# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Buscar livro
# 4 - Remover livro
# 5 - Sair               

# Opção selecionada: 4
# Digite o nome do livro: O pequeno principe

# ==========================
#       Biblioteca
# ==========================

# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Buscar livro
# 4 - Remover livro
# 5 - Sair               

# Opção selecionada: 2

#             titulo.: Os santos
#             Ano....: 2023      
#             Autor: Leandro Assis e Triscila Oliveira  
        

# ==========================
#       Biblioteca
# ==========================

# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Buscar livro
# 4 - Remover livro
# 5 - Sair               

# Opção selecionada: 5
# encerrando programa