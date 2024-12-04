def lerArquivo (nomearq):
    for codficaca in open(nomearq, 'r'):
        codficaca = codficaca.split(';')
        yield codficaca[0], float (codficaca[2])
        #yield codficaca.rstrip()

arquivo = input ("Digite o nome do arquivo: ")
for linha in lerArquivo(arquivo):
    print(linha)
print("FIM")