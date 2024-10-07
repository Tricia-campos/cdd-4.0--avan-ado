from biblioteca import*

txt=input("Digite um texto:")
cont = 0
for x in txt:
    if x in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
        cont += 1
print(f"O texto tem {cont} letras")

