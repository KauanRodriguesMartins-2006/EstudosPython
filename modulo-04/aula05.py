import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 08
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Sair 
                                   
Opção escolhida: """))
    
    if menu == 1:
        
        
        id_select = int(input("Digite o id do usuario que deseja deletar: "))
        
        cursor.execute("SELECT * FROM usuarios")
        data = cursor.fetchall()
        print(data)
        
        sql_delete = """
            DELETE FROM usuarios WHERE id = ?
        """
        
        cursor.execute(sql_delete, (id_select,))
        print("Usuário deletado")
        
        conexao.commit()
        
        cursor.execute("SELECT * FROM usuarios")
        data1 = cursor.fetchall()
        print(data1)
        
        
        
    elif menu == 2:
        id_select1 = int(input("Digite o id do usuario que deseja deletar: "))
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_select1,))
        usuario = cursor.fetchall()
        
        if usuario:
            cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_select1,))
            status_user = cursor.fetchall()
            
            print(status_user)
            
            sql_delete1 = """
                DELETE FROM usuarios WHERE id = ?
            """
            
            cursor.execute(sql_delete1, (id_select1,))
            print("\nUsuário deletado\n")
            conexao.commit()
            
            cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_select1,))
            status_user = cursor.fetchall()
                        
            print(status_user)
        
        else:
            print("Usuário não encontrado")
            
    elif menu == 3:
        id_ask = int(input("Digite o id do usuario que deseja deletar: "))
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_ask,))
        usuario = cursor.fetchall()
        
        if usuario:
            question = input("Deseja realmente deletar o usuário ? (s/n): ").lower()
            
            if question == 's':
                sql_delete2 = """
                     DELETE FROM usuarios WHERE id = ?
                """
                            
                cursor.execute(sql_delete2, (id_ask,))
                print("\nUsuário deletado\n")
                conexao.commit()
            elif question == 'n':
                print("Exclusão cancelada")
            else:
                print("Opção invalida!")
                
        else:
            print("Usuário não encontrado")
            
    elif menu == 4:
        print("Encerrando programa")
        break
    
cursor.close()
conexao.close()