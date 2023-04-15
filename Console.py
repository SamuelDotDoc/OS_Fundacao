import random

resp = "SIM"

def LogOn():
    loggado = False
    while(loggado == False):
        usuario = input("Usuario: ")
        senha = input("Senha: ") + "\n"
        d = {}
        with open("Files\Login.txt") as file:
            for line in file:
                (key, val) = line.split(": ")
                d[key] = val
        file.close()
        if usuario in d:
            if (senha == d.get(usuario)):
                print("Bem vindo agente ", usuario, "!")
                input()
                return
            else:
                print("ACESSO NEGADO")
                input()
        else:
            print("ACESSO NEGADO")
            input()
            quit()

def ConsoleEntidades():
    print("-----------------------------------------------------------------------------")
    print("PROMPT DE COMANDO 001 F1980 5MHZ")
    print("BANCO DE DADOS DE ENTIDADES")
    print("TERMINAL ", random.randint(1, 50), " - USUÁRIO CONFIGURADO PARA AGENTES")
    print("-----------------------------------------------------------------------------")
    print("O que deseja fazer?")
    print()
    print("<1> Pesquisar por entidade")
    print("<2> Registrar Entidade")
    print("<3> Voltar")
    alt = input()
    if (alt == '1' or alt == '2' or alt == '3'):
        if (alt == '1'):
            d = {}
            with open("Files\Entidades.txt") as file:
                for line in file:
                    (key, val) = line.split(": ")
                    d[key] = val
            print(str(d.keys()).strip('{'))
            pesquisa = "'" + input("Digite o nome da entidade que deseja pesquisar...") + "'"
            if pesquisa in d:
                print(d[pesquisa])
            else:
                print("Entidade não encontrada!")
            file.close()
            input()
            return
        elif (alt == '2'):
            print("Por favor informe:")
            numId = input("Código de identificação - ")
            classe = input("Classe do objeto - ")
            indicativos = input("Indicativos de sua presença - ")
            descricao = input("Descrição do objeto - ")

            print("Confirme o registro...<sim> ou <não>",
                  "\n Código do objeto: ", numId,
                  "\n Classe do objeto: ", classe,
                  "\n Indicativos do objeto: ", indicativos,
                  "\n Descrição do objeto: ", descricao)
            confirma = input().upper()

            if(confirma == 'SIM'):
                RegistraEntidade(numId, ("Classe - " + classe,"Indicativos - " + indicativos,"Descricao - " + descricao))
                print("Entidade Registrada!")
                input()
            else:
                print("Registro cancelado...")
                input()

            return
        else:
            return

    else:
        print("Responda com uma alternativa válida.")
        input()
        return

def RegistraEntidade(key, val):
    Entidade = {
        key : val
    }
    file = open("Files\Entidades.txt", "a")
    file.writelines(str(Entidade).strip("{}") + "\n")
    file.close()

def ConsoleAgentes():
    print("-----------------------------------------------------------------------------")
    print("PROMPT DE COMANDO 001 F1980 5MHZ")
    print("BANCO DE DADOS DE AGENTES")
    print("TERMINAL ", random.randint(1, 50), " - USUÁRIO CONFIGURADO PARA AGENTES")
    print("-----------------------------------------------------------------------------")
    print()
    d = {}
    with open("Files\Agentes.txt") as file:
        for line in file:
            (key, val) = line.split(": ")
            d[key] = val
    print(str(d.keys()).strip('{'))
    pesquisa = "'" + input("Digite o nome do agente que deseja pesquisar...") + "'"
    if pesquisa in d:
        print(d[pesquisa])
    else:
        print("Agente não encontrado!")
    file.close()
    input()
    return

LogOn()

while (resp == "SIM"):
    print("-----------------------------------------------------------------------------")
    print("PROMPT DE COMANDO 001 F1980 5MHZ")
    print("UNIDADE DE MONITORAMENTO E REGISTRO DE ENTIDADES")
    print("TERMINAL ", random.randint(1, 50), " - USUÁRIO CONFIGURADO PARA AGENTES")
    print("-----------------------------------------------------------------------------")
    print("O que deseja fazer?")
    print()
    print("<1> Acessar banco de dados de entidades")
    print("<2> Procurar por agentes no banco de dados")
    print("<3> Sair do console")
    alt = input()
    if (alt == '1' or alt == '2' or alt == '3'):
        if (alt == '1'):
            ConsoleEntidades()
        elif (alt == '2'):
            ConsoleAgentes()
        else:
            print("Saindo do console...")
            quit()
    else:
        print("Responda com uma alternativa válida.")
        input()
        resp == "SIM"