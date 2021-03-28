print("Wlcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people_total = int(input("How many people to split the bill?"))

payment_total = total_bill * (1 + (percentage_tip)/100) / people_total
paymentFinal = round(payment_total, 2)
formatedPaymentFinal = "{:.2f}".format(paymentFinal)


print(f"Each person should pay: {formatedPaymentFinal}")