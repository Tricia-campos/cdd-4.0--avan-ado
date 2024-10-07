def piramide(n):
    for i in range(1,n+1):
        for x in range(i):
            print(i, end=" ")
        print()
def piramide2(n):
    for i in range(n+1):
        for x in range(1,i+1):
            print(x, end=" ")
        print()

def vogais(txt):
    cont = 0
    for x in txt:
        if x in "aeiouAEIOU":
            cont+=1
    print(f"O texto tem {cont} vogais")


def cadastro():
      while True:
            usuario = input("Digite o nome de usuario: ")
            if usuario in usuarios:
                  print("usuario cadastrado")
            else:
                  senha = int(input("Digite a senha numerica:"))
                  usuarios.append(usuario)
                  senhas.append(senha)
                  print("cadastro feito com sucesso")

            dnv = int(input(f"Você deseja cadastrar mais um usuario?\n "
                        f"(1- sim// 2- não) :"))
            if dnv != 1:
                  break

def login():
      while True:
            usuario = input("Digite o nome de usuario: ")
            senha = int(input("Digite a senha numerica:"))
            if usuario in usuarios:
                  indice = usuarios.index(usuario)
                  if senhas[indice] == senha:
                        print(f"Bem-vindo, {usuario}!")
                        break
                  else:
                        print("senha incorreta!")
            else:
                  print("Usuario invalido!")
def mostrar():
    print("Os usuários cadastrados e suas senhas são:")
    for i in range(len(usuarios)):
        print(f"Usuário: {usuarios[i]} - Senha: {senhas[i]}")

def sair():
      print("Finalizando...")

def menu():
      while True:
            print(f" BEM VINDO!!\n"
                  f"DIGITE 1 PARA REALIZAR CADASTRO\n"
                  f"DIGITE 2 PARA FAZER LOGIN\n"
                  f"DIGITE 3 PARA MOSTRAR OS USUARIOS\n"
                  f"DIGITE 4 PARA SAIR\n")

            bv = int(input("Digite a opcão desejada: "))
            if bv ==1:
                  cadastro()
            elif bv == 2:
                  login()
            elif bv == 3:
                  mostrar()
            elif bv == 4:
                  print("finalizando")
                  break
            else:
                  print("invalido")


def inverterNomes(nome1,nome2,nome3,nome4,nome5):
    nomes = [""] * 5
    nomes[0] = nome1
    nomes[1] = nome2
    nomes[2] = nome3
    nomes[3] = nome4
    nomes[4] = nome5
    print(nomes)
    nomes.reverse()
    print(nomes)

def soma(*numeros):
    t= len(numeros)
    soma = 0
    for x in range(t):
        soma = soma + numeros[x]
    print(soma)

