agenda = {}
lista_dados = ["nome","telefone","email","data de nascimento"]


while 1:
    
    ope = int(input("""
         *******************************************************************************
         **                              agenda pessoal                               **
         **                                                                           **
         **                                                                           **
         **                           1 - salvar contato                              **
         **                           2 - alterar contato                             **
         **                           3 - buscar contatos                             **
         **                           4 - apagar contato                              **
         **                           5 - lista de contatos                           **
         **                                                                           **
         ** pressione 0 pra sair                                                      **
         *******************************************************************************
        

    """))

    if ope == 1:
        print("salvar contato")
        contato = []
        contato.append(input("nome"))
        contato.append(input("telefone"))
        contato.append(input("E-mail"))
        contato.append(input("data de nascimento"))
        agenda[nome]=contato
        print(f"contato {nome} foi salvo com sucesso")
              
    elif ope == 2:
        print ("alterar contato")
        nome = input("qual o contato: ")
        print(agenda[nome])
        campo = input("qual o dado que voce quer alterar: ")
        print(f"voce quer alterar {[agenda[nome][lista_dados.index(campo)]]} ?")
        novo_dado = input("qual o novo dado: ")
        agenda[nome][lista_dados.index(campo)]
        
    elif ope == 3:
        print ("buscar contato")
        nome = input("qual contato: ")
        print(agenda[nome])
    elif ope == 4:
        print ("Apagar contato")
        nome = input("qual o contato: ")
        contato = agenda[nome]
        if contato == agenda.pop(nome):
            print(f"{nome} foi apagado com sucesso")
    elif ope == 5:
        print ("Listar contatos")
        print(f"a agenda possui  contatos")
    elif ope == 0:
        break
