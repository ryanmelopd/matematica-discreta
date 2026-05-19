def sucessor(n):
    return n + 1

def soma(a, b):
    resultado = a
    for i in range(b):
        resultado = sucessor(resultado)
    return resultado

a = int(input("Insira o primeiro número:"))
b = int(input("Insira quantas vezes você quer o sucessor desse número:"))
print(soma(a, b))