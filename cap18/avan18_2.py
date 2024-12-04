import sqlite3

conector = sqlite3.connect('loja.db')
cursor = conector.cursor()

try:
    sql = "drop table produto"
    cursor.execute(sql)
except sqlite3.OperationalError:
    pass

sql = """
    create table produto
    (codigo integer, descri text, preço numeric, quant integer)
"""
cursor.execute(sql)

sql= """
    insert into produto (codigo, descri, preço, quant)
    values(?, ?, ?, ?)
"""

nome_arq ="E:\Pycharm\pythonProject\cap18\papelaria.txt"
for linha_arq in open(nome_arq, 'r', encoding = 'utf-8'):
    dados =linha_arq.split(';')
    print(dados)
    cursor.execute(sql, dados)


conector.commit()

cursor.close()
conector.close()

print("FIM")