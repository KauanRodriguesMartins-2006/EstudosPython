import sqlite3

menu = 10
while True:
    menu = int(input("""
========================
        Aula 03
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
        
        nome = input("Digite um nome: ")
        idade = int(input("Digite a idade: "))
        email = input("Digite o email: ")
        
        sql = """
INSERT INTO usuarios (nome, idade, email)
VALUES (?, ?, ?);      
"""
        cursor.execute(sql, (nome, idade, email))
        
        conexao.commit()
        print("Usuário cadastrado")
        
        cursor.close()
        conexao.close()
    elif menu == 2:
        while True:
            opc = int(input("""
========================
   CADASTRO DE USUÁRIOS
========================

1 - Cadastrar usuário
2 - Sair
                                                      
Opção escolhida: """))
            
            if opc == 1:
                conexao1 = sqlite3.connect("bancos/estudos.db")
                cursor1 = conexao1.cursor()
                        
                nome = input("Digite um nome: ")
                idade = int(input("Digite a idade: "))
                email = input("Digite o email: ")
                        
                sql = """
        INSERT INTO usuarios (nome, idade, email)
        VALUES (?, ?, ?);      
        """
                cursor1.execute(sql, (nome, idade, email))
                        
                conexao1.commit()
                print("Usuário cadastrado")
                        
                cursor1.close()
                conexao1.close()
            
            elif opc == 2:
                print("Retornando ao menu anterior")
                break
            
    elif menu == 3:
        conexao2 = sqlite3.connect("bancos/estudos.db")
        cursor2 = conexao2.cursor()
                                
        nome = input("Digite um nome: ")
        idade = int(input("Digite a idade: "))
        email = input("Digite o email: ")
                                
        sql = """
INSERT INTO usuarios (nome, idade, email)
VALUES (?, ?, ?);      
"""
        cursor2.execute(sql, (nome, idade, email))
                                
        conexao2.commit()
        print("Usuário cadastrado")
        
        cursor2.execute("SELECT * FROM usuarios")
        data = cursor2.fetchall()
        print(data)
             
        cursor2.close()
        conexao2.close()
    elif menu == 4:
        while True:
            opc = int(input("""
========================
   SISTEMA DE USUÁRIOS
========================

1. Cadastrar usuário
2. Listar usuários
3. Sair
                        
Opção escolhida: """))
            
            if opc == 1:
                conexao3 = sqlite3.connect("bancos/estudos.db")
                cursor3 = conexao3.cursor()
                                        
                nome = input("Digite um nome: ")
                idade = int(input("Digite a idade: "))
                email = input("Digite o email: ")
                                        
                sql = """
        INSERT INTO usuarios (nome, idade, email)
        VALUES (?, ?, ?);      
        """
                cursor3.execute(sql, (nome, idade, email))
                                        
                conexao3.commit()
                print("Usuário cadastrado")
                                        
                cursor3.close()
                conexao3.close() 
            
            elif opc == 2:
                conexao4 = sqlite3.connect("bancos/estudos.db")
                cursor4 = conexao4.cursor()
                
                cursor4.execute("SELECT * FROM usuarios")
                data4 = cursor4.fetchall()
                
                print(data4)
                
            elif opc == 3:
                print("Retornando ao menu anterior")
                break
    elif menu == 5:
        print("Encerrando programa")
        break