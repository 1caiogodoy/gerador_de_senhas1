from flask import Flask, render_template, request
import random
app = Flask(__name__)


def trabalho(quantidade, quantidadeSenha):
    # quantidadeSenha = int(input("Digite quantas senhas deseja: "))
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


@app.route("/", methods=["GET", "POST"],)
def home():
    resultado = None
    if request.method == "POST":
        quantidade = request.form.get("quantidade")
        quantidadeSenha = request.form.get("quantidadeSenha")
        if quantidade and quantidadeSenha:
            quantidade = int(quantidade)
            quantidadeSenha = int(quantidadeSenha)
            resultado = trabalho(quantidade, quantidadeSenha)
    return render_template("home.html", resultado=resultado)


if __name__ == "__main__":  
    app.run(debug=True)