lista_de_compras = []
# adicionar_item = 'i' 'inserir'
# apagar_item = 'a' 'apagar'
# listar = 'l' 'listar'
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air :')

    if opcao == 'i':
        Item = input('Item: ')
        lista_de_compras.append(Item)

    elif opcao == 'a':
        for i, valor in enumerate(lista_de_compras):
            print(i, valor)
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
        except ValueError:
            print('Por favor digite um número int. ')
        except IndexError:
            print('Índice não existe na lista ')
        except Exception:
            print('Erro desconhecido ')

    elif opcao == 'l':

        if len(lista_de_compras) == 0:
            print('Não tem itens ')

        for i, valor in enumerate(lista_de_compras):
            print(i, valor)

    elif opcao == 's':
        print('Saindo... ')
        break

    else:
        print('Por favor, escolha entre "i" para INSERIR, "a" para APAGAR, \n'
              '"l" para ver a LISTA ou "s" para SAIR ')
