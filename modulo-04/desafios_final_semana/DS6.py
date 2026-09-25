import sqlite3

conexao = sqlite3.connect("../bancos/estudos.db")
cursor = conexao.cursor()

while True:
    menu = int(input("""
========================
   RELATÓRIO DE USUÁRIOS
========================

1. Relatório geral
2. Usuários sem pedidos
3. Usuário com mais pedidos
4. Filtrar usuários por idade
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        sql_rg = """
            SELECT usuarios.nome, usuarios.idade, COUNT(pedidos.id) AS quantidade
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.id
            ORDER BY pedidos.id DESC
        """
        
        cursor.execute(sql_rg)
        data_rg = cursor.fetchall()
        
        for nome_rg, idade_rg, quantidade_rg in data_rg:
            print(f"Nome: {nome_rg} | Idade: {idade_rg} | Pedidos: {quantidade_rg}")
#================================================================================================================     
    elif menu == 2:
        sql_usp = """
           SELECT usuarios.nome AS nome, pedidos.id AS pedidos
           FROM usuarios
           LEFT JOIN pedidos
           ON usuarios.id = pedidos.usuario_id
           WHERE pedidos.id is NULL
        """
           
        cursor.execute(sql_usp)
        dados_usp = cursor.fetchall()
           
        for nome_usp in dados_usp:
            print(f"Sem pedidos: {nome_usp[0]}")
#================================================================================================================      
    elif menu == 3:
        sql_ump = """
            SELECT usuarios.nome, COUNT(pedidos.id) AS pedidos
            FROM usuarios
            JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.id
            ORDER BY pedidos DESC
            LIMIT 1
        """
        
        cursor.execute(sql_ump)
        data_ump = cursor.fetchall()
        
        for nome_ump, pedidos_ump in data_ump:
            print(f"Nome: {nome_ump} | Pedidos: {pedidos_ump}")
#================================================================================================================
    elif menu == 4:
        idade_min = int(input("Digita uma idade minima que deseje filtrar: "))
        
        sql_fui = """
            SELECT usuarios.nome, usuarios.idade, COUNT(pedidos.id) AS quantidade
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            WHERE idade >= ?
            GROUP BY usuarios.id
            ORDER BY pedidos.id DESC
        """
        
        cursor.execute(sql_fui, (idade_min,))
        data_fui = cursor.fetchall()
        
        for nome_fui, idade_fui, quantidade_fui in data_fui:
            print(f"Nome: {nome_fui} | Idade: {idade_fui} | Pedidos: {quantidade_fui}")
#================================================================================================================
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()