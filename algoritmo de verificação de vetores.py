vetor1 = []
vetor2 = []

quantidade_de_valores_v1 = int(input("Insira a quantidade de valores do primeiro vetor: "))
quantidade_de_valores_v2 = int(input("Insira a quantidade de valores do segundo vetor: "))

for i in range(quantidade_de_valores_v1):
    a = int(input("Insira os valores para o primeiro vetor:"))
    vetor1.append(a)
        
for j in range(quantidade_de_valores_v2):
    b = int(input("Insira os valores para o segundo vetor:"))
    vetor2.append(b)

vetores_iguais = True

if len(vetor1) != len(vetor2):
    vetores_iguais = False

else:
    for i in vetor1:
        if i not in vetor2:
            vetores_iguais = False
            break

if vetores_iguais == True:
    print("Vetores iguais")

else:
    print("Vetores diferentes")