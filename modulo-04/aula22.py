import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 22
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        sql_cast = """
            SELECT usuarios.nome, usuarios.idade, CAST(idade AS TEXT) AS idade_texto
            FROM usuarios
        """
        
        cursor.execute(sql_cast)
        data_cast = cursor.fetchall()
        
        for nome_cast, idade_cast, idade_texto in data_cast:
            print(f"Nome: {nome_cast} | Idade: {idade_cast} | Idade convertida: {type(idade_texto)}")
#======================================================================================================
    elif menu == 2:
        sql_real = """
            SELECT usuarios.nome, usuarios.idade, CAST(idade AS REAL) AS idade_decimal
            FROM usuarios
            ORDER BY idade_decimal DESC
        """
        
        cursor.execute(sql_real)
        data_real = cursor.fetchall()
        
        for nome_real, idade_real, idade_decimal in data_real:
            print(f"Nome: {nome_real} | Idade: {idade_real} | Idade convertida: {type(idade_decimal)}")
#======================================================================================================
    elif menu == 3:
        sql_half = """
            SELECT usuarios.nome, usuarios.idade, CAST(idade AS REAL) / 2 AS idade_metade
            FROM usuarios
        """
        
        cursor.execute(sql_half)
        data_half = cursor.fetchall()
        
        for nome_half, idade_half, idade_metade in data_half:
            print(f"Nome: {nome_half} | Idade: {idade_half} | Metade da idade: {idade_metade}")
#======================================================================================================
    elif menu == 4:
        sql_qtdP = """
            SELECT usuarios.nome, COUNT(pedidos.id) AS qtd_pedidos, CAST(COUNT(pedidos.id) AS TEXT) AS qtd_text
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.id
            ORDER BY qtd_pedidos DESC
        """
        
        cursor.execute(sql_qtdP)
        data_qtdP = cursor.fetchall()
        
        for nome_p, qtd_pedidos, qtd_text in data_qtdP:
            print(f"Nome: {nome_p} | Quantidade de pedidos: {qtd_pedidos} | Quantidade de pedidos em texto: {qtd_text} - {type(qtd_text)}")
        
#======================================================================================================
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()