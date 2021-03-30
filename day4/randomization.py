import random

random_integer = random.randint(1, 10)
print(random_integer)

#Random float sempre vai de 0.000... a 0.999...
random_float = random.random()
print(random_float)

#se quiser expandir o limite basta multiplicar pelo número limite
#por exemplo, entre 0.000... a 4.999...
random_float = random.random()
random_float *= 5
print(random_float)