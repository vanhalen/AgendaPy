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
        buscar_contato(contato)
        print("-------------------------------------")


def buscar_contato(contato):
    if (contato in AGENDA):
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]['telefone'])
        print("Email:", AGENDA[contato]['email'])
        print("Endereço:", AGENDA[contato]['endereco'])
    else:
        print("Esse contato não existe!")


def incluir_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print("Contato {} adicionado com sucesso!".format(contato))


# mostrar_contatos()
incluir_contato('Maria', '11 94555-9988',
                'maria@maria.com', 'Rua Datileira, 22')
buscar_contato('Maria')
