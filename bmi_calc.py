
# Calculates weight
def bmi_calc(height, weight):
    
    return float((weight/(height**2)))

# Tells how much is the ideal weight for those who have to gain weight
def weight_needed_gain():
    weight2 = weight
    while bmi_calc(height, weight) < bmi_limits[0]:
        weight2 += 0.1
        bmi_calc(height, weight2)
        if bmi_calc(height, weight2) > bmi_limits[0]:
            return float(weight2)

# Tells how much is the ideal weight for those who have to lose weight
def weight_needed_lose_for_normal():
    weight2 = weight
    while bmi_calc(height, weight) > bmi_limits[1]:
        weight2 -= 0.1
        bmi_calc(height, weight2)
        if bmi_calc(height, weight2) < bmi_limits[1]:
            return float(weight2)
def weight_needed_lose_for_over():
    weight2 = weight
    while bmi_calc(height, weight) > bmi_limits[2]:
        weight2 -= 0.1
        bmi_calc(height, weight2)
        if bmi_calc(height, weight2) <= bmi_limits[2]:
            return float(weight2)

sair = False

while sair == False:
    #Variables and arrays needed
    height = float(input('Tell me your height in CENTIMETERS: '))/100
    weight  = float(input('Tell me your weight in KILOGRAMS: '))
    bmi_limits = [18.5, 25, 30]
    print('Your bmi is ' + str(bmi_calc(height, weight)))
    #Conditional operations
    if bmi_calc(height, weight) < bmi_limits[0]:
        
        print('You are underweight')
        
        weight_to_gain = weight_needed_gain()- weight
        #Tell how much weight the user needs to gain
        print('You have to gain ' + str(weight_to_gain) + ' kilograms')
        pass
    elif bmi_calc(height, weight) >= bmi_limits[0] and bmi_calc(height, weight) < bmi_limits[1]:
        print('You have a normal weight')
        pass

    elif bmi_calc(height, weight) >= bmi_limits[1] and bmi_calc(height, weight) < bmi_limits[2]:
        print('You are overweight')
        weight_to_lose = weight - float(weight_needed_lose_for_normal())
        #Tell how much weight the user needs to lose
        print('You need to lose ' + str(weight_to_lose) + ' kilograms')
        pass
    elif bmi_calc(height, weight) >= bmi_limits[2]:
        weight_to_lose = weight - weight_needed_lose_for_normal()
        #Tell how much weight the user needs to lose
        print('You need to lose ' + str(weight_to_lose) + ' kilograms to have a normal weight')
        weight_to_lose2 = weight - float(weight_needed_lose_for_over())
        print('You need to lose ' + str(weight_to_lose2) + ' kilograms to have an overweight weight')
        print('You are obese')
        pass
    else:
        print('Input error')
    print('Do you wish to continue?')
    sim_ou_nao = input('(Y/N)?')
    if sim_ou_nao.lower() == 'y':
        sair = False
    else:
        sair = True