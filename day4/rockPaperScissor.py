import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock Paper Scissors game!\n")
human_choice = int(input("What is your choice? 1 for rock, 2 for paper, 3 for scissors\n"))

possible_choices = ["1-Rock", "2-Paper", "3-Scissors"]
computer_choice = random.choice(possible_choices)
#print(computer_choice)

# Humano: Pedra
if human_choice == 1:
    if computer_choice == possible_choices[0]:
        print(f"You choose: Rock!\n {rock}\n")
        print(f"Computer choose: Rock!\n {rock}\n")
        print("It's a Draw!")
        finish = input("Press \'Enter\' to finish the game...")
    elif computer_choice == possible_choices[1]:
        print(f"You choose: Rock!\n {rock}\n")
        print(f"Computer choose: Paper!\n {paper}\n")
        print("You Lose!")
        finish = input("Press \'Enter\' to finish the game...")
    elif computer_choice == possible_choices[2]:
        print(f"You choose: Rock!\n {rock}\n")
        print(f"Computer choose: Scissors\n {scissors}\n")
        print("You Win!")
        finish = input("Press \'Enter\' to finish the game...")
# Humano: Papel
elif human_choice == 2:
    if computer_choice == possible_choices[0]:
        print(f"You choose: Paper!\n {paper}\n")
        print(f"Computer choose: Rock!\n {rock}\n")
        print("You Win!")
        finish = input("Press \'Enter\' to finish the game...")
    elif computer_choice == possible_choices[1]:
        print(f"You choose: Paper!\n {paper}\n")
        print(f"Computer choose: Paper!\n {paper}\n")
        print("It's a Draw!")
        finish = input("Press \'Enter\' to finish the game...")
    elif computer_choice == possible_choices[2]:
        print(f"You choose: Paper!\n {paper}\n")
        print(f"Computer choose: Scissors!\n {scissors}\n")
        print("You Lose!")
        finish = input("Press \'Enter\' to finish the game...")
# Humano: Tesoura    
elif human_choice == 3:
    if computer_choice == possible_choices[0]:
        print(f"You choose: Scissors!\n {scissors}\n")
        print(f"Computer choose: Rock!\n {rock}\n")
        print("You Lose!")
        finish = input("Press \'Enter\' to finish the game...")
    elif computer_choice == possible_choices[1]:
        print(f"You choose: Scissors!\n {scissors}\n")
        print(f"Computer choose: Paper!\n {paper}\n")
        print("You Win!")
        finish = input("Press \'Enter\' to finish the game...")
    elif computer_choice == possible_choices[2]:
        print(f"You choose: Scissors!\n {scissors}\n")
        print(f"Computer choose: Scissors!\n {scissors}\n")
        print("It's a Draw!")
        finish = input("Press \'Enter\' to finish the game...")
else:
    print("Type a valid option. 1 for rock, 2 for paper, 3 for scissors\nTry again")
    finish = input("Press Enter to finish the game...")