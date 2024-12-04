def soma(*args):
    r=0
    for x in args:
        r+=x
    return r

def multi(*args):
    r =1
    for  x in args:
        r*=x
    return r

if __name__ == '__main__':
    print("Incio do Modulo")