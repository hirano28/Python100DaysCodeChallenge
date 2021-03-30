import random
import emoji

#Game UI
print("Welcome to the Treasure Map challenge!")

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]
print("    1     2     3")
print(f"1{row1}\n2{row2}\n3{row3}\n")

#Treasure localization
possible_choices = [11, 12, 13, 21, 22, 23, 31, 32, 33]
treasure = random.choice(possible_choices)
treasureString = str(treasure)

print(f"treasure is at: {treasure}")
rightChoice_number1 = treasureString[0]
rightChoice_number2 = treasureString[1]

#User trying to find the treasure
choice = input("In which position you think the treasure is? Type first the number for the column and after the number for the line\n")

choice_number1 = int(choice[0])
choice_number2 = int(choice[1])

if choice_number1 == int(rightChoice_number1) and choice_number2 == int(rightChoice_number2):
    map[choice_number2-1][choice_number1-1] = emoji.emojize("\U0001f947")
    print(f"1{row1}\n2{row2}\n3{row3}\n")
    print("Congratulations, you found the treasure!")
    end = input("Press enter to finish...")
else:
    map[choice_number2-1][choice_number1-1] = emoji.emojize("\U0001f4a9")
    print(f"1{row1}\n2{row2}\n3{row3}\n")
    print("Sorry, try again.")
    end = input("Press enter to finish...")