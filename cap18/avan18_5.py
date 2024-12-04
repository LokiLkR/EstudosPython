import sqlite3
conector = sqlite3.connect('loja.db')
cursor = conector.cursor()
sql= """
    alter table produto add custo numeric
"""
cursor.execute(sql)
sql= """
    alter table produto add aliquota numeric
"""
cursor.execute(sql)

sql= """
    alter table produto add Qmin numeric
"""
cursor.execute(sql)

sql="""update produto set custo = 0, aliquota = 0, Qmin = 0
"""
cursor.execute(sql)
conector.commit()

cursor.close()
conector.close()