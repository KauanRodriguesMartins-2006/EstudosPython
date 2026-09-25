import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 20
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        sql_co = """
            SELECT usuarios.nome, COALESCE(pedidos.produto, "Sem informação") AS produto
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
        """
        
        cursor.execute(sql_co)
        data_co = cursor.fetchall()
        
        for nome_co, produto_co in data_co:
            print(f"Nome: {nome_co} | Produto: {produto_co}")
#=================================================================  
    elif menu == 2:
        sql_count = """
            SELECT usuarios.nome, COALESCE(COUNT(pedidos.id), '0') AS pedidos_qtd
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.id
            ORDER BY pedidos.usuario_id DESC
        """
        
        cursor.execute(sql_count)
        data_count = cursor.fetchall()
        
        for nome_count, pedidos_qtd in data_count:
            print(f"Nome: {nome_count} | Quantidade de pedidos: {pedidos_qtd}")
        
        
#=================================================================     
    elif menu == 3:
        sql_conc = """
            SELECT usuarios.nome, COALESCE("Pedido: " || pedidos.produto, "Sem pedido cadastrado") AS descricao_pedido
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
        """
        cursor.execute(sql_conc)
        data_conc = cursor.fetchall()
        
        for nome_conc, descricao_pedido in data_conc:
            print(f"Nome: {nome_conc} | {descricao_pedido}")
#=================================================================
    elif menu == 4:
        sql = """
            SELECT usuarios.nome, COUNT(pedidos.id) AS quantidade, COALESCE(
                (SELECT 'Possui pedidos' FROM pedidos WHERE pedidos.usuario_id = usuarios.id LIMIT 1),
                 'Sem pedidos'
            ) AS situacao
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.id
            ORDER BY quantidade DESC
        """
        
        cursor.execute(sql)
        data = cursor.fetchall()
        
        for nome, quantidade, situacao in data:
            print(f"Nome: {nome} | Quantidade: {quantidade} | Situação: {situacao}")
        
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()