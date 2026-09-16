import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 08
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        cursor.execute("SELECT COUNT(*) FROM usuarios_api")
        cont = cursor.fetchone()[0]
        print(f"Quantidade de usuários: {cont}")
        
        cursor.execute("SELECT * FROM usuarios_api")
        lista_users = cursor.fetchall()
        
        for id_u, nome_u, email_u in lista_users:
            print(f"Id: {id_u} | Nome: {nome_u} | Email: {email_u}")
#=====================================================================================            
    elif menu == 2:
        cursor.execute("SELECT * FROM usuarios_api ORDER BY nome LIMIT  3")
        limit_users = cursor.fetchall()
        
        for id_u, nome_u, email_u in limit_users:
            print(f"Id: {id_u} | Nome: {nome_u} | Email: {email_u}")
#=====================================================================================            
    elif menu == 3:
        cursor.execute("SELECT COUNT(*) FROM usuarios_api WHERE id > 5")
        more_users = cursor.fetchone()[0]
        
        print(f"Quantidade de usuários: {more_users}")
#=====================================================================================
    elif menu == 4:
        cursor.execute("SELECT MIN(id) FROM usuarios_api")
        minimo = cursor.fetchone()[0]
        
        cursor.execute("SELECT MAX(id) FROM usuarios_api")
        maximo = cursor.fetchone()[0]
        
        print(f"Menor id de usuário: {minimo} | Maior id de usuário: {maximo}")
    elif menu == 5:
        print("Encerrando programa")
        break
    
cursor.close()
conexao.close()