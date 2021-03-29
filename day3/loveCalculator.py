print("Welcome to the love calculator!")

name1 = input("Enter your name: ")
name2 = input("Enter the name of your loved one: ")

name1_lower = name1.lower()
name2_lower = name2.lower()

letters = ['t', 'r', 'u', 'e', 'l', 'o', 'v', 'e']
total_name1 = 0
total_name2 = 0

for x in letters:
    total_temp = name1_lower.count(x)
    total_name1 += total_temp

for x in letters:
    total_temp = name2_lower.count(x)
    total_name2 += total_temp

total_name1_str = str(total_name1)
total_name2_str = str(total_name2)
finalScore = int(total_name1_str + total_name2_str)

print(f"\nPontos nome 1: {total_name1}\nPontos nome 2: {total_name2}")


if finalScore < 10 or finalScore > 90:
    print(f"Your score is {finalScore}, you go together like coke and mentos.")
elif finalScore >= 40 and finalScore <= 50:
    print(f"Your score is {finalScore}, you are alright together.")
else:
    print(f"Your score is {finalScore}")
