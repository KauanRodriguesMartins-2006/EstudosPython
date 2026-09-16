import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 14
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        cursor.execute("""
            SELECT usuarios.nome AS nome_u
            FROM usuarios
            WHERE id IN(
                SELECT usuario_id
                FROM pedidos
            )      
        """)
        
        data = cursor.fetchall()
        
        
        for nome_u in data:
            print(f"Nome: {nome_u[0]}")
#===========================================================         
    elif menu == 2:
        cursor.execute("""
            SELECT usuarios.nome AS nome_u1
            FROM usuarios
            WHERE id NOT IN(
                SELECT usuario_id
                FROM pedidos
            )      
        """)
                
        data1 = cursor.fetchall()
                
                
        for nome_u1 in data1:
            print(f"Nome: {nome_u1[0]}")
#===========================================================
    elif menu == 3:
        cursor.execute("""
            SELECT usuarios.nome AS nome_u2, usuarios.idade as idade_u
            FROM usuarios
            WHERE idade > (
                SELECT AVG(idade) AS media_idade
                FROM usuarios
            )      
        """)
                        
        data2 = cursor.fetchall()
                        
                      
        for nome_u2, idade_u in data2:
            print(f"Nome: {nome_u2} | Idade: {idade_u}")
#===========================================================           
    elif menu == 4:
        cursor.execute("""
    SELECT nome_n, quantidade
    FROM (
        SELECT usuarios.nome AS nome_n, COUNT(*) AS quantidade
        FROM pedidos
        JOIN usuarios
        ON pedidos.usuario_id = usuarios.id
        GROUP BY usuario_id
    )
    WHERE quantidade = (
        SELECT MAX(quantidade)
        FROM (
            SELECT COUNT(*) AS quantidade
            FROM pedidos
            GROUP BY usuario_id
        )
    )
""")
                                
        data3 = cursor.fetchall()
                                
                              
        for nome_n, quantidade in data3:
            print(f"Nome: {nome_n} | Quantidade de pedidos: {quantidade}")
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()