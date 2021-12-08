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

# def valida_contato(contato):
#     if (contato in AGENDA):
#         return True
#     else:
#         print("Esse contato não existe!")
#         return False


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


def salvar_contato(contato, telefone, email, endereco, tipo):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    if (tipo == 'i'):
        tipo = 'criado'
    elif (tipo == 'u'):
        tipo = 'editado'
    else:
        tipo = 'criado/editado'

    print("Contato {} {} com sucesso!".format(contato, tipo))


def criar_contato(contato, telefone, email, endereco):
    salvar_contato(contato, telefone, email, endereco, 'i')


def editar_contato(contato, telefone, email, endereco):
    salvar_contato(contato, telefone, email, endereco, 'u')


def deletar_contato(contato):
    if (contato in AGENDA):
        AGENDA.pop(contato)
        print("Contato {} deletado com sucesso!".format(contato))
    else:
        print("Esse contato não existe!")


# buscar_contato('Rodrigo')
print('####### AGENDA #######')
criar_contato('Maria', '11 94555-9988',
              'maria@maria.com', 'Rua Datileira, 22')
print('######################')
editar_contato('Rodrigo', '11 91111-2222',
               'edit@edit.com', 'Rua Editada, 589')
print('######################')
deletar_contato('Rafael')
print('######################')
mostrar_contatos()
