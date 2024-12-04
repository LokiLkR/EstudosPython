n =-1
while n != 0:
    n = int(input("Digiite um inteiro: "))
    match n:
        case 1:
            print (" voce digitou 1")
        case 2:
            print(" voce digitou 2")
        case 3:
            print(" voce digitou 3")
        case _:
            print(" voce opa")