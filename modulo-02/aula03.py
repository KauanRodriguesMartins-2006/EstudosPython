# # == Exercicio 01 ==
# alunos = [
#     {
#         "nome": "Kauan",
#         "idade": 19
#     },
#     {
#         "nome": "Artur",
#         "idade": 20
#     }
# ]

# print(alunos[0])
# print(alunos[1])

# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula03.py
# {'nome': 'Kauan', 'idade': 19}
# {'nome': 'Artur', 'idade': 20}




# # == Exercicio 02 ==
# alunos = [
#     {
#         "nome": "Kauan",
#         "idade": 19
#     },
#     {
#         "nome": "Artur",
#         "idade": 20
#     }
# ]

# for aluno in alunos:
#     print("Nome: ",aluno["nome"],"\n","Idade: ",aluno["idade"])
    
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula03.py
# Nome:  Kauan 
#  Idade:  19
# Nome:  Artur 
#  Idade:  20




# # == Exercicio 03 ==
# alunos = [
#     {
#         "nome": "Kauan",
#         "idade": 19
#     },
#     {
#         "nome": "Artur",
#         "idade": 20
#     }
# ]

# novo_aluno =  {
#         "nome": "Maria",
#         "idade": 19 
#     }


# alunos.append(novo_aluno)

# for aluno in alunos:
#     print("Nome: ",aluno["nome"],"\n","Idade: ",aluno["idade"])
    
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula03.py
# Nome:  Kauan 
#  Idade:  19
# Nome:  Artur 
#  Idade:  20
# Nome:  Maria 
#  Idade:  19




# # == Desafio ==
# funcionarios = [
#     {
#         "nome": "Kauan",
#         "cargo": "Desenvolvedor pleno",
#         "salário": 3200
#     },
#     {
#         "nome": "Daniel",
#         "cargo": "Desenvolvedor sênior",
#         "salário": 4800
#     },
#     {
#         "nome": "Gabriel",
#         "cargo": "Desenvolvedor Junior",
#         "salário": 2800
#     },
#     {
#         "nome": "Sarah",
#         "cargo": "Desenvolvedor Junio",
#         "salário": 2800
#     }
# ]



# for funcionario in funcionarios:
#     print("Nome: ",funcionario["nome"],"\n","Cargo: ",funcionario["cargo"],"\n","Salário: ",funcionario["salário"])
    
# Resultado:
# PS C:\Users\kauan\OneDrive\Desktop\EstudosPython\modulo-02> uv run aula03.py
# Nome:  Kauan 
#  Cargo:  Desenvolvedor pleno 
#  Salário:  3200
# Nome:  Daniel 
#  Cargo:  Desenvolvedor sênior 
#  Salário:  4800
# Nome:  Gabriel 
#  Cargo:  Desenvolvedor Junior 
#  Salário:  2800
# Nome:  Sarah 
#  Cargo:  Desenvolvedor Junio 
#  Salário:  2800





