import sqlite3

menu = 10
while True:
    menu = int(input("""
========================
        Aula 08
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        conexao = sqlite3.connect("bancos/estudos.db")
        cursor = conexao.cursor()
        
        id_Select = int(input("Digite o id de um usuário: "))
        age_change = (int(input("Digite a nova idade do usuário: ")))
        
        sql = """
            UPDATE usuarios
            SET idade = ?
            WHERE id = ?;
        """
        
        cursor.execute(sql, (age_change, id_Select))
        
        conexao.commit()
        print("Idade atualizada")
        
        cursor.close()
        conexao.close()
        
#=========================================================================        
    elif menu == 2:
        conexao1 = sqlite3.connect("bancos/estudos.db")
        cursor1 = conexao1.cursor()
        
        id_Select1 = int(input("Digite o id de um usuário: "))
        name_change = input("Digite o novo nome: ")
        email_change = input("Digite o novo email: ")
        
        sql = """
                    UPDATE usuarios
                    SET nome = ?, email = ?
                    WHERE id = ?;
                """
                
        cursor1.execute(sql, (name_change, email_change, id_Select1))
        
        conexao1.commit()
        print("Informações atualizadas")
        
        cursor1.execute("SELECT * FROM usuarios WHERE id = ?", (id_Select1,))
        data = cursor1.fetchone()
        
        print(data)
        
        cursor1.close()
        conexao1.close()
#=========================================================================        
    elif menu == 3:
        conexao2 = sqlite3.connect("bancos/estudos.db")
        cursor2 = conexao2.cursor()
        
        id_Select2 = int(input("Digite o id de um usuário: "))
        cursor2.execute("SELECT * FROM usuarios WHERE id = ?", (id_Select2,))
        usuario = cursor2.fetchone()
        
        
        
        if usuario:
            print(usuario)

            age_change1 = int(input("Digite a nova idade: "))
            
            sql =  """
                UPDATE usuarios
                SET idade = ?
                WHERE id = ?;
            """
                
            cursor2.execute(sql, (age_change1, id_Select2))
            conexao2.commit()
            print("Idade Atualizada")
            
            selecionar = "SELECT * FROM usuarios WHERE id = ?"
            cursor2.execute(selecionar, (id_Select2,))
            data = cursor2.fetchone() 
            
            print(data)
        else:
            print("Usuário não encontrado")
            
            
            
        cursor2.close()
        conexao2.close()
        
#=========================================================================        
    elif menu == 4:
        conexao3 = sqlite3.connect("bancos/estudos.db")
        cursor3 = conexao3.cursor()
                
        age_add = int(input("Digite quantos anos devem ser adicionados: "))
        
        sql = """
            UPDATE usuarios
            SET idade = idade + ?
        """
        
        cursor3.execute(sql, (age_add,))
        
        cursor3.execute("SELECT * FROM usuarios")
        data1 = cursor3.fetchall()
        
        print(data1)
        conexao3.commit()
        
        cursor3.close()
        conexao3.close()
#=========================================================================      
    elif menu == 5:
        print("Encerrando programa")
        break