import random
import maths


def mutate(a_list):
    """The bug was that you were appending the new_item at the end of the for loop,
    which resulted in one value being added to the b_list"""
    b_list = []
    # new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
