usuario = [""]*5
senha = [""]*5
tam = len(usuario)
for x in range(tam):
    usuario[x] = input("Digite o nome de usuario: ")
    senha[x] = int(input("Digite a senha numerica:"))

for y in range(tam):
    print(f"Na posição: {y} - Usuario: {usuario[y]} Senha:{senha[y]}")
