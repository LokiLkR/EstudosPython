import sqlite3
conector = sqlite3.connect('loja.db')
cursor = conector.cursor()
sql= """
    insert into produto (codigo, descri, preço, quant)
    values (?, ?, ?, ?)
"""
print("Digite os dados")
print("Codigo, Descrição, Preço, Estoque")
ler = input()
while ler != '':
    try:
        dados = ler.split(',')
        print(dados)
        cursor.execute(sql, dados)
        conector.commit()
    except sqlite3.OperationalError as e:
        print(e.sqlite_errorname)
        print(f"{dados} Dados Invalidos")
    else:
        (' '*10,' ... dados inseridos com sucesso')
    finally:
        print('\nCodigo, Descrição, Preço, Estoque')
    ler = input()


cursor.close()
conector.close()

