print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a ilha do tesouro!")
print("A sua missão é achar o tesouro.")
print("---------------------------------\n")

escolha1 = input("Você está em uma encruzilhada. Para que lado você quer ir? Digite \"esquerda\" ou \"direita\"\n")
if escolha1 == "esquerda":
    escolha2 = input("Você chegou a um lago. Há uma ilha no meio do lago. Digite \"esperar\" para esperar por um bot ou digite \"nadar\" para nadar até a ilha\n")
    if escolha2 == "esperar":
        escolha3 = input("Você chegou a ilha ileso. Há uma casa com 3 portas. uma vermelha, uma amarela e outra azul. Qual cor você escolhe?\n")
        if escolha3 == "vermelha":
            print("Você entrou em um quarto em chamas e morreu queimado. Game Over!")
            input("Aperte enter para finalizar.")
        elif escolha3 == "amarela":
            print("Você encontrou o paraíso e agora está a salvo. Parabéns!!!")
            input("Aperte enter para finalizar.")
        elif escolha3 == "azul":
            print("Assim que a porta se abriu um leão pulou em cima de você e te devorou. Game Over!")
            input("Aperte enter para finalizar.")
    elif escolha2 == "nadar":
        print("Você não aguentou nadar até a ilha e morreu afogado. Game Over!")
        input("Aperte enter para finalizar.")
    else:
        print("Digite uma alternativa válida, comece novamente.")
        input("Aperte enter para finalizar.")
elif escolha1 == "direita":
    print("Você caiu em um abismo e morreu. Game Over!")
    input("Aperte enter para finalizar.")
else:
    print("Digite uma alternativa válida, comece novamente.")
    input("Aperte enter para finalizar.")
    
