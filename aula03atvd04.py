from biblioteca import*

txt=input("Digite um texto:")
cont = 0
tam = len(txt)
for x in txt:
    if x in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
        cont += 1
print(f"O texto tem {cont} letras")

for i in range(tam-1,-1,-1):
    print(txt[i],end=" ")
