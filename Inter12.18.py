def calcMedia (pnotas): #str que vai receber 4 notas
    pnotas = pnotas.split() #retorno do split eh uma lista
    for i in range (len(pnotas)):
        pnotas[i] = float(pnotas[i])
    media = (pnotas[0]+ pnotas[1]+ pnotas[2]) *0.3 +pnotas[3]*0.1
    situacao ='APROVADO' if media >=7 else "REPROVCADO"
    pnotas.append(media)
    pnotas.append(situacao)
    return pnotas

notas =input ("Digita as 4 notas (P1 P2 P3 NT): ")
resultado = calcMedia(notas)
print(f'P1 {resultado [0]:.1f}; ', end ='')
print(f'P2 {resultado [1]:.1f}; ', end ='')
print(f'P3 {resultado [2]:.1f}; ', end ='')
print(f'NT {resultado [3]:.1f} - > ', end ='')
print(f'Media {resultado [4]:.1f} ', end ='')
print(f'Situação {resultado [5]}')



