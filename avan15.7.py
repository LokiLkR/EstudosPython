def mediaMovel():
    total = qtde = 0
    while True:
        novodado = (yield total/ qtde if qtde > 0 else  0)
        if novodado is not None:
            total += novodado
            qtde += 1

gen = mediaMovel()
next (gen)
valor= input("Digite um valor ou (FIM para terminar): ")

while valor.upper() != 'FIM':
    resultado = gen.send(float(valor))
    print(f"media movel atual = {resultado:.3f}")
    valor = input("Digite um valor ou (FIM para terminar): ")

print(f"valor Final da Media{resultado:.3f}")

print("FIM")
