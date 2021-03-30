import random

print("Welcome to the Heads or Tails game\n")

rand_number = random.randint(1, 2)

if rand_number == 1:
    print("The result is: HEAD")
else:
    print("The result is: TAILS")
