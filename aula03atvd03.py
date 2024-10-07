
num = [""]*10
tam = len(num)
maior = 0
menor = 0
soma= 0
for i in range(tam):
    num[i]= int(input("digite os numeros: "))
    soma = soma + num[i]
for x in range(tam):
    if num[x] %2==0:
        print(num[x], end=" ")
    if num[x] > maior:
        maior = num[x]
        #maior = max(num)
    if num[x] < maior:
        menor = num[x]
        #menor = min(num)
print(f"o menor numero é: {menor}, o maior numero é:{maior}")

media = soma/num[i]
print(media)