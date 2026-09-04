import sqlite3

import requests

Url = 'https://jsonplaceholder.typicode.com/users'

sessao = requests.Session()
sessao.headers.update({
    "Accept": "application/json"
})

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Aula 07
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Desafio  
5. Sair  
                                   
Opção escolhida: """))
    
    if menu == 1:
        getUser = sessao.get(Url)
        gu = getUser.json()
                
        cont_insert_users = 0
        cont_updated_users = 0
        cont_noUp_users = 0
                
        for i in gu:
            cursor.execute("SELECT id, email FROM usuarios_api WHERE id = ?", (i['id'],))
            existe = cursor.fetchone()
                    
            if existe is None:
                cont_insert_users += 1
                sql = """
                INSERT INTO usuarios_api (id, nome, email)
                VALUES (?, ?, ?);
                """
                cursor.execute(sql, (i['id'], i['name'], i['email']))
                print(f"Usuário {i['name']} inserido")
            else:
                        
                if existe[1] == i['email']:
                    cont_noUp_users += 1
                    print("Emails estão corretos")
                else:
                    cont_updated_users += 1
                    sql1 = """
                        UPDATE usuarios_api
                        SET email = ?
                        WHERE id = ?
                    """
                            
                    cursor.execute(sql1, (i['email'], i['id']))
                            
        conexao.commit()  
        print(f"""
Usuários inseridos: {cont_insert_users}
Usuários atualizados: {cont_updated_users}
Usuários sem alteração: {cont_noUp_users}
""")
#=====================================================================================       
    elif menu == 2:
        getUser = sessao.get(Url)
        gu = getUser.json()
                        
        cont_insert_users = 0
        cont_updated_users = 0
        cont_noUp_users = 0
                        
        for i in gu:
            cursor.execute("SELECT id, nome, email FROM usuarios_api WHERE id = ?", (i['id'],))
            existe = cursor.fetchone()
                            
            if existe is None:
                cont_insert_users += 1
                sql = """
                INSERT INTO usuarios_api (id, nome, email)
                VALUES (?, ?, ?);
                """
                cursor.execute(sql, (i['id'], i['name'], i['email']))
                print(f"Usuário {i['name']} inserido")
            else:
                                
                if existe[1] == i['name'] and existe[2] == i['email']:
                    cont_noUp_users += 1
                    print("Emails e nomes estão corretos")
                else:
                    cont_updated_users += 1
                    sql1 = """
                        UPDATE usuarios_api
                        SET email = ?, nome = ?
                        WHERE id = ?
                    """
                    print("Usuário(s) atualizado(s)")
                                    
                    cursor.execute(sql1, (i['email'], i['name'], i['id']))
                                    
        conexao.commit()  
        print(f"""
Usuários inseridos: {cont_insert_users}
Usuários atualizados: {cont_updated_users}
Usuários sem alteração: {cont_noUp_users}
""")
#=====================================================================================
    elif menu == 3:
        id_select = int(input("Digite o id do usuário que deseja atualizar: "))
        param = {
            'id': id_select
        }
        
        getUser = sessao.get(Url, params= param)
        gu = getUser.json()
                                
        cont_insert_users = 0
        cont_updated_users = 0
        cont_noUp_users = 0
                                
        for i in gu:
            cursor.execute("SELECT id, nome, email FROM usuarios_api WHERE id = ?", (i['id'],))
            existe = cursor.fetchone()
                                    
            if existe is None:
                cont_insert_users += 1
                sql = """
                INSERT INTO usuarios_api (id, nome, email)
                VALUES (?, ?, ?);
                """
                cursor.execute(sql, (i['id'], i['name'], i['email']))
                print(f"Usuário {i['name']} inserido")
            else:
                                        
                if existe[1] == i['name'] and existe[2] == i['email']:
                    cont_noUp_users += 1
                    print("Emails e nomes estão corretos")
                else:
                    cont_updated_users += 1
                    sql1 = """
                        UPDATE usuarios_api
                        SET email = ?, nome = ?
                        WHERE id = ?
                    """
                    print("Usuário(s) atualizado(s)")
                                            
                    cursor.execute(sql1, (i['email'], i['name'], i['id']))
                                            
        conexao.commit()  
        print(f"""
Usuários inseridos: {cont_insert_users}
Usuários atualizados: {cont_updated_users}
Usuários sem alteração: {cont_noUp_users}
""")
    elif menu == 4:
        cursor.execute("SELECT COUNT(*) FROM usuarios_api")
        total = cursor.fetchone()[0]
        
        cursor.execute("SELECT id, nome, email FROM usuarios_api")
        existe = cursor.fetchall()
        
        if existe:
            print(f"""
Quantidade de ususários: {total}
Usuários: {existe} |
""")
        else:
            print("Nenhum registro encontrado")
        
    elif menu == 5:
        print("Encerrando programa")
        break
    
    
cursor.close()
cursor.close()