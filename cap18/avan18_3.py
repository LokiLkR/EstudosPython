import sqlite3
conector = sqlite3.connect('loja.db')
cursor = conector.cursor()
sql= """select * from produto
      where preço < 5.00
      order by preço desc"""
cursor.execute(sql)
dados = cursor.fetchall()
cursor.close()
conector.close()

print("\nColsuta 'loja.db'")
print("Dados da Tabela Produto")
print("-"*65)
print('{:<7}{:40}{:>8}{:>6}'.format('Codigo','Descrição','Preço',' Estoque'))
print("-"*31)
for d in dados:
    print(f"{d[0]:<7}{d[1]:40}{d[2]:8.2f}{d[3]:6}") #eu não seiiiiiiiiii
print("-"*65)

print("Encontrados {} registros".format(len(dados)))
print("-"*65)



print("FIM")
