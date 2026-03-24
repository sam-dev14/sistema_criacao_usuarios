import json

print("-- Verificador de Usuários --")

with open("usuarios.json", "r", encoding="utf-8") as f:
    usuarios = json.load(f)

print(f"Total de usuários: {len(usuarios)}\n")

for usuario in usuarios:
    print("----------------------------")
    print(f"Nome:   {usuario['Nome']}")
    print(f"Email:  {usuario['Email']}")
    print(f"Idade:  {usuario['Idade']}")
    print(f"Cidade: {usuario['Cidade']}")
    print(f"Estado: {usuario['Estado']}")
    print("----------------------------\n")
