a = [0,0,0,0,0,0,0,0,0,0]
x = 0
m = [0,0,0,0,0,0,0,0,0,0]
tam = len(a)

for j in range(tam):
    a[j] = int(input("Digite um numero: "))

x =int(input("Digite o multiplicador: "))

for i in range(tam):
    m[i]=a[i]*x

print(a)
print(x)
print(m)