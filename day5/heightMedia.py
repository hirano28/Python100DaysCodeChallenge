# Here i can't use len() or sum() functions to complete the challenge]

students_height = input("Input a list of students height:\n").split()

total_height = 0
media_height = 0
total_students = 0

for x in students_height:
    int_x = int(x)
    total_height += int_x
    total_students += 1

media_height = total_height / total_students

print(f"The total height is: {total_height}, and the media height is: {int(media_height)}")
