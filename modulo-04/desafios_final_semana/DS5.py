import sqlite3

conexao = sqlite3.connect("../bancos/estudos.db")
cursor = conexao.cursor()

while True:
    opcao = int(input("""
========================
   DESAFIO — BUGS
========================

1. Listar usuários e pedidos
2. Usuários sem pedidos
3. Quantidade de pedidos
4. Ranking de pedidos
5. Sair

Opção: """))

    if opcao == 1:
        sql = """
            SELECT usuarios.nome, pedidos.produto
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
        """

        cursor.execute(sql)
        dados = cursor.fetchall()

        for nome, produto in dados:
            print(f"{nome} -> {produto}")

    elif opcao == 2:
        sql = """
            SELECT usuarios.nome
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            WHERE pedidos.id is NULL
        """

        cursor.execute(sql)
        dados = cursor.fetchall()

        for nome in dados:
            print(f"Sem pedidos: {nome[0]}")

    elif opcao == 3:
        sql = """
            SELECT usuarios.nome, COUNT(pedidos.id) AS quantidade
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.nome
        """

        cursor.execute(sql)
        dados = cursor.fetchall()

        for nome, quantidade in dados:
            print(f"{nome}: {quantidade} pedido(s)")

    elif opcao == 4:
        sql = """
            SELECT usuarios.nome, COUNT(pedidos.id) AS quantidade
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.nome
            ORDER BY quantidade DESC
        """

        cursor.execute(sql)
        dados = cursor.fetchall()

        for nome, quantidade in dados:
            print(f"{nome}: {quantidade} pedido(s)")

    elif opcao == 5:
        print("Encerrando...")
        break

cursor.close()
conexao.close()