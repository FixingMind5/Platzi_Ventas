import random

letter = None
words = ['apple', 'banana', 'car', 'bike', 'computer', 'python']
randNum = random.randint(0, 5)

def wordList():
    global words

    for idx, word in enumerate(words):
        print(" {}: {}".format(idx, word))

    print('\n')


def someWords():
    global words
    global randNum
    return words[randNum]


def longWord(word):
    eachSpace = range(len(word))

    return eachSpace


def getIt():
    return input('---> ')


def easyClue(word):
    if word == 'apple':
        print("A red rounded five word fruit")
    elif word == 'banana':
        print('A large yellow six word fruit')
    elif word == 'car':
        print('Something like McQueen')
    elif word == 'bike':
        print('Futurist E.T. (movie) vehicle')
    elif word == 'computer':
        print('You don\'t need it, programmer friend')
    elif word == 'python':
        print('the sssss\'s language')


def guessIt(word, eSpace):
    oWord = ''

    for e in eSpace:
        letra = getIt()
        if letra == word[e]:
            oWord += letra
            print('grats!\n')
            continue
        else:
            print('Ups! :(\n')
            break

    if oWord == word:
        print('=' * 50)
        print('-' * 20, 'YOU WON!', '-' * 20)
        print('=' * 50, '\n')
    else:
        print(':(' * 25)
        print('-' * 20, 'YOU LOSE', '-' * 20)
        print(':(' * 25, '\n')

    print('Let\'s play again')


if __name__ == '__main__':
    print("WELCOME TO GUESS THE WORD\n")
    print("There you have some words behind this instructions")
    print("So, you need to write each letter in front of ---> to start to play\n")

    wordList()

    word = someWords()
    eSpace = longWord(word)

    print("CLUE:")
    easyClue(word)
    print("")

    guessIt(word, eSpace)
