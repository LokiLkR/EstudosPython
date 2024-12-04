codGrav=input("Digite Gravação: ")
codLeit=input("Digite a Leitura: ")

print("--Etapa de Gravação--")
arq = open('codificacao.txt', 'w', encoding=codGrav)
arq.write("Gravaçã de Arquivo\n")
arq.write("acentos: á, é, í, Á, É, Í, ç, Ç\n")
arq.close()

print("\n--Etapa de Leitura do Arquivo--")

arq = open('codificacao.txt', 'r', encoding=codLeit)
s= arq.readline()
print(s.rstrip())
s=arq.readline()
print(s.rstrip())
arq.close()

print("--FIM--")
