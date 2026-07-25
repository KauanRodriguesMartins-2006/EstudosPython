nome = input("Digite o nome do aluno: ")
idade= int(input("Digite a idade do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) /2
Midade = "Sim"


if idade >= 18:
    Midade = "Sim"
else:
    Midade = "Não"

print(f"""
=========================
      Relatorio
=========================
      
Nome.............: {nome}

Idade............: {idade}

Maior de idade...: {Midade}

Nota 1...........: {nota1}

Nota 2...........: {nota2}

Média............: {media}

""")