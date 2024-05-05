def inverta_palavras():
    print('Inverta textos/palavras com esse algoritmo')
    string_para_teste = input("Digite uma palavra: ")
    string_array = []
    palavra = False
    list_parcial2 = []
    for letra in string_para_teste:

        if letra == ' ':
            palavra = True


        string_array.insert(0, letra)

    string_final = ''.join(string_array)
    if palavra == True:
        list_parcial = string_final.split(" ")
        for pal in list_parcial:
            list_parcial2.insert(0, pal)
        string_final2 = ' '.join(list_parcial2)
        print(string_final2)
    else:
        print(string_final)
        pass

sair = False

while sair == False:
    inverta_palavras()
    print('Deseja continuar?')
    sim_ou_nao = input('(Y/N)?')
    if sim_ou_nao.lower() == 'y':
        sair = False
    else:
        sair = True