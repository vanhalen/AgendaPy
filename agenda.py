AGENDA = {}

AGENDA['Rodrigo'] = {
    'telefone': '11 94222-3859',
    'email': 'rodrigorrchagas@gmail.com',
    'endereco': 'Rua Henrique Casela, 58',
}
AGENDA['Rafael'] = {
    'telefone': '11 95333-4960',
    'email': 'rafael.sa@gmail.com',
    'endereco': 'Av. Eloah Cabral Saueia, 251',
}


def mostrar_contatos():
    for contato in AGENDA:
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]['telefone'])
        print("Email:", AGENDA[contato]['email'])
        print("Endereço:", AGENDA[contato]['endereco'])
        print("-------------------------------------")


mostrar_contatos()
