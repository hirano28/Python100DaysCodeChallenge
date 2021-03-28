altura = input("Digite a sua altura: \n")
peso = input("Digite o seu peso: \n")

imc_calculator = float(peso) / (float(altura)**float(altura))


if imc_calculator < 18.5:
    print("You are underweight.\nYour BMI is: " + str(imc_calculator))
elif imc_calculator >= 18.5 and imc_calculator < 25:
    print("You are in normal range.\nYour BMI is: " + str(imc_calculator))
elif imc_calculator >= 25 and imc_calculator < 30:
    print("You are overweight.\nYour BMI is: " + str(imc_calculator))
elif imc_calculator > 30:
    print("Well... you are obese.\nYour BMI is: " + str(imc_calculator))
else:
    print("Please review data you entered for height and weight, probably is wrong.\nYour BMI is: " + str(imc_calculator))


    