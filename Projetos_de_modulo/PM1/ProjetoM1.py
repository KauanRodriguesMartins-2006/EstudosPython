Alunos = []


def cadastro_alunos():
    Nome = input("Digite o nome do aluno: ")
    Idade = int(input("Digite a idade do aluno: "))

    Alunos.append(f"{Nome} - {Idade}")


def mostrar_alunos():
    
    for i in Alunos:
        print("\n",i)

menu = 9
           
while menu != 0:
    menu = int(
        input("""
===== Sistema Escolar =====

1 - Cadastrar aluno
2 - Listar alunos
3 - Sair

""")
    )

    if menu == 1:
        cadastro_alunos()
    elif menu == 2:
        mostrar_alunos()
    elif menu == 3:
        print("Encerrando o programa.")
        break

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\python-roadmap\Projetos_de_modulo> uv run ProjetoM1.py

# ===== Sistema Escolar =====

# 1 - Cadastrar aluno
# 2 - Listar alunos
# 3 - Sair

# 1
# Digite o nome do aluno: Kauan
# Digite a idade do aluno: 19

# ===== Sistema Escolar =====

# 1 - Cadastrar aluno
# 2 - Listar alunos
# 3 - Sair

# 1
# Digite o nome do aluno: João
# Digite a idade do aluno: 18

# ===== Sistema Escolar =====

# 1 - Cadastrar aluno
# 2 - Listar alunos
# 3 - Sair

# 1
# Digite o nome do aluno: Maicoul Jaqcson
# Digite a idade do aluno: 25

# ===== Sistema Escolar =====

# 1 - Cadastrar aluno
# 2 - Listar alunos
# 3 - Sair

# 2

#  Kauan - 19

#  João - 18

#  Maicoul Jaqcson - 25

# ===== Sistema Escolar =====

# 1 - Cadastrar aluno
# 2 - Listar alunos
# 3 - Sair

# 3
# Encerrando o programa.