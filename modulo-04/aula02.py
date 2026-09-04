import sqlite3


menu = 10
while True:
    menu = int(input("""
========================
        Aula 02
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        conexao = sqlite3.connect("bancos/estudos.db")
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM usuarios")
        
        data = cursor.fetchall()
        print(data)
        
        cursor.close()
        conexao.close()
        
    elif menu == 2:
        conexao1 = sqlite3.connect("bancos/estudos.db")
        cursor1 = conexao1.cursor()
        
        id_select = int(input("Digite um id de usuário: "))
        cursor1.execute(f"SELECT * FROM usuarios WHERE id = {id_select}")
        data1 = cursor1.fetchone()
        
        print(data1)
        
        cursor1.close()
        conexao1.close()

    elif menu == 3:
        conexao2 = sqlite3.connect("bancos/estudos.db")
        cursor2 = conexao2.cursor()
        
        age_check = int(input("Digite a idade do usuário que deseja achar: "))
        cursor2.execute(f"SELECT * FROM usuarios WHERE idade = {age_check}")
        data2 = cursor2.fetchall()
        
        print(data2)
        
        if data2 == []:
            print("Nenhum usuário encontrado")
        
        cursor2.close()
        conexao2.close()

    elif menu == 4:
        conexao3 = sqlite3.connect("bancos/estudos.db")
        cursor3 = conexao3.cursor()
        
        cursor3.execute("SELECT * FROM usuarios")
        data3 = cursor3.fetchall()
        
        cont = 0
        
        for i in data3:
            cont += 1
        
        cursor3.execute("SELECT idade FROM usuarios ORDER BY idade DESC LIMIT 1")
        data4 = cursor3.fetchone()
        cursor3.execute("SELECT idade FROM usuarios ORDER BY idade ASC LIMIT 1")
        data5 = cursor3.fetchone()
        
        cursor3.execute("SELECT AVG(idade) AS media_idade FROM usuarios")
        data6 = cursor3.fetchall()
        
        age_check = int(input("Digite a idade do usuário que deseja achar: "))
        cursor3.execute(f"SELECT * FROM usuarios WHERE idade = {age_check}")
        data7 = cursor3.fetchall()
        
        print(f"""
========== RELATÓRIO ==========

Total de usuários: {cont}
Maior idade: {data4}
Menor idade: {data5}
Média das idades: {data6}

Usuários encontrados:
{data7}            
""")
        
        
        
#         O programa deve:

# Buscar todos os usuários com SELECT + fetchall().
# Calcular no Python:
# quantidade total de usuários;
# maior idade;
# menor idade;
# média das idades.
# Pedir uma idade ao usuário.
# Fazer uma nova consulta usando WHERE para encontrar todos os usuários daquela idade.
# Mostrar os usuários encontrados.
# Se não houver usuários com aquela idade, informar isso.
# Fechar cursor e conexão.
    elif menu == 5:
        print("Encerrando programa")
        break