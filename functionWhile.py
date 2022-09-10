# functionWhile.py
'''
Recall of very simple operations with functions via task1 and task2:
1. Functions with while loop.
2. Break statement.
3. Pickle module to save dictionary. 
   Don't forget to change key value name during every iteration.
4. simple_colors module.
'''
#
#
# Functions with while loop task1.
#
from simple_colors import *
import pickle
from pathlib import Path
import os
'''
task1:
Create the while loop with the functions inside, which returns formatted name.
Quit the while loop with breake statement.
'''


def main():
    # creating while loop with breake statement
    while True:  # infinite loop
        name = input("Ener the first name or 'q' to quit: ")

        if name == 'q':
            break  # quit the while loop

        lastName = input("Enter yout 2nd name or 'q' to quit: ")
        if lastName == 'q':
            break

        print(f"Hello! {prepareName(name, lastName)}")


def prepareName(first, last):
    return f"{str(first).title()} {str(last).title()}"


main()

#
#
# Functions with while loop task2.
#
'''
task2:
Write a while loop, that allows users to enter album's artis and title.
Call function makeAlbum(), which returns distinary {artist, title}.
Print dictionary.
Use breake statement to quit the while loop. 
'''


def main2():
    # changing current directory
    patH = Path.cwd() / Path('recall')  # for saving the file
    os.chdir(patH)  # to save file in the recall directory

    # creating while loop
    counter = 0
    while True:
        counter += 1
        artist = input(
            str("\n\nEnter the album's artist or 'q' to quit: ").title())

        if artist.lower() == 'q':
            break

        title = input(
            green("Enter the title of the album or 'q' to quit: ", ['bold', 'underlined']))

        if title == 'q':
            break

        print(f"\nYour album is: {albumDict(artist, title, counter)}\n")


def albumDict(artist, title, counter):

    # loading the earlier created dictionary or using the empty one
    try:
        inputFile = open('albumDict.dat', 'rb')
        album = pickle.load(inputFile)
        inputFile.close()
    except FileNotFoundError:
        album = {}

    # packing parameters to dictionary
    # artist, counter are keys, therfore they must be different during evry iteration
    album[f"artist{counter}"] = artist
    album[f"title{counter}"] = title   # not to override old one

    # save dictionary
    saveAlbum(album)

    # return dictionary
    return album


def saveAlbum(dicT):
    filE = open('albumDict.dat', 'wb')
    pickle.dump(dicT, filE)
    filE.close()


main2()
