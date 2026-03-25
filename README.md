# Sistema de Cadastro de Usuários.

Projeto em Python para cadastrar e visualizar usuários via terminal, salvando os dados em um arquivo JSON.

---

## Arquivos

| Arquivo                   | Descrição                                                  |
| ------------------------- | ---------------------------------------------------------- |
| `criacao_usuarios.py`     | Cadastra novos usuários e salva no arquivo `usuarios.json` |
| `verificacao_usuarios.py` | Lê e exibe todos os usuários cadastrados                   |
| `usuarios.json`           | Banco de dados gerado automaticamente                      |

---

## Como usar

### Cadastrar usuários

```bash
python criacao_usuarios.py
```

O programa vai pedir: nome, idade, cidade, estado e e-mail.  
O e-mail deve ser de um dos provedores aceitos (Gmail, Hotmail, Yahoo ou Outlook).  
Os dados são salvos em `usuarios.json`.

### Visualizar usuários cadastrados

```bash
python verificacao_usuarios.py
```

Exibe todos os usuários salvos no arquivo `usuarios.json`.

---

## Requisitos

- Python 3.x
- Nenhuma biblioteca externa (usa apenas `json` e `os`)

---

## Observações

- E-mails duplicados não são aceitos.
- O arquivo `usuarios.json` é criado automaticamente no primeiro cadastro.
