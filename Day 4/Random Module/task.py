import random
import module

random_integer = random.randint(1, 10)
print(module.my_favorite_number)

random_number = random.random()

random_float = random.uniform(0.0, 10.0)

if random_float <= 5.0:
    print("Heads")
else:
    print("Tails")