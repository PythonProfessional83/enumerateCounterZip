# passingListToFunction.py
'''
Passing a List to the Function.
Modifying a List in a Function.
Preventing a function from modyfying a list.
'''
from simple_colors import *
#
#
# task1 - passing a list to the function
#
'''
task1:
We have a list of users and we want to print greeting to each.
Send a list of names to a function, which greets each user individally.
'''


def main():
    names = ['Jack', 'Kris', 'John', 'Billy']
    greeting(names)


def greeting(names):
    for name in names:
        print(blue(f"Hello {str(name).upper()}!!", ['bold', 'underlined']))


main()

#
#
# task3
#
'''
task3
Consider a company that creates 3d printed models of designs, that user submit.
Dasigne that need to be printed are stored in the list and
after being printed they are moved to seprerate list.
Below code is without the function use.
'''
# test list.pop()
toBePrinted2 = ['spider', 'tomato', 'intelligence']
design1 = print(f"\n\ntoBePrinted.pop(): {toBePrinted2.pop()}\n")
print(f"toBePrinted: {toBePrinted2}\n\n")

unprintedDesigns = ['spider robot',
                    'intelligent home', 'artificial intelligence']
completedModels = []

if unprintedDesigns:   # list is True untill has any index
    print('\nis full\n')
else:
    print('\nis empty\n\n')

# while loop must be working until list is empty
while unprintedDesigns:     # list is True untill has any index
    model = unprintedDesigns.pop()
    completedModels.append(model)
    print(f"unprintedDesigns.pop()--> priting model: {model}")

print()
for model in completedModels:
    print(f"completed model: {model}")
print('\n\n')
'''
task3 - with functions. 
First function will handle printing the designs.
2nd function will summarize the print, that heve been made.
'''


def main2():
    unprintedDesigns = ['spider robot',
                        'intelligent home', 'artificial intelligence']
    completedModels = []
    printModels(unprintedDesigns, completedModels)
    print(f"\n\nunprintedDesigns:after pop():{unprintedDesigns}\n")


def printModels(unprinted, completed):
    
    while unprinted:
        model = unprinted.pop()
        completed.append(model)
        print(f"printing model:{model}")
    
    displayModels(completed)

def displayModels(completed):
    print('\n\n')
    for model in completed:
        print(f"completed model: {model}")

    print('\n\n')
    
main2()

'''
task4 - with functions. Preventing the 1st function from modyfying oryginala list. 
First function will handle printing the designs.
2nd function will summarize the print, that heve been made.
'''

def main3():
    unprintedDesigns = ['spider robot',
                        'intelligent home', 'artificial intelligence']
    completedModels = []
    printModels(unprintedDesigns[:], completedModels)
    print(f"\n\nunprintedDesigns:after pop():{unprintedDesigns}\n")  # original list is unchanged


def printModels(unprinted, completed):
    
    while unprinted:
        model = unprinted.pop()
        completed.append(model)
        print(f"printing model:{model}")
    
    displayModels(completed)

def displayModels(completed):
    print('\n\n')
    for model in completed:
        print(f"completed model: {model}")

    print('\n\n')
    
main3()