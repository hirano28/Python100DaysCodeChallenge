print("Bem vindo ao Python Entrega de Pizzas\n")
size = input("What size pizza do you want? S, M or B\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

total_amount = 0

if size == "S":
    total_amount += 15
    if add_pepperoni == "Y":
        total_amount += 2
    if extra_cheese == "Y":
        total_amount += 1
elif size == "M":
    total_amount += 20
    if add_pepperoni:
        total_amount += 3
    if extra_cheese:
        total_amount += 1
elif size == "B":
    total_amount += 25
    if add_pepperoni:
        total_amount += 3
    if extra_cheese:
        total_amount += 1
else:
    "Please enter a valid option, try again."

print(f"Your final bill is: {total_amount}")