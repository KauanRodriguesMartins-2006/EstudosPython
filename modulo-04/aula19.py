import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 19
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        sql_dis = """
            SELECT DISTINCT idade 
            FROM usuarios
        """
        
        cursor.execute(sql_dis)
        data_dis = cursor.fetchall()
        
        for idade_d in data_dis:
            print(f"Idades: {idade_d[0]}")
#=============================================================       
    elif menu == 2:
        sql_order = """
            SELECT DISTINCT idade 
            FROM usuarios
            ORDER BY idade ASC
        """
                
        cursor.execute(sql_order)
        data_order = cursor.fetchall()
                
        for idade_o in data_order:
            print(f"Idades: {idade_o[0]}")
#=============================================================
    elif menu == 3:
        sql_dis_double = """
            SELECT DISTINCT idade, email
            FROM usuarios
            ORDER BY idade DESC
        """
        
        cursor.execute(sql_dis_double)
        data_dis_double = cursor.fetchall()
        
        for idade_dd, email_dd in data_dis_double:
            print(f"Idades: {idade_dd} | Email: {email_dd}")
#=============================================================        
    elif menu == 4:
        sql_dis_filter = """
            SELECT DISTINCT idade
            FROM usuarios
            WHERE idade >= 22
            ORDER BY idade DESC
        """
        
        cursor.execute(sql_dis_filter)
        data_dis_filter = cursor.fetchall()
        
        for idade_df in data_dis_filter:
            print(f"Idade: {idade_df[0]}")
        
        
#=============================================================
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()