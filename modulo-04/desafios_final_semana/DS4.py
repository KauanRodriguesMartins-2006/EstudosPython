import sqlite3

conexao = sqlite3.connect("../bancos/estudos.db")
cursor = conexao.cursor()

while True:
    opc = int(input("""
========================
   RELATÓRIO DE VENDAS
========================

1. Relatório completo
2. Usuários sem pedidos
3. Usuário com mais pedidos
4. Sair
                    
Opção escolhida: """))
    
    if opc == 1:
        cursor.execute("""
                           SELECT usuarios.nome AS nome_u, COUNT(pedidos.id) AS quantidade
                           FROM usuarios
                           LEFT JOIN pedidos
                           ON usuarios.id = pedidos.usuario_id
                           GROUP BY usuarios.nome
                       """)
        
        data = cursor.fetchall()
        
        for nome_u, quantidade in data:
            print(f"Nome: {nome_u} | Quantidade de pedidos: {quantidade}")
#==================================================================================================

    elif opc == 2:
        cursor.execute("""
                           SELECT usuarios.nome AS nome_u1, COUNT(pedidos.id) AS quantidade1
                           FROM usuarios
                           LEFT JOIN pedidos
                           ON usuarios.id = pedidos.usuario_id
                           WHERE pedidos.id IS NULL
                           GROUP BY usuarios.nome
                       """)

        data1 = cursor.fetchall()
        
        for nome_u1, quantidade1 in data1:
            print(f"Nome: {nome_u1} | Quantidade de pedidos: {quantidade1}")
#==================================================================================================
    elif opc == 3:
        cursor.execute("""
                           SELECT usuarios.nome AS nome_u2, COUNT(pedidos.id) AS quantidade2
                           FROM usuarios
                           LEFT JOIN pedidos
                           ON usuarios.id = pedidos.usuario_id
                           GROUP BY usuarios.nome
                           ORDER BY quantidade2 DESC
                           LIMIT 1
                       """)
        
        data2 = cursor.fetchall()
        
        for nome_u2, quantidade2 in data2:
            print(f"Nome: {nome_u2} | Quantidade de pedidos: {quantidade2}")        
#==================================================================================================           
    elif opc == 4:
        print("Encerrando sistema")
        break   

        
cursor.close()
conexao.close()