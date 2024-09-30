nota =["","","","",""]
tam = len(nota)
soma = 0
cont = 0
for i in range(tam):
    nota[i] = float(input("Digite a nota: "))

for x in range(tam):
    soma += nota[x]
media = soma/tam

for z in range(tam):
   if nota[z] >= media:
       cont +=1

print(f" temos {cont} alunos com nota maior que a media {media}")