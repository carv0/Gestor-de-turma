# Gestor de disciplina de uma turma

# Listas e variáveis
nomes = []
notas1p = []
notas2p = []
notas3p = []
mediafinal = []
pos = 0
maior = 0

# Inicio do programa na tela
print("PROGRAMA PARA GERIR UMA TURMA.")
num_alunos = eval(input("\n Introduza o número de alunos: "))

# Adição de valores às listas
for i in range(num_alunos):
    nomes.append(input("\nIndique o nome do aluno: "))
    notas1p.append(eval(input("Indique a nota de " + nomes[i] + " no 1º período: ")))
    notas2p.append(eval(input("Indique a nota de " + nomes[i] + " no 2º período: ")))
    notas3p.append(eval(input("Indique a nota de " + nomes[i] + " no 3º período: ")))

# Médias de cada período
print("\n- MÉDIA DE CADA PERÍODO: ")


def calcula_media(alunos):
    soma = 0
    for i in range(len(alunos)):
        soma = soma + alunos[i]
    media = soma / len(alunos)
    return media


print("1º Período: ", calcula_media(notas1p))
print("2º Período: ", calcula_media(notas2p))
print("3º Período: ", calcula_media(notas3p))

# Classificação final do ano (média dos 3 períodos)
print("\n- CLASSIFICAÇÃO FINAL (média dos 3 períodos): ")
mediaf = (calcula_media(notas1p) + calcula_media(notas2p) + calcula_media(notas3p)) / 3
print("A média final é ", mediaf)

# Melhor(es) aluno(s) de cada período e respetiva nota:
print("\n-MELHORES ALUNOS DE CADA PERÍODO: ")

# 1º Período
for i in range(num_alunos):
    if notas1p[i] > maior:
        maior = notas1p[i]
        pos = i
print("No 1º período:", nomes[pos], "teve", maior, ".")

# 2º Período
for j in range(num_alunos):
    if notas2p[j] > maior:
        maior = notas2p[j]
        pos = j
print("No 2º período:", nomes[pos], "teve", maior, ".")

# 3º Período
for k in range(num_alunos):
    if notas3p[k] > maior:
        maior = notas3p[k]
        pos = k
print("No 3º período:", nomes[pos], "teve", maior, ".")

# Melhores alunos do ano e suas notas
print("\n-MELHOR ALUNO DA TURMA:")
for i in range(num_alunos):
    mediafinal.append((notas1p[i] + notas2p[i] + notas3p[i]) / 3)
    if mediafinal[i] > mediaf:
        pos = i
print("Parabéns", nomes[pos], "tiveste", mediafinal[pos], "e foste o melhor aluno da turma.")

# Ordem crescente de notas os nomes dos alunos e respetivas notas finais de ano
print("\n-NOMES E RESPETIVAS NOTAS POR ORDEM CRESCENTE")
for i in range(num_alunos):
    mediafinal.sort()
    print(nomes[i],"teve", mediafinal[i])

print("\n:)")
