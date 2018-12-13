import secrets
from pathlib import Path
import urllib.request
import re
import argparse

parser = argparse.ArgumentParser(description='Python Implementation of Diceware',
                                 usage='diceware.py -l <number of words> [options]')

parser.add_argument('-l', '--length', type=int, default=5, help='number of words in password')

parser.add_argument('-s', '--secure', action='store_true', help='inserts random character for extra entropy')

args = parser.parse_args()

def readFile(file):
    try:
        dict = {}
        wordlist = cleanFile(file.open(mode='r').readlines())
        for line in wordlist:
            dict[line[:5]] = line[6:].replace('\n', "")
        return dict
    except:
        print('Something Went Wrong')

def getList():
    url = 'http://world.std.com/%7Ereinhold/diceware.wordlist.asc'
    try:
        urllib.request.urlretrieve(url, 'wordlist.txt')
    except:
        print("Unable To Reach Wordlist")

def cleanFile(wordlist):
    wordlist = wordlist[2:-11]
    return wordlist

def rollDice():
    roll = []
    rollTotalString = ""
    while(len(roll) < 5):
        num = secrets.randbelow(7)
        if(num != 0):
            roll.append(num)
            rollTotalString += str(num)
    return rollTotalString

def genPass(wordlist, wordAmt):
    password = ""
    for i in range(wordAmt):
        password += wordlist[rollDice()] + " "

    if(args.secure):
        password = extraStrength(password)
    return password

def extraStrength(password):
    charSet = [["~", "!", "#", "$", "%", "^"],
               ["&", "*", "(", ")", "-", "="],
               ["+", "[", "]", "\\", "{", "}"],
               [":", ";", "\"", "\'", "<", ">"],
               ["?", "/", "0", "1", "2", "3"],
               ["4", "5", "6", "7", "8", "9"]]

    passwordArr = password.split(" ") # this is kinda a stupid name, change pl0x
    selectedWord = passwordArr[secrets.randbelow(len(passwordArr))]
    position = secrets.randbelow(len(selectedWord))
    charToInsert = charSet[secrets.randbelow(6)][secrets.randbelow(6)]
    updatedWord = selectedWord[:position] + charToInsert + selectedWord[position:]

    return re.sub(r'\b'+selectedWord+r'\b', updatedWord, password)


def run(pass_length):
    print("[*] Generating")
    file = Path('wordlist.txt')
    if file.is_file():
        wordlist = readFile(file)
    else:
        getList()
        wordlist = readFile(file)

    print(genPass(wordlist, pass_length))

if __name__ == '__main__':
    run(args.length)
