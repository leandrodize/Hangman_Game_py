import os
import pyfiglet
import random
import time


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
                        |
                        |
                        |
                        |
                   ========== """)
        with open ("./words.txt","r",encoding="utf-8") as wr:
            wordrand = random.choice(wr.readlines())
            wordrand = wordrand.lower().strip()
            worduser = ""
            lives = 6
            while lives > 0:
                losses = 0
                for letter in wordrand:
                    if letter in worduser:
                        print(letter,end=" ")
                    else:
                        losses = (losses + 1)
                        print("_",end=" ")
                if losses == 0:
                    print("\n")
                    fiwin = pyfiglet.figlet_format("*WON GAME*")
                    print(fiwin)
                    time.sleep(5)
                    os.system("cls")
                    break
                print("\n")
                letteruser = str(input("WRITE HERE ONE LETTER ==> "))
                worduser = (worduser + letteruser)
                os.system("cls")
                if letteruser in wordrand:
                    print("LETTER CORRECT, CONTINUE PLAYING")
                    print("LIVES ===> "+str(lives))
                if letteruser not in wordrand:
                    lives = (lives - 1)
                    print("LETTER INCORRECT, RETRY PLAYING")
                    print("LIVES ===> "+str(lives))
                if lives == 6:
                    print(fihangman)
                    print("""
                     ___
                    |   |
                        |
                        |
                        |
                        |
                   ========== """)
                if lives == 5:
                    print(fihangman)
                    print("""
                     ___
                    |   |
                    O   |
                        |
                        |
                        |
                   ========== """)
                if lives == 4:
                    print(fihangman)
                    print("""
                     ___
                    |   |
                   _O   |
                        |
                        |
                        |
                   ========== """)
                if lives == 3:
                    print(fihangman)
                    print("""
                     ___
                    |   |
                   _O/  |
                        |
                        |
                        |
                   ========== """)
                if lives == 2:
                    print(fihangman)
                    print("""
                     ___
                    |   |
                   _O/  |
                    |   |
                        |
                        |
                   ========== """)
                if lives == 1:
                    print(fihangman)
                    print("""
                     ___
                    |   |
                   _O/  |
                    |   |
                   /    |
                        |
                   ========== """)
                if lives == 0:
                    print(fihangman)
                    print("""
                     ___
                    |   |
                   _O/  |
                    |   |
                   / \  |
                        |
                   ========== """)
                    filoss = pyfiglet.figlet_format("LOSS GAME")
                    print("THE WORD WAS: "+ str(wordrand.upper()))
                    print(filoss)
                    time.sleep(5)
                    os.system("cls")
                    break
            else:
                fielse = pyfiglet.figlet_format("GAME OVER")
                print(fielse)
                time.sleep(4)
                os.system("cls")
    if option == 2:
        os.system("cls")
        fiinstructions = pyfiglet.figlet_format("INSTRUCTIONS")
        print(fiinstructions)
        with open ("./instructions.txt","r",encoding="utf-8") as i:
            for line in i:
                print(line)
    if option == 3:
        os.system("cls")
        fiseewords = pyfiglet.figlet_format("LIST WORDS:")
        print(fiseewords)
        with open ("./words.txt","r",encoding="utf-8") as lw:
            for line in lw:
                line = line.upper().strip()
                print(line)
    if option == 4:
        os.system("cls")
        fiaddwords = pyfiglet.figlet_format("ADD WORD")
        print(fiaddwords)
        with open ("./words.txt","a",encoding="utf-8") as aw:
            newword = str(input("WRITE HERE NEW WORD:"))
            newword = newword.lower().strip().replace(" ","")
            aw.write("\n")
            aw.write(newword)
    if option == 5:
        os.system("cls")
        fiexitgame = pyfiglet.figlet_format("EXIT GAME")
        print(fiexitgame)
        exit()



if __name__=="__main__":
    run()
