import json
import os

print("Bem-vindo ao Sistema de Cadastro de Usuários!\n")

provedores = ["@gmail.com", "@hotmail.com", "@yahoo.com", "@outlook.com"]

while True:
    novo_usuario = {
        "Nome": input("Digite o seu nome: "),
        "Idade": int(input("Digite a sua idade: ")),
        "Cidade": input("Digite a sua cidade: "),
        "Estado": input("Digite o seu estado: "),
    }

    while True:
        email = input("Digite o seu E-mail: ")

        if any(email.endswith(p) for p in provedores):
            novo_usuario["Email"] = email
            break
        else:
            print("Provedor inválido! Use gmail, hotmail, yahoo ou outlook.\n")

    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r", encoding="utf-8") as f:
            try:
                usuarios = json.load(f)
            except json.JSONDecodeError:
                usuarios = []
    else:
        usuarios = []

    emails = [u["Email"] for u in usuarios]

    if novo_usuario["Email"] in emails:
        print("Esse email já está cadastrado!")
    else:
        usuarios.append(novo_usuario)
        with open("usuarios.json", "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
        print("Usuário cadastrado com sucesso!")

    resposta = input("Deseja cadastrar outro usuário? (s/n): ").strip().lower()

    if resposta == "s":
        print("Continuando...\n")
    else:
        print("Encerrando...")
        break
