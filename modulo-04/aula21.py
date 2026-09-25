import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 21
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        sql_iv = """
            SELECT usuarios.nome, usuarios.idade, NULLIF(idade, 0) AS idade_validada
            FROM usuarios   
        """
        
        cursor.execute(sql_iv)
        data_iv = cursor.fetchall()
        
        for nome_iv, idade_iv, idade_validada_iv in data_iv:
            print(f"Nome: {nome_iv} | Idade: {idade_iv} | Idade validada: {idade_validada_iv}")
#===========================================================================================================================================================================
    elif menu == 2:
        sql_qtdNull = """
            SELECT usuarios.idade, COUNT(idade) AS qtd_idade, NULLIF(COUNT(idade), 1) AS idade_validada
            FROM usuarios
            GROUP BY usuarios.idade
            ORDER BY idade ASC
        """
        
        cursor.execute(sql_qtdNull)
        data_qtdNull = cursor.fetchall()
        
        for idade_qn, qtd_idade_qn, idade_validada_qn in data_qtdNull:
            print(f"Idade: {idade_qn} \nQunatidade de pessoas com essa idade: {qtd_idade_qn} \nIdade validada: {idade_validada_qn}\n")
#===========================================================================================================================================================================
    elif menu == 3:
        sql_ec = """
            SELECT usuarios.nome, usuarios.idade, usuarios.email, NULLIF(email, CASE WHEN idade = 22 THEN email ELSE NULL END) AS email_validado
            FROM usuarios
        """
        
        cursor.execute(sql_ec)
        data_ec = cursor.fetchall()
        
        for nome_ec, idade_ec, email_ec, email_validado_ec in data_ec:
            print(f"Nome: {nome_ec} | Idade: {idade_ec} | Email: {email_ec} | Email validado: {email_validado_ec}")
#===========================================================================================================================================================================        
    elif menu == 4:
        sql_re = """
            SELECT usuarios.nome, COUNT(pedidos.id) AS qtd_pedidos, NULLIF('Possui pedidos', CASE WHEN COUNT(pedidos.id) = 0 THEN 'Possui pedidos' ELSE NULL END) AS status
            FROM usuarios
            LEFT JOIN pedidos
            ON usuarios.id = pedidos.usuario_id
            GROUP BY usuarios.nome
            ORDER BY qtd_pedidos DESC
        """
        
        cursor.execute(sql_re)
        data_re = cursor.fetchall()
        
        for nome_re, qtd_pedidos_re, status_re in data_re:
            print(f"Nome: {nome_re} | Quantidade de pedidos: {qtd_pedidos_re} | Status: {status_re}")
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()