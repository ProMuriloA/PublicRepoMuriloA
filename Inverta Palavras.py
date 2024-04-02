def inverta_palavras():
    print('Inverta textos/palavras com esse algoritmo')
    string_para_teste = input("Digite uma palavra: ")
    string_array = []
    for letra in string_para_teste:
        string_array.insert(0, letra)
    string_final = ''.join(string_array)
    print(string_final)

sair = False

while sair == False:
    inverta_palavras()
    print('Deseja continuar?')
    sim_ou_nao = input('(Y/N)?')
    if sim_ou_nao.lower() == 'y':
        sair = False
    else:
        sair = True