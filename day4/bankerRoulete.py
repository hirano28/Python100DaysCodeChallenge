import random

names_string = input("Give me everybody's name, separeted by a comma.\n")
names = names_string.split(",")

#choosenOne = random.randint(1, len(names))
choosenOne = random.choice(names)

#print(f"The choosen one is: {names[choosenOne-1]}")
print(f"The choosen one is: {choosenOne}")
