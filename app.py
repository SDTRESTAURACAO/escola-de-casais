from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os

app = Flask(__name__)
app.secret_key = "chave_secreta"

DADOS_JSON = "dados.json"

# Função para carregar os dados
def carregar_dados():
    if not os.path.exists(DADOS_JSON):
        return []
    with open(DADOS_JSON, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.decoder.JSONDecodeError:
            return []

# Função para salvar os dados
def salvar_dados(dados):
    with open(DADOS_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Rota da tela de cadastro
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome1 = request.form["nome1"]
        nome2 = request.form["nome2"]
        telefone = request.form["telefone"]

        dados = carregar_dados()
        dados.append({"nome1": nome1, "nome2": nome2, "telefone": telefone, "presencas": 0})
        salvar_dados(dados)

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for("index"))

    return render_template("index.html")

# Rota da tela de presença
@app.route("/presenca", methods=["GET", "POST"])
def presenca():
    if request.method == "POST":
        telefone = request.form["telefone"]
        dados = carregar_dados()

        for casal in dados:
            if casal["telefone"] == telefone:
                casal["presencas"] += 1
                salvar_dados(dados)
                flash("Presença registrada com sucesso!", "success")
                return redirect(url_for("presenca"))

        flash("FAÇA PRIMEIRO SEU CADASTRO", "danger")

    return render_template("presenca.html")

# Rota para login de administrador
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "ZEJUNIOADM" and senha == "SDTR01":
            session["admin"] = True
            return redirect(url_for("admin"))

        flash("Login inválido!", "danger")

    return render_template("login.html")

# Rota da área administrativa
@app.route("/admin")
def admin():
    if not session.get("admin"):
        return redirect(url_for("login"))

    dados = carregar_dados()
    return render_template("admin.html", casais=dados)

# Rota para logout do administrador
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


app = Flask(__name__)
app.secret_key = "chave_secreta"

DADOS_JSON = "dados.json"

# Função para carregar os dados
def carregar_dados():
    if not os.path.exists(DADOS_JSON):
        return []
    with open(DADOS_JSON, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.decoder.JSONDecodeError:
            return []

# Função para salvar os dados
def salvar_dados(dados):
    with open(DADOS_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Rota da tela de cadastro
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome1 = request.form["nome1"]
        nome2 = request.form["nome2"]
        telefone = request.form["telefone"]

        dados = carregar_dados()
        dados.append({"nome1": nome1, "nome2": nome2, "telefone": telefone, "presencas": 0})
        salvar_dados(dados)

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for("index"))

    return render_template("index.html")

# Rota da tela de presença
@app.route("/presenca", methods=["GET", "POST"])
def presenca():
    if request.method == "POST":
        telefone = request.form["telefone"]
        dados = carregar_dados()

        for casal in dados:
            if casal["telefone"] == telefone:
                casal["presencas"] += 1
                salvar_dados(dados)
                flash("Presença registrada com sucesso!", "success")
                return redirect(url_for("presenca"))

        flash("FAÇA PRIMEIRO SEU CADASTRO", "danger")

    return render_template("presenca.html")

# Rota para login de administrador
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "ZEJUNIOADM" and senha == "SDTR01":
            session["admin"] = True
            return redirect(url_for("admin"))

        flash("Login inválido!", "danger")

    return render_template("login.html")

# Rota da área administrativa
@app.route("/admin")
def admin():
    if not session.get("admin"):
        return redirect(url_for("login"))

    dados = carregar_dados()
    return render_template("admin.html", casais=dados)

# Rota para logout do administrador
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
