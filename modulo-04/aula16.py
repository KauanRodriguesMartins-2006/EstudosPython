import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 16
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        sql = """
            SELECT nome, idade,
                CASE
                    WHEN idade >= 18 THEN 'Maior de idade'
                    ELSE 'Menor de idade'
                END AS classificacao
            FROM usuarios  
        """
        
        cursor.execute(sql)
        data = cursor.fetchall()
        
        for nome_u, idade_u, classificacao_u in data:
            print(f"Nome: {nome_u} | Idade: {idade_u} | Classificação: {classificacao_u}")
        
    elif menu == 2:
        sql1 = """
            SELECT nome, idade,
                CASE
                    WHEN idade >= 12 AND idade < 18 THEN 'Adolescente'
                    WHEN idade >= 18 AND idade < 30 THEN 'Jovem Adulto'
                    WHEN idade >= 30 THEN 'Adulto'
                    ELSE 'Criança'
                END AS faixa_etaria
            FROM usuarios  
        """
        cursor.execute(sql1)
        data1 = cursor.fetchall()
                
        for nome_u, idade_u, faixa_etaria in data1:
            print(f"Nome: {nome_u} | Idade: {idade_u} | Faixa etária: {faixa_etaria}")
        
    elif menu == 3:
        #No momento da execução deste código so tinha/tem um registro na tabela pedidos :\
        sql2 = """
            SELECT usuarios.nome AS username, COUNT(pedidos.id) AS quantidade,
                CASE
                    WHEN COUNT(pedidos.id) = 0 THEN 'Sem pedidos'
                    WHEN COUNT(pedidos.id) = 1 THEN 'Poucos pedidos'
                    WHEN COUNT(pedidos.id) = 2 THEN 'Vários pedidos'
                    WHEN COUNT(pedidos.id) >= 3 THEN 'Muitos pedidos'
                END AS situacao
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.id
            ORDER BY nome
        """
        
        cursor.execute(sql2)
        data2 = cursor.fetchall()
        
        for username, quantidade, situacao in data2:
            print(f"Nome: {username} | Quantidade de pedidos: {quantidade} | Situação: {situacao}")
        
    elif menu == 4:
        sql3 = """
            SELECT usuarios.nome AS username, pedidos.produto AS produto,
                CASE
                    WHEN idade < 18 THEN 'Menor de idade'
                    WHEN idade >= 18 AND idade < 30 THEN 'Jovem'
                    WHEN idade >= 30 THEN 'Adulto'
                END AS idade_usuario
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.id
            ORDER BY nome
        """
        
        cursor.execute(sql3)
        data2 = cursor.fetchall()
                
        for username, produto, idade_usuario in data2:
            print(f"Nome: {username} | Produto comprado: {produto} | Grupo etário: {idade_usuario}")
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()