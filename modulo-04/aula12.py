import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 12
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        cursor.execute("""
                           CREATE TABLE IF NOT EXISTS pedidos(
                               id INTEGER PRIMARY KEY,
                               usuario_id INTEGER,
                               produto TEXT
                           )      
    """)
        
        while True:
            opc = int(input("""
1. Cadastro de produto                        
2. Sair
                         
Opção escolhida: """))
            
            if opc == 1:
                id_user = int(input("Digite o id de um usuário existente: "))
                produto_user = input("Digite o nome do produto que esse usuário comprou: ")
                
                sql = """
                         INSERT INTO pedidos (usuario_id, produto)
                         VALUES(?, ?);
                """
                
                cursor.execute(sql, (id_user, produto_user))
                
                conexao.commit()
 
            elif opc == 2:
                print("Retornando ao menu anterior")
                break
#================================================================================================================
    elif menu == 2:
        sql1 = """
SELECT usuarios.nome AS username, pedidos.produto AS user_product
FROM usuarios
JOIN pedidos
ON usuarios.id = pedidos.usuario_id          
"""

        cursor.execute(sql1)
        data = cursor.fetchall()
        
        for username, user_product in data:
            print(f"Usuário: {username} | Produto: {user_product}")
#================================================================================================================      
    elif menu == 3:
        id_select = int(input("Digite o id do usuário que deseja verificar o historico de compras: "))
        
        sql2 = """
        SELECT usuarios.nome AS username, pedidos.produto AS user_product
        FROM usuarios
        JOIN pedidos
        ON usuarios.id = pedidos.usuario_id          
        WHERE usuarios.id = ?
        """
        
        cursor.execute(sql2, (id_select,))
        data = cursor.fetchall()
                
        for username, user_product in data:
            print(f"Usuário: {username} | Produto: {user_product}")
#================================================================================================================
    elif menu == 4:
        sql1 = """
        SELECT usuarios.nome AS username, pedidos.produto AS user_product
        FROM usuarios
        JOIN pedidos
        ON usuarios.id = pedidos.usuario_id   
        ORDER BY usuarios.nome ASC       
        """
        
        cursor.execute(sql1)
        data = cursor.fetchall()
                
        for username, user_product in data:
            print(f"Usuário: {username} | Produto: {user_product}")
#================================================================================================================
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()