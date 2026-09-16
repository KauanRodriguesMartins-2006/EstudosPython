import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 15
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        print("==== Antes ====")
        cursor.execute("SELECT * FROM usuarios")
        data = cursor.fetchall()
                
        for  id_u, nome_u, idade_u, email_u in data:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
            
        sql = """
            UPDATE usuarios
            SET idade = idade + 1
            WHERE id IN (
                SELECT usuario_id
                FROM pedidos
            )
        """
        
        cursor.execute(sql)
        conexao.commit()
        
        cursor.execute("SELECT * FROM usuarios")
        data = cursor.fetchall()
        
        print("\n==== Depois ====")   
        cursor.execute("SELECT * FROM usuarios")
        data = cursor.fetchall() 
        
        for  id_u, nome_u, idade_u, email_u in data:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
#=============================================================================================
    elif menu == 2:
        print("==== Antes ====")
        cursor.execute("SELECT * FROM pedidos")
        data1 = cursor.fetchall()
                        
        for  id_p, usuario_id_p, produto_p in data1:
            print(f"Id: {id_p} | Nome: {usuario_id_p} | Idade: {produto_p}")
            
            
        sql1 = """
            DELETE FROM pedidos
            WHERE pedidos.usuario_id IN (
                SELECT id 
                FROM usuarios
                WHERE idade < 25
            )   
        """
        cursor.execute(sql1)
        conexao.commit()
        
        print("\n==== Depois ====")
        cursor.execute("SELECT * FROM pedidos")
        data1 = cursor.fetchall()
                        
        for  id_p, usuario_id_p, produto_p in data1:
            print(f"Id: {id_p} | Id de usuario: {usuario_id_p} | Idade: {produto_p}")
#=============================================================================================

    elif menu == 3:
        print("==== Antes ====")
        cursor.execute("SELECT * FROM usuarios")
        data = cursor.fetchall()
                        
        for  id_u, nome_u, idade_u, email_u in data:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
            
        nome_produto = input("\nDigite o nome do produto: ").capitalize()
        
        sql2 = """
            UPDATE usuarios
            SET idade = idade + 2
            WHERE id IN (
                SELECT usuario_id
                FROM pedidos
                WHERE produto = ?
            )
        """
        
        cursor.execute(sql2, (nome_produto,))
        conexao.commit()
        
        print("\n==== Depois ====")   
        cursor.execute("SELECT * FROM usuarios")
        data = cursor.fetchall()
        
        for  id_u, nome_u, idade_u, email_u in data:
            print(f"Id: {id_u} | Nome: {nome_u} | Idade: {idade_u} | Email: {email_u}")
        
    elif menu == 4:
        
        print("==== Antes ====")
        cursor.execute("SELECT * FROM pedidos")
        data1 = cursor.fetchall()
                                
        for  id_p, usuario_id_p, produto_p in data1:
            print(f"Id: {id_p} | Nome: {usuario_id_p} | Idade: {produto_p}")
            
        idade_min = int(input("\nDigite a idade minima: "))
            
        sql3 = """
                    DELETE FROM pedidos
                    WHERE pedidos.usuario_id IN (
                        SELECT id 
                        FROM usuarios
                        WHERE idade < ?
                    )   
                """
             
        cursor.execute(sql3, (idade_min,))
        
        print("\n==== Meio ====")
        cursor.execute("SELECT * FROM pedidos")
        data1 = cursor.fetchall()
                                        
        for  id_p, usuario_id_p, produto_p in data1:
            print(f"Id: {id_p} | Nome: {usuario_id_p} | Idade: {produto_p}")
            
        conexao.rollback()
            
        print("\n==== Depois ====")
        cursor.execute("SELECT * FROM pedidos")
        data1 = cursor.fetchall()
                                        
        for  id_p, usuario_id_p, produto_p in data1:
            print(f"Id: {id_p} | Nome: {usuario_id_p} | Idade: {produto_p}")
            
        
        
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()