while True:
    try:
        opcao = int(input('[1], [2] e [3]: ')) 
        if opcao < 1 or opcao > 3:
            print('Valor inválido. [1], [2] e [3]: ')
        else:
            break
    except ValueError:
        print('Valor inválido. [1], [2] e [3]: ')
    except:
        print('Erro inesperdo.[1], [2] e [3]: ')

match opcao:
    case 1:
        print('1 selecionado')
    case 2:
        print('2 selecionado')
    case _:
        print('3 selecionado')        