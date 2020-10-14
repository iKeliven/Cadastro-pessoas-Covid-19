def cabecalho():
    print('*' * 40)
    print("***********Faculdade Cesusc*************")
    print("Curso: Análise e Desenvolvimento de Sistemas")
    print("Disciplina: Lógica Computacional e Algoritmos")
    print("Prof: Roberto Fabiano Fernandes")
    print("Aluna: Keliven Bordin Demarchi")
    print("Turma: ADS 11")
    print("Avaliação: N3")
    print('*' * 40, "\n")


# pedindo usuario e validando valores
def user_senha():
    user = ["admin"]
    pword = ["1234"]
    e_usuario = str(input("Usuário: "))
    while not e_usuario in user:
        e_usuario = str(input("Usuário inválido, tente novamente: "))

    e_senha = str(input("Senha: "))

    while not e_senha in pword:
        e_senha = str(input("Senha inválida, tente novamente: "))
    else:
        print("Bem vindo!")


# mostrando menu
def menu():
    print("Escolha a opção: \n"
          "1 - Cadastrar Dados \n"
          "2 - Listar Dados \n"
          "3 - Alterar Dados \n"
          "4 - Excluir Dados \n"
          "5 - Realizar Cópia do arquivo \n"
          "0 - Sair \n"
          "Digite a opção escolhida: ")
    return input()


# funcao menu de opcoes
def menu_opcoes():
    while True:
        opcao = menu()
        if opcao == '1':
            cadastro()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            nome = input('Insira o nome que deseja alterar: ').title()
            alterar(nome)
        elif opcao == '4':
            nome = input('Insira o nome que deseja excluir: ').title()
            excluir(nome)
        elif opcao == '5':
            print("Backup realizado!")
            copia()
        else:
            print('Programa finalizado!')
            break


# funcao cadastro
def cadastro():
    try:
        arquivo = open('Dados.txt', 'a')
        nome = input('Nome completo: ').title()
        cns = input('CNS: ')
        bairro = input('Bairro: ')
        un_saude = input('Unidade de Saúde: ')
        nascimento = input('Data de nascimento: ')
        comorbidades = str(input('Comorbidades: '))
        inicio = input('Data de início dos sintomas: ')
        endereco = input('Endereço: ')
        telefone1 = input('Telefone 1: ')
        telefone2 = input('Telefone 2: ')
        while telefone1 == '':
            print('Obrigatório preencher um telefone no cadastro!')
            telefone1 = input('Insira o Telefone 1: ')
        sintomas = str(input('Sintomas Inícias: '))
        arquivo.write(nome + '#' + cns + '#' + bairro + '#' + un_saude + '#' + nascimento + '#' + comorbidades + '#' +
                      inicio + '#' + endereco + '#' + telefone1 + '#' + telefone2 + '#' + sintomas + '#' + '\n')
        arquivo.close()
        print("Cadastro realizado com sucesso!")
    except IOError as error:
        print('Erro', error)


# funcao listar
def listar():
    try:
        arquivo = open("Dados.txt", "r+")
        print("Lista: \n-------")
        for linha in arquivo:
            print(linha)
            print("--------------------")
        arquivo.close()
    except IOError as error:
        print("Erro", error)


# funcao excluir nomes
def excluir(nome):
    try:
        arquivo = open("Dados.txt", "r")
        linhas = arquivo.readlines()
        for linha in linhas:
            if linha.startswith(nome):
                pos = linhas.index(linha)
                linhas.pop(pos)
                arquivo = open("Dados.txt", "w")
                arquivo.writelines(linhas)
        arquivo.close()
        print("Contato removido! \n")
        return 0
    except IOError as error:
        print("ERRO: ", error)


# funcoes cadastrar
def alterar(nome):
    try:
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for elemento in linhas:
                if elemento.startswith(nome):
                    nome = input('Insira o novo nome: ').title()
                    cns = input('Insira o novo CNS: ')
                    bairro = input('Insira o novo Bairro: ')
                    un_saude = input('Insira a nova Unidade de Saúde: ')
                    nascimento = input('Insira a nova Data de nascimento: ')
                    comorbidades = str(input('Comorbidade: '))
                    inicio = input('Insira a nova Data de início dos sintomas: ')
                    endereco = input('Insira o novo Endereço completo: ')
                    telefone1 = input('Insira o novo Telefone 1: ')
                    telefone2 = input('Insira o novo Telefone 2: ')
                    while telefone1 == '':
                        print('Obrigatório preencher um telefone no cadastro!')
                        telefone1 = input('Insira o novo Telefone 1: ')
                    sintomas = str(input('Sintomas Inícias: '))
                    pos = linhas.index(elemento)
                    item = (nome + '#' + cns + '#' + bairro + '#' + un_saude + '#' + nascimento + '#' + comorbidades + '#' +
                                  inicio + '#' + endereco + '#' + telefone1 + '#' + telefone2 + '#' + sintomas + '#' + '\n')
                    linhas.pop(pos)
                    linhas.insert(pos, item)
                    arquivo = open('Dados.txt', 'w')
                    arquivo.writelines(linhas)
                    arquivo.close()
                    print("Alteração realizada com sucesso!")
    except IOError as error:
        print('Erro', error)


# funcao backup
def copia():
    try:
        arquivo1 = open("Dados.txt", "r")
        arquivo2 = open("copia_Dados.txt", "w")
        for texto in arquivo1:
            arquivo2.write(texto)
        arquivo1.close()
        arquivo2.close()
    except IOError as error:
        print("ERRO: ", error)
