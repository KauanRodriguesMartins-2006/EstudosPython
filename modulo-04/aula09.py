import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 09
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        cursor.execute("SELECT * FROM usuarios WHERE id > 5 AND idade > 18")
        data = cursor.fetchall()
        
        for  id_u, nome_u, idade_u, email_u in data:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
#=============================================================================================================
    elif menu == 2:
        cursor.execute("SELECT * FROM usuarios WHERE idade < 20 OR idade > 30")
        data1 = cursor.fetchall()
        
        for  id_u, nome_u, idade_u, email_u in data1:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
#=============================================================================================================
    elif menu == 3:
        cursor.execute("SELECT * FROM usuarios WHERE idade BETWEEN 18 AND 30 OR nome LIKE 'P%'")
        data2 = cursor.fetchall()
        
        for  id_u, nome_u, idade_u, email_u in data2:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
#=============================================================================================================
    elif menu == 4:
        cursor.execute("SELECT * FROM usuarios WHERE nome LIKE '%a%'")
        data3 = cursor.fetchall()
        
        for  id_u, nome_u, idade_u, email_u in data3:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()