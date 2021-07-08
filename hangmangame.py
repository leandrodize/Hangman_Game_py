import os
import pyfiglet


def run():
    fihangman = pyfiglet.figlet_format("HANGMAN GAME")
    print(fihangman)
    menu = """WELCOME!!YOU HAVE THE FOLLOWING OPTIONS:
    1)START GAME
    2)INSTRUCTIONS
    3)SEE WORDS
    4)ADD WORD
    5)EXIT GAME
    WRITE HERE THE OPTION NUMBER ==> """
    option = int(input(menu))
    if option == 1:
        os.system("cls")
        print(fihangman)
        print("""
                     ___
                    |   |
                   _O/  |
                    |   |
                   / \  |
                        |
                   ========== """)
    if option == 2:
        os.system("cls")
        fiinstructions = pyfiglet.figlet_format("INSTRUCTIONS")
        print(fiinstructions)
    if option == 3:
        os.system("cls")
        fiseewords = pyfiglet.figlet_format("LIST WORDS:")
        print(fiseewords)
    if option == 4:
        os.system("cls")
        fiaddwords = pyfiglet.figlet_format("ADD WORD")







if __name__=="__main__":
    run()