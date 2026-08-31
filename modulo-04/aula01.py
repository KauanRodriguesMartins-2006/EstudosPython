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
        print("Conexão on")
        conexao.close()
        print("Conexão off")
        
    elif menu == 2:
        conexao1 = sqlite3.connect("bancos/estudos.db")
        cursor = conexao1.cursor()
        print("Cursor criado")
        conexao1.close()
        print("Conexão off")
        
    elif menu == 3:
        conexao2 = sqlite3.connect("bancos/estudos.db")
        cursor1 = conexao2.cursor()
        
        cursor1.execute("""
CREATE TABLE usuarios (
id INTEGER PRIMARY KEY,
nome TEXT,
idade INTEGER,
email TEXT
)   
""")
        
        cursor1.executescript("""
INSERT INTO usuarios (nome, idade, email)
VALUES ('Maria', 18, 'maria@gmail.com');

INSERT INTO usuarios (nome, idade, email)
VALUES ('João', 19, 'joao@gmail.com');

INSERT INTO usuarios (nome, idade, email)
VALUES ('Pedro', 20, 'pedro@gmail.com');
""")
        
        conexao2.commit()
        
        cursor1.close()
        conexao2.close()
        
        print("Conexão off")
        
    elif menu == 5:
        print("Encerrando programa")
        break
