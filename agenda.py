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
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print("-------------------------------------")
    else:
        print('\n\n\n\nAgenda vazia!!!')
        print("-------------------------------------")


def buscar_contato(contato):
    #    if (contato in AGENDA): # Poderia ser esse if para validar
    try:
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]['telefone'])
        print("Email:", AGENDA[contato]['email'])
        print("Endereço:", AGENDA[contato]['endereco'])
    except:
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


def criar_contato(contato):
    try:
        AGENDA[contato]
        print("O contato {} já existe!".format(contato))
    except:
        telefone = input('Telefone:')
        email = input('E-mail:')
        endereco = input('Endereço:')
        print('\n')
        salvar_contato(contato, telefone, email, endereco, 'i')


def editar_contato(contato, telefone, email, endereco):
    if (contato in AGENDA):
        salvar_contato(contato, telefone, email, endereco, 'u')
    else:
        print("Esse contato não existe!")


def deletar_contato(contato):
    if (contato in AGENDA):
        AGENDA.pop(contato)
        print("Contato {} deletado com sucesso!".format(contato))
    else:
        print("Esse contato não existe!")


def exportar_contatos():
    pasta = '2.python/1.projeto1/agendapy/'
    nome_arquivo = 'agenda.csv'
    try:
        with open(pasta+nome_arquivo, 'w') as arquivo:
            arquivo.write("Nome;Telefone;E-mail;Endereço\n")
            for contato in AGENDA:
                arquivo.write("{};{};{};{}\n".format(
                    contato, AGENDA[contato]['telefone'], AGENDA[contato]['email'], AGENDA[contato]['endereco']))
            print('\n>>>>', nome_arquivo, 'exportada com sucesso!')
    except Exception as error:
        print("Erro ao exportar o arquivo")
        print(error)


def importar_contatos():
    pasta = '2.python/1.projeto1/agendapy/'
    nome_arquivo = 'agenda.csv'
    try:
        with open(pasta+nome_arquivo, 'w') as arquivo:
            arquivo.write("Nome,Telefone,E-mail,Endereço\n")
            for contato in AGENDA:
                arquivo.write("{};{};{};{}\n".format(
                    contato, AGENDA[contato]['telefone'], AGENDA[contato]['email'], AGENDA[contato]['endereco']))
            print('\n>>>>', nome_arquivo, 'exportada com sucesso!')
    except Exception as error:
        print("Erro ao exportar o arquivo")
        print(error)


def imprimir_menu():
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contato')
    print('3 - Criar contato')
    print('4 - Editar contato')
    print('5 - Deletar contato')
    print('6 - Exportar contatos (.CSV)')
    print('7 - Importar contatos (.CSV)')
    print('0 - Fechar agenda')
    print('Pressione Enter - Mostrar Menu')


# Roda o programa
def agenda():
    escolha_menu = input("Digite uma opção:")

    if(escolha_menu == ''):
        imprimir_menu()
    elif(escolha_menu == '1'):
        mostrar_contatos()
    elif(escolha_menu == '2'):
        contato = input('Digite o nome do contato:')
        print('\n')
        buscar_contato(contato)
    elif(escolha_menu == '3'):
        print('\n### Criar contato ###\n')
        contato = input('Nome:')
        criar_contato(contato)
    elif(escolha_menu == '4'):
        print('\n### Editar contato ###\n')
        contato = input('Digite o nome do contato:')
        telefone = input('Telefone:')
        email = input('E-mail:')
        endereco = input('Endereço:')
        print('\n')
        editar_contato(contato, telefone, email, endereco)
    elif(escolha_menu == '5'):
        contato = input('Digite o nome do contato:')
        deletar_contato(contato)
    elif(escolha_menu == '6'):
        exportar_contatos()
    elif(escolha_menu == '7'):
        importar_contatos()
    elif(escolha_menu == '0' or escolha_menu == 'exit' or escolha_menu == 'fechar'):
        return  # break caso for usar em um loop
    else:
        print("Comando não encontrado! Tente novamente ^^")

    print('\n')
    agenda()


def run():
    print('\n\n\n\n\n\n\n\n\n\n\n\n')
    print('########################')
    print('@@@@@@@@@@@@@@@@@@@@@@@@')
    print('Bem vindo ao AgendaPy!!!')
    print('@@@@@@@@@@@@@@@@@@@@@@@@')
    print('########################')
    print('\n')
    imprimir_menu()
    print('\n')
    agenda()
    print('\n')


run()
