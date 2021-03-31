# Here i can't use len(), sum(), max() or min() functions to complete the challenge

notes = input("Enter the notes:").split()

higher_one = 0

for note in notes:
    int_note = int(note)
    if int_note > higher_one:
        higher_one = int_note

print(f"The highest note is: {higher_one}")