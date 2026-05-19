vetor1 = [1,2,3,4,5,6]
vetor2 = [2,4,6]

vetoresIguais = True

if len(vetor1) != len(vetor2):
    vetoresIguais = False

else:
    for i in vetor1:
        if i not in vetor2:
            vetoresIguais = False
            break

if vetoresIguais == True:
    print("Vetores iguais")

else:
    print("Vetores diferentes")