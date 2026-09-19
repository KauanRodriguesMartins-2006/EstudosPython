import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 17
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        sql = """
             EXPLAIN QUERY PLAN
             SELECT * FROM usuarios
             WHERE nome = 'Maria'
        """
        
        cursor.execute(sql)
        data = cursor.fetchall()
        
        for linha in data:
            print(linha)
#===================================================================    
    elif menu == 2:
        cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_usuario_nome
    on usuarios(nome)                    
""")
        
        sql1 = """
                EXPLAIN QUERY PLAN
                SELECT * FROM usuarios
                WHERE nome = 'Maria'
        """
                
        cursor.execute(sql1)
        data1 = cursor.fetchall()

        for linha in data1:
            print(linha)
#===================================================================
    elif menu == 3:
        cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_usuario_idade
    on usuarios(idade)                    
""")
        
        sql2 = """
            EXPLAIN QUERY PLAN
            SELECT * FROM usuarios
            WHERE idade >= ?
        """
        sql_2 = """
            SELECT * FROM usuarios
            WHERE idade >= ?
        """
        
        cursor.execute(sql2, (25,))
        data2 = cursor.fetchall()
        
        cursor.execute(sql_2, (25,))
        data_2 = cursor.fetchall()
        
        
        for linha in data2:
            print(linha)
            
        for id_u, nome_u, idade_u, email_u in data_2:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
    elif menu == 4:
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_usuario_email
            on usuarios(email)                    
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_nome_like
            on usuarios(nome)                    
        """)
        
        # Consulta A
        print("CONSULTA A")
        email_search = input("Digite o email exato de quem procura: ")
        
        sql_a = """
            EXPLAIN QUERY PLAN
            SELECT * FROM usuarios
            WHERE email = ?
        """
        cursor.execute(sql_a, (email_search,))
        data_a = cursor.fetchall()
        
        for linha in data_a:
            print("\n",linha)
        
        sql_a1 = """
            SELECT * FROM usuarios
            WHERE email = ?
        """
        cursor.execute(sql_a1, (email_search,))
        data_a1 = cursor.fetchall()
        
        for id_a, nome_a, idade_a, email_a in data_a1:
            print(f"Id: {id_a} | Nome: {nome_a} | Idade: {idade_a} | Email: {email_a}")
            
        # Consulta B
        print("\nCONSULTA B")
        
        nome_patch = input("Digite uma letra de um nome: ")
        
        sql_b = """
            EXPLAIN QUERY PLAN
            SELECT * FROM usuarios
            WHERE nome LIKE ?
        """
        
        cursor.execute(sql_b, (f'%{nome_patch}%',))
        data_b = cursor.fetchall()
        
        for linha_b in data_b:
            print("\n",linha_b)
            
        sql_b1 = """
            SELECT * FROM usuarios
            WHERE nome LIKE ?
        """
        
        cursor.execute(sql_b1, (f'%{nome_patch}%',))
        data_b1 = cursor.fetchall()
        
        for id_b, nome_b, idade_b, email_b in data_b1:
            print(f"\nId: {id_b} | Nome: {nome_b} | Idade: {idade_b} | Email: {email_b}")
         
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()