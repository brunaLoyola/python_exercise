lista_compras = []

while True:
    opcao = int(input("Digite uma opção: \n 01 - Adicionar Item \n 02 - Remover item \n 03 - Ver lista de compras \n 04 - Sair\n"))

    if opcao == 4:
        break
    elif opcao == 1:
        item = input("Digite o item a ser adicionado na lista de compras:")
        lista_compras.append(item)
        continue
    elif opcao == 2:
        remover = input("Digite qual item deseja remover:")
        if remover in lista_compras:
            lista_compras.remove(remover)
            print(f'"{remover}" removido da lista.')
        else:
            print("Item inexistente")
        
    elif opcao == 3:
        for item in lista_compras:
            print("-", item)
        continue
    else:
        print("Opção incorreta")
        continue