def edil(n1, n2, n3, n4, n5):
    lista =[n1, n2, n3, n4, n5]
    minimo = min(lista)
    maximo = max (lista)
    print(f"\no valor maximo e: {maximo}\no valor minimo e: {minimo}")
    soma = lista[0] + lista[1] + lista[2] + lista[3] + lista[4]
    print("a soma e: ", soma)
    media = soma/5
    return media

n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))
n3 = int(input("digite o terceiro numero: "))
n4 = int(input("digite o quarto numero: "))
n5 = int(input("digite o quinto numero: "))

lista =[n1, n2, n3, n4, n5]
edy = edil(n1, n2, n3, n4, n5)
print("a media e: ", edy)
edi = edy *5
print(f"{edy} x 5 = {edi}")