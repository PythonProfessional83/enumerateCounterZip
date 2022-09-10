# passinfArbitraryArgsToFunction.py
'''
1. Task1 - function with positional argument and arbitrary arguments.
2. Task2 - function with arbitrary keyword arguments.
'''
#
#
# Task1 - function with positional argument and arbitrary arguments.
#
'''
Task1.
Make a pizza with positional argument - size and arbitrary arguments: toppings
'''


def main():
    pizza(12, 'tomato', 'chhese', 'hum', 'onion')


def pizza(size, *toppings):  # toppings is the tuple
    print(f"You ordered the {size} inch pizza with the toppings: ")

    for topping in toppings:
        print(f"-{topping}")

    print()
    print(
        f"You ordered the {size} inch pizza with the toppings: {list(toppings)}", end='')
    for topping in toppings:
        print(f"{topping}", end=' ')
    print()


main()

#
#
# 2. Task2 - function with arbitrary keyword arguments.
#

'''
task2:
Create function, which accepts name, surname of the person as a positional arguement.
You don't know what kind of informations/arbitrary arguments will be passed farther, so create
**kwargs--> key-word argument, which will be accepting/ pucking any number of the key-value arguments.
'''
def main2():
    userData = dataGather('Kris', 'Kozak', location='Berlin', occupation='Painter', country='Germany')
    print(f"\nuserData: {userData}\n")
    
    for key, value in userData.items():
        print(f"{key:<12}: {value}")

def dataGather(name, surname, **userInfo):  # function packs data to the dictionary
    userInfo['name'] = name
    userInfo['surname'] = surname
    userInfo['gender'] = 'male'
    
    return userInfo
    


main2()

