import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 11
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        cursor.execute("SELECT idade, COUNT(*) as quantidade FROM usuarios GROUP BY idade")
        data = cursor.fetchall()
        
        for idade_u, quantidade in data:
            print(f"Idade: {idade_u} | Quantidade: {quantidade}")
#====================================================================================================================================            
    elif menu == 2:
        cursor.execute("SELECT idade, COUNT(*) as quantidade FROM usuarios GROUP BY idade HAVING COUNT(*) > 1")
        data1 = cursor.fetchall()
                
        for idade_u, quantidade in data1:
            print(f"Idade: {idade_u} | Quantidade: {quantidade}")
#====================================================================================================================================            
    elif menu == 3:
        cursor.execute("SELECT idade, COUNT(*) as quantidade FROM usuarios GROUP BY idade ORDER BY idade DESC")
        data2 = cursor.fetchall()
                
        for idade_u, quantidade in data2:
            print(f"Idade: {idade_u} | Quantidade: {quantidade}")
#====================================================================================================================================
    elif menu == 4:
        while True:
            opc = int(input("""
=======================
    Grupos de idade       
=======================
1. 19 a 24 anos
2. 25 a 29 anos
3. 30+ anos
4. Retornar
      
Opção escolhida: """))
            if opc == 1:
                cursor.execute("""SELECT idade, COUNT(*) as quantidade FROM usuarios WHERE idade >= 19 
                               and idade < 25 GROUP BY idade ORDER BY idade DESC""")
                group_age1 = cursor.fetchall()
                                
                for idade_u, quantidade in group_age1:
                    print(f"Idade: {idade_u} | Quantidade: {quantidade}")
            
            elif opc == 2:
                cursor.execute("""SELECT idade, COUNT(*) as quantidade FROM usuarios WHERE idade >= 25 
                               and idade < 30 GROUP BY idade ORDER BY idade DESC""")
                group_age2 = cursor.fetchall()
                                                
                for idade_u, quantidade in group_age2:
                    print(f"Idade: {idade_u} | Quantidade: {quantidade}")
                    
            elif opc == 3:
                cursor.execute("""SELECT idade, COUNT(*) as quantidade FROM usuarios WHERE idade >= 30
                               GROUP BY idade ORDER BY idade DESC""")
                group_age3 = cursor.fetchall()
                                                                
                for idade_u, quantidade in group_age3:
                    print(f"Idade: {idade_u} | Quantidade: {quantidade}")
                    
            elif opc == 4:
                print("Retornando ao menu anterior")
                break          
#====================================================================================================================================    
    elif menu == 5:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()