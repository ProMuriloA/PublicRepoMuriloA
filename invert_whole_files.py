import sys

print('You can invert texts with this algorith')
print('Use the archive path and name as an argument')
def inverta_palavras():
    with open(sys.argv[1], 'r') as text_to_open:
        for line_inside in text_to_open:
            string_para_teste = line_inside
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
    print('Do you wish to continue?')
    sim_ou_nao = input('(Y/N)?')
    if sim_ou_nao.lower() == 'y':
        sair = False
    else:
        sair = True