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
        Aula 06
========================    

1. Exercicio 1
2. Exercicio 2
3. Exercicio 3
4. Sair
                                   
Opção escolhida: """))
    
    if menu == 1:
        usuarios = sessao.get(Url)
        user = usuarios.json()
        
        cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios_api(
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT
)               
""")
        
        for i in user:
            sql = """
INSERT INTO usuarios_api (id, nome, email)
VALUES(?, ?, ?);
            """
            cursor.execute(sql, (i['id'], i['name'], i['email']))
            
        conexao.commit()
        print("Usuários cadastrados")
        cursor.execute("SELECT * FROM usuarios_api ")
        data = cursor.fetchall()
        print(data)

#======================================================================================
    elif menu == 2:
        usuarios = sessao.get(Url)
        user = usuarios.json()

        for i in user:
            cursor.execute("SELECT id FROM usuarios_api WHERE id = ?", (i['id'],))
            existe = cursor.fetchone()

            if existe is None:
                sql = """
                INSERT INTO usuarios_api (id, nome, email)
                VALUES (?, ?, ?);
                """
                cursor.execute(sql, (i['id'], i['name'], i['email']))
                print(f"Usuário {i['name']} inserido")
            else:
                print(f"Usuário {i['name']} já existe, pulando")

        conexao.commit()
        print("Processo finalizado")
#===========================================================================================
    elif menu == 3:
        getUser = sessao.get(Url)
        gu = getUser.json()
        
        cont_insert_users = 0
        cont_updated_users = 0
        cont_noUp_users = 0
        
        for i in gu:
            cursor.execute("SELECT id FROM usuarios_api WHERE id = ?", (i['id'],))
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
                cursor.execute("SELECT email FROM usuarios_api WHERE id = ?", (i['id'],))
                email_check = cursor.fetchone()
                
                if email_check[0] == i['email']:
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
                
    elif menu == 4:
        print("Encerrando programa")
        break
    
cursor.close()
conexao.close()