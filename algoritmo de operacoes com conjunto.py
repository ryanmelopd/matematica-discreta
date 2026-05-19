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

uniao = []

for i in vetor1:
    if i not in uniao:
        uniao.append(i)

for i in vetor2:
    if i not in uniao:
        uniao.append(i)

print("União:", uniao)

intersecao = []

for i in vetor1:
    if i in vetor2 and i not in intersecao:
        intersecao.append(i)

print("Interseção:", intersecao)

diferenca = []

for i in vetor1:
    if i not in vetor2:
        diferenca.append(i)

print("Diferença:", diferenca)

diferenca_simetrica = []

for i in vetor1:
    if i not in vetor2:
        diferenca_simetrica.append(i)

for i in vetor2:
    if i not in vetor1:
        diferenca_simetrica.append(i)

print("Diferença Simétrica:", diferenca_simetrica)