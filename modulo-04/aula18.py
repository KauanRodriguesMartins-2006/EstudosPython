import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 18
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        sql_union_simple = """
           SELECT nome 
           FROM usuarios
           WHERE idade < 25
           
           UNION
           
           SELECT nome 
           FROM usuarios
           WHERE idade >= 30
        """
        
        cursor.execute(sql_union_simple)
        data_union = cursor.fetchall()
        
        for nome_u in data_union:
            print(f"Nome: {nome_u[0]}")
#==================================================================       
    elif menu == 2:
        sql_union_double = """
            SELECT nome, 'Menor de 25' AS categoria
            FROM usuarios
            WHERE idade < 25
            
            UNION ALL
            
            SELECT nome, '25 ou mais' AS categoria
            FROM usuarios
            WHERE idade >= 25
        """
        
        cursor.execute(sql_union_double)
        data_unionD = cursor.fetchall()
        
        for nome_ud, categoria_ud in data_unionD:
            print(f"Nome: {nome_ud} | Categoria: {categoria_ud}")
#==================================================================
    elif menu == 3:
        sql_union_join = """
            SELECT nome AS informacao
            FROM usuarios
            
            UNION
            
            SELECT produto AS informacao
            FROM pedidos
        """
        
        cursor.execute(sql_union_join)
        data_unionJ = cursor.fetchall()
        
        for informacao in data_unionJ:
            print(f"Informação: {informacao[0]}") 
        
    elif menu == 4:
        sql_union_filter = """
            SELECT nome 
            FROM usuarios
            WHERE idade < 25
            
            UNION
            
            SELECT nome
            FROM usuarios
            WHERE nome LIKE 'M%'
        """
        
        cursor.execute(sql_union_filter)
        data_unionF = cursor.fetchall()
        
        for nome_f in data_unionF:
            print(f"Nome: {nome_f[0]}")
        
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()