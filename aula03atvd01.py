n = [""]*10
tam =len(n)

cont = 0
for j in range(tam):
    n[j] = int(input("Digite um numero: "))
num = int(input("Digite um número para pesquisar: "))

for z in range(tam):
    if n[z]== num:
        cont+=1

print(cont)
