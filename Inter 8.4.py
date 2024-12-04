cod= [103,117,121,135,161,189,200,204,216]
lista= []
print (" alternativa com if classico")
for cods in cod:
    if 120 <= cods and cods <=200:
        lista.append(cods)
print(f"Filtraados {lista}")

lista=[]
print("\n\nAkterados linha unica")
for cods in cod:
    lista.append(cods) if 120<= cods and cods <=200 else 0

print(f"Filtraados 2 {lista}")
