import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 13
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        sql = """
            SELECT usuarios.nome AS username, pedidos.produto AS user_product
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
        """
        
        cursor.execute(sql)
        data = cursor.fetchall()
        
        for username, user_product in data:
            print(f"Usuário: {username} | Produto: {user_product}")
    elif menu == 2:
        sql1 = """
                    SELECT usuarios.nome AS username1, pedidos.produto AS user_product1
                    FROM usuarios
                    LEFT JOIN pedidos
                    ON usuarios.id = pedidos.usuario_id
                    WHERE pedidos.id IS NULL
                """
                
        cursor.execute(sql1)
        data1 = cursor.fetchall()
                
        for username1, user_product1 in data1:
            print(f"Usuário: {username1} | Produto: {user_product1}")
    elif menu == 3:
        sql2 = """
                    SELECT usuarios.nome AS username2, COUNT(pedidos.id) AS quantidade
                    FROM usuarios
                    LEFT JOIN pedidos
                    ON usuarios.id = pedidos.usuario_id
                    GROUP BY usuarios.nome 
                """
                        
        cursor.execute(sql2)
        data2 = cursor.fetchall()
                        
        for username2, quantidade in data2:
            print(f"Usuário: {username2} | Quantidade de Produtos: {quantidade}")
    elif menu == 4:
        sql3 = """
                    SELECT usuarios.nome AS username3, COUNT(pedidos.id) AS quantidade1
                    FROM usuarios
                    LEFT JOIN pedidos
                    ON usuarios.id = pedidos.usuario_id
                    GROUP BY usuarios.nome 
                """
                                
        cursor.execute(sql3)
        data3 = cursor.fetchall()
                                
        print("\n==== Usuários que possuem pedidos ====")
        for username3, quantidade1 in data3:
            if quantidade1 > 0:
                print(f"Usuário: {username3} | Quantidade de Produtos: {quantidade1}")
        print("--------------------------------------------------------------------------------")
        print("==== Usuários que não possuem pedidos ====")
        for username3, quantidade1 in data3:
            if quantidade1 == 0:
                print(f"Usuário: {username3} | Quantidade de Produtos: {quantidade1}")
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()