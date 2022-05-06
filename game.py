import random
def initialize():
    print("Choose number of digits to guess?")
    digits = int(input("Enter digits:"))
    print("You have entered ",digits)
    number=''
    for i in range(digits):
        number = number + str(random.randint(1,9))
    return number
number = initialize()
#print (number)
while True: 
    guess = str(input("Guess " + str(len(number)) + " digit number:"))
    if number == guess:
        print("You guessed correctly!")
        break
    else:
        bulls = 0
        cows = 0
        for d in guess:
            if d in number and guess.index(d) == number.index(d):
                bulls+=1
            elif d in number:
                cows+=1
        print(bulls,' bulls and ',cows,' cows')    
        #testing22
