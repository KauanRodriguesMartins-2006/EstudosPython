nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print(f"""
     =======================
     RELATÓRIO DO ALUNO
     =======================
      
     Nome: {nome}
     Idade: {idade}
     Nota 1: {nota1}
     Nota 2: {nota2}
     Média : {media}
""")