import sqlite3
conector = sqlite3.connect('loja.db')
cursor = conector.cursor()
sql= """
    update produto
        set custo = ?, aliquota = ?, Qmin = ?
        where codigo = ?
"""

for linha_arq in open ('papelaria Up.txt',  encoding= 'utf-8'):
    dados = linha_arq.split(';')
    dados.append(dados[0])
    del (dados [0])
    print(dados)
    cursor.execute(sql, dados)
conector.commit()

print("tabala atualizada")
cursor.close()
conector.close()
print('FIM')