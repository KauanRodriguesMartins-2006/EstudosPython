import sqlite3

conexao = sqlite3.connect("../bancos/estudos.db")
cursor = conexao.cursor()
menu = 10
while True:
    menu = int(input("""
========================
        Desafio
========================    

1. Cadastro de tarefa
2. Listar tarefas
3. Listar tarefas de determinada prioridade
4. Marcar como concluída
5. Mostrar tarefas total
6. Quantas tarefas ativas x concluidas
7. Sair
                                   
Opção escolhida: """))
    
    if menu == 1:
        cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY,
    titulo TEXT,
    descricao TEXT,
    prioridade TEXT,
    status TEXT
    )            
""")
        titulo = input("Digite o titulo da tarefa: ")
        descricao = input("Digite a descriçao da tarefa: ")
        prioridade = input("Digite a prioridade da tarefa (baixa, media ou alta): ").upper()
        status = 'ATIVA'
        
        cursor.execute("""
    INSERT INTO tarefas (titulo, descricao, prioridade, status)
    VALUES (?, ?, ?, ?)
""", (titulo, descricao, prioridade, status))
        
        print("Tarefa cadastrada")
        
        conexao.commit()
#===================================================================================================
    elif menu == 2:
        cursor.execute("SELECT * FROM tarefas")
        data = cursor.fetchall()
        
        for id_t, titulo_t, descricao_t, prioridade_t, status_t in data:
            print(f"Id: {id_t} | Título: {titulo_t} | Descrição: {descricao_t} | Prioridade: {prioridade_t} | Status: {status_t} ")
#=====================================================================================================
    elif menu == 3:
        opc = int(input("""
============================
    Lista de prioridades
============================   

1. Baixa
2. Média
3. Alta
                               
Opção escolhida: """))
        
        if opc == 1:
            cursor.execute("SELECT * FROM tarefas WHERE prioridade = 'BAIXA'")
            data1 = cursor.fetchall()
            
            for id_t, titulo_t, descricao_t, prioridade_t, status_t in data1:
                print(f"Id: {id_t} | Título: {titulo_t} | Descrição: {descricao_t} | Prioridade: {prioridade_t} | Status: {status_t} ")
                
        elif opc == 2:
            cursor.execute("SELECT * FROM tarefas WHERE prioridade = 'MEDIA'")
            data2 = cursor.fetchall()
                        
            for id_t, titulo_t, descricao_t, prioridade_t, status_t in data2:
                print(f"Id: {id_t} | Título: {titulo_t} | Descrição: {descricao_t} | Prioridade: {prioridade_t} | Status: {status_t} ")
        elif opc == 3:
            cursor.execute("SELECT * FROM tarefas WHERE prioridade = 'ALTA'")
            data3 = cursor.fetchall()
                        
            for id_t, titulo_t, descricao_t, prioridade_t, status_t in data3:
                print(f"Id: {id_t} | Título: {titulo_t} | Descrição: {descricao_t} | Prioridade: {prioridade_t} | Status: {status_t} ")
    elif menu == 4:
        id_tarefa = int(input("Digite o id da tarefa a ser marcada como concluida: "))
        
        
        sql_update_status = """
            UPDATE tarefas
            SET status = 'CONCLUIDA'
            WHERE id = ?
        """
        
        cursor.execute(sql_update_status, (id_tarefa,))
        conexao.commit()
        
    elif menu == 5:
        cursor.execute("SELECT COUNT(*) FROM tarefas")
        quantidade = cursor.fetchone()[0]
        
        print(f"Quantidade total de tarefas {quantidade}")
    elif menu == 6:
        cursor.execute("SELECT COUNT(*) FROM tarefas WHERE status = 'ATIVA'")
        quantidade_ativa = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM tarefas WHERE status = 'CONCLUIDA'")
        quantidade_concluida = cursor.fetchone()[0]
        
        print(f"Quantidade de tarefas ativas: {quantidade_ativa} | Quantidade de tarefas concluidas: {quantidade_concluida}")
    elif menu == 7:
        print("Encerrando programa")
        break

cursor.close()
conexao.close()