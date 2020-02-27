lives = 6
word = ""
letter = ""
updatedSpaces= []

def initialize():
    global word
    global updatedSpaces
    word = "airport"
    print("_ " * len(word))
    updatedSpaces = ("_ " * len(word))
    print("Try to guess the word within 6 tries")
    print(updatedSpaces)
    
def getLetter():
    global letter
    print("What is your guess?")
    letter = raw_input()


def won():
    global lives
    if updatedSpaces == word:
        print('Congratulations, you got the word!')
    else:
        '''lives = lives -1
        if lives == 0:
            print('You lost :(')'''
        getLetter()
    
def check():
    global updatedSpaces
    global lives
    if letter in word:
        index = -1
        for i in word:
            index += 1
            if letter == i:
                updatedSpaces[index] = letter
            else:
                continue
        print (' '.join(updatedSpaces))
        won()     
    else: 
        lives -= 1
        if lives == 0:
            print('You loser')
        getLetter()
    
def main():
    initialize()
    getLetter()
    check()