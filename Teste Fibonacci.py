
print('Teste se seu número está na sequência fibonacci')


def calculadora_fibonacci():
    numero_para_teste = int(input("Insira o número a ser testado: "))
    indice1 = 1
    indice2 = 0
    fibo = False
    fibo_anterior = []
    if numero_para_teste == 0:
        print('Seu número está na sequência fibonacci')
        print('Seu número é' + str(numero_para_teste))
        fibo = True
    else:
        while indice2 < numero_para_teste:
            indice2 = indice1 + indice2
            fibo_anterior.append(indice2)

            indice1 = indice2 - indice1
            if numero_para_teste == indice2:
                print('Seu número está na sequência fibonacci')
                print('Seu número é' + str(numero_para_teste))
                fibo = True
                break
        if fibo == False:
            print('Seu número não está na sequência fibonacci')
    print("Fibonacci anterior:" + str(fibo_anterior))
sair = False

while sair == False:
    calculadora_fibonacci()
    print('Deseja continuar?')
    sim_ou_nao = input('(Y/N)?')
    if sim_ou_nao.lower() == 'y':
        sair = False
    else:
        sair = True