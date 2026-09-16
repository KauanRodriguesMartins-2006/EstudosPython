import sqlite3

conexao = sqlite3.connect("../bancos/estudos.db")
cursor = conexao.cursor()

menu = 0

while menu != 5:
    menu = int(input("""
========================
   DESAFIO DE SÁBADO
========================

1. Mostrar usuários e pedidos
2. Mostrar usuários sem pedidos
3. Quantidade de pedidos por usuário
4. Ranking de usuários por pedidos
5. Sair

Opção escolhida: """))

    if menu == 1:
        cursor.execute("""
            SELECT usuarios.nome AS nome_u, pedidos.produto AS produto_p
            FROM usuarios
            JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
        """)

        dados = cursor.fetchall()

        for nome_u, produto_p in dados:
            print(f"Usuário: {nome_u} | Produto: {produto_p}")

    elif menu == 2:
        cursor.execute("""
            SELECT usuarios.nome AS nome_u1, pedidos.produto AS produto_p1
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            WHERE pedidos.id is NULL
        """)

        dados = cursor.fetchall()

        for nome_u1, produto_p1 in dados:
            print(f"Usuário: {nome_u1} | Produto: {produto_p1}")

    elif menu == 3:
        cursor.execute("""
            SELECT usuarios.nome, COUNT(pedidos.id) AS quantidade
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.nome
        """)

        dados = cursor.fetchall()

        for nome, quantidade in dados:
            print(f"Usuário: {nome} | Pedidos: {quantidade}")

    elif menu == 4:
        cursor.execute("""
            SELECT usuarios.nome, COUNT(pedidos.id) AS quantidade
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.nome
            ORDER BY quantidade DESC
        """)

        dados = cursor.fetchall()

        for nome, quantidade in dados:
            print(f"Usuário: {nome} | Pedidos: {quantidade}")

    elif menu == 5:
        print("Encerrando programa")

    else:
        print("Opção inválida")

cursor.close()
conexao.close()