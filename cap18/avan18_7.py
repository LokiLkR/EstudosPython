import sqlite3
conector = sqlite3.connect('loja.db')
cursor = conector.cursor()
sqlcont ="""
    select count(codigo) from produto where codigo =?
"""
sqldel= """
    delete from produto where codigo = ?
"""
codigo =input("Digite o codigo a ser excluido: ")
excluidos = []
while codigo.upper()!= 'FIM':
    cursor.execute(sqlcont, [int(codigo)]) #existencia do codigo
    cont= cursor.fetchone()
    if cont[0] ==0:
        print(f" ...Codigo {codigo} não exisste ")
    else:
        cursor.execute(sqldel, [int(codigo)])
        excluidos.append(int(codigo))
        conector.commit()
    codigo = input("Digite o codigo a ser excluido: ")


print("Codigos excluidos")
print(excluidos)

cursor.close()
conector.close()
print("FIM")