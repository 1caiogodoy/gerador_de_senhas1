import random
# from main import home()


def trabalho(quantidade):
    quantidadeSenha = int(input("Digite quantas senhas deseja: "))
    quantidadeSenha2 = 0
    senha = ""
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    simbolos = "!@#$%¨&"
    senhas = []
    while quantidadeSenha2 != quantidadeSenha:
        quantidadeSenha2 += 1
        for x in range(quantidade):
            numero = random.randint(0, 9)
            letra = random.choice(letras)
            simbolo = random.choice(simbolos)
            numero = str(numero)
            senha += numero
            if len(senha) == quantidade:
                senhas.append(senha)
            senha += letra
            if len(senha) == quantidade:
                senhas.append(senha)
            senha += simbolo
            if len(senha) == quantidade:
                senhas.append(senha)
        if len(senhas) == quantidadeSenha:
            break
        else:
            senha = ""
    return senhas


print(trabalho(quantidade=int(input(
    "Digite o tamanho da senha que deseja:"""))))
