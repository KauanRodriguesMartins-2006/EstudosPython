import sqlite3

conexao = sqlite3.connect("bancos/estudos.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco REAL
    )
""")

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))

cursor.execute("""
    INSERT INTO produtos (nome, preco)
    VALUES (?, ?)
""", (nome, preco))

conexao.commit()

cursor.execute("""
    SELECT id, nome, preco
    FROM produtos
    ORDER BY nome
""")

produtos = cursor.fetchall()

for produto in produtos:
    print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2]}")

cursor.execute("SELECT COUNT(*) FROM produtos")
total = cursor.fetchone()[0]

print(f"Total de produtos: {total}")

cursor.close()
conexao.close()