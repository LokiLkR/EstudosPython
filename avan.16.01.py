def valor_venda(codigo, valcusto):

    def alteraMagem():
        nonlocal margem
        if codigo[0]== '8':
            margem =12/100
        elif codigo[0] == '9':
            margem = 10/100

    margem = 16 / 100
    alteraMagem()
    valVenda = valcusto * (1+ margem)
    return valVenda


Pcusto= 100
codProd = '1280'
pVenda = valor_venda(codProd, Pcusto)
print(f"Produto {codProd}: campra = {Pcusto:.2f}  e venda = {pVenda:.2f}")

codProd = '8280'
pVenda = valor_venda(codProd, Pcusto)
print(f"Produto {codProd}: campra = {Pcusto:.2f}  e venda = {pVenda:.2f}")

codProd = '9280'
pVenda = valor_venda(codProd, Pcusto)
print(f"Produto {codProd}: campra = {Pcusto:.2f}  e venda = {pVenda:.2f}")