# 365 dias em 1 ano
# 52 semanas em 1 ano
# 12 meses em 1 ano

currentAge = input("What is yout age?\n")

ageLimit = 90

ageLeft = ageLimit - int(currentAge)
monthsLeft = ageLeft * 12
weeksLeft = ageLeft * 52
daysLeft = ageLeft * 365

print(f"You have {daysLeft} days, {weeksLeft} weeks and {monthsLeft} months left.")





