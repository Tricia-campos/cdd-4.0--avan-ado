#FUNÇAO-- exemplo
##def imp_nome(nome):
 #   print(f"Nome:{nome}")
#imp_nome("Danile")
#imp_nome("Dan")
#imp_nome("Dani")


def inverter(n):
    for i in range(1,num+1):
        for x in range(i):
            print(i, end=" ")
        print()
num = int(input("digite um numero: "))
inverter(num)