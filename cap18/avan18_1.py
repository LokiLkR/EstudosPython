import sqlite3

conector = sqlite3.connect('loja.db')
cursor = conector.cursor()

sql = """
    create table produto
    (codigo integer, descri text, preço numeric, quant integer)
"""

cursor.execute(sql)

sql= """
    insert into produto (codigo, descri, preço, quant)
    values(1138, 'lapis preto', 1.90, 376)
"""

cursor.execute(sql)

sql= """
    insert into produto (codigo, descri, preço, quant)
    values(1251, 'papel sulfite A4', 7.20, 188)
"""
cursor.execute(sql)
conector.commit()

cursor.close()
conector.close()

print("FIM")
