import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 10
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        idade_select = int(input("Digite a idade que quer procurar: "))
        
        cursor.execute("SELECT * FROM usuarios WHERE idade > ?", (idade_select,))
        data = cursor.fetchall()
        
        for id_u, nome_u, idade_u, email_u in data:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
#=============================================================================================
    elif menu == 2:
        name_select = input("Digite parte de um nome: ")
        
        cursor.execute("SELECT * FROM usuarios WHERE nome LIKE ?", (f'%{name_select}%',))
        data1 = cursor.fetchall()
        
        for  id_u, nome_u, idade_u, email_u in data1:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
#=============================================================================================
    elif menu == 3:
        idade_min = int(input("Digite a idade minima: "))
        idade_max = int(input("Digite a idade maxima: "))
        
        cursor.execute("SELECT * FROM usuarios WHERE idade BETWEEN ? AND ?",(idade_min, idade_max,))
        data2 = cursor.fetchall()
        
        for  id_u, nome_u, idade_u, email_u in data2:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
    elif menu == 4:
        idade = int(input("Digite a idade minima: "))
        nome_parcial = input("Digite uma letra de um nome: ")
        
        if idade and nome_parcial:
            cursor.execute("SELECT * FROM usuarios WHERE idade >= ? AND nome LIKE ?", (idade, f'%{nome_parcial}%',))
            data3 = cursor.fetchall()
          
            for  id_u, nome_u, idade_u, email_u in data3:
                print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")  
            

    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()