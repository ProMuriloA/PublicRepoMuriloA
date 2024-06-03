def open_text(text_title):
    with open(text_title, 'r') as text_to_open:
        for line_inside in text_to_open:
            print(line_inside)

# Abrir Texto Introdutório
open_text('Temperature.txt')

# Input para determinar qual escala
escolha = int(input('Choose a number: '))

array_escala = [False, False, False, False, False, False]

# "Flipar" o booleano do array
def escolha_a_escala(escolha):
    escolha = int(escolha)
    if escolha == 1:
        array_escala[int(escolha-1)] = True
        pass
    elif escolha == 2:
        array_escala[escolha-1] = True
        pass
    elif escolha == 3:
        array_escala[int(escolha-1)] = True
        pass
    elif escolha == 4:
        array_escala[int(escolha-1)] = True
        pass
    elif escolha == 5:
        array_escala[int(escolha-1)] = True
        pass
    elif escolha == 6:
        array_escala[int(escolha-1)] = True
        pass
    else:
        print('Type a valid number')
        pass

escolha_a_escala(escolha)

# Retornar o Índice do Booleano Flipado
def RetornaIndiceArrayEscala():
    for indice, valor in enumerate(array_escala):
        if valor == True:
            return indice
        
indice_escolhido = RetornaIndiceArrayEscala()
temperatura = float(input('Tell me the temperature: '))

# Classe para processamento de informações

class ConversorDeTemperatura:
    def __init__(self) -> None:
        self.indice_escolhido = indice_escolhido
        self.temperatura = temperatura
        self.nome_temp_final = ['Celsius', 'Kelvin', 'Fahrenheit']
    
    def CelsiusParaFahrenheit(self):
        return ((temperatura * 1.8) + 32)
    def CelsiusParaKelvin(self):
        return (temperatura + 273)
    def FahrenheitParaCelsius(self):
        return (temperatura -32) /18
    def FahrenheitParaKelvin(self):
        return ((((temperatura -32)*5)/9) + 273)
    def KelvinParaCelsius(self):
        return (temperatura - 273)
    def KelvinParaFahreinheit(self):
        return (((temperatura - 273)*1.8) + 32)
    def escolha_metodo(self, indice_escolhido):
            if indice_escolhido == 0:
                return ConversorDeTemperatura.CelsiusParaFahrenheit(self), self.nome_temp_final[2]
            if indice_escolhido == 1:
                return ConversorDeTemperatura.CelsiusParaKelvin(self), self.nome_temp_final[1]
            if indice_escolhido == 2:
                return ConversorDeTemperatura.FahrenheitParaCelsius(self), self.nome_temp_final[0]
            if indice_escolhido == 3:
                return ConversorDeTemperatura.FahrenheitParaKelvin(self), self.nome_temp_final[1]
            if indice_escolhido == 4:
               return ConversorDeTemperatura.KelvinParaCelsius(self), self.nome_temp_final[0]
            if indice_escolhido == 5:
                return ConversorDeTemperatura.KelvinParaFahreinheit(self), self.nome_temp_final[2]
    def afirmacao_final(self, temperatura_final, nome_temp_final):
        print("The temperature in " + str(nome_temp_final) + " is " + str(temperatura_final))

# Output da Calculadora
Conversor1 = ConversorDeTemperatura()
temperatura_final = Conversor1.escolha_metodo(indice_escolhido)
temperatura_final = temperatura_final[0]
nome_temp_final = Conversor1.escolha_metodo(indice_escolhido)[1]
Conversor1.afirmacao_final(temperatura_final, nome_temp_final)