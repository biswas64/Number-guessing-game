import random as rd  
def random_generator():
    randomNumber = rd.randint(1,100)
    return randomNumber


def user_guess():
    while True:
        try:
            userGuess = int(input("Enter your guess(1-100): "))
            if 1 <= userGuess <= 100 :
                return userGuess
            else:
                print("please enter value between 1-100")
        except ValueError:
                print("Invalid input")

def store():  
    #stores the use input and random number and returns it
    userNumber = user_guess()
    randomNumber =  random_generator()
    return userNumber,randomNumber

def data_handler(userNumber,randomNumber,chances):
    '''
    checks if userinput and random number are same.
    if same ,runs result
    if wrong and chances = 1, which means its in brutal mode....it runs result
    if wrong but not brutal mode... runs if_wrong function
    '''
    if userNumber != randomNumber:
        if chances == 1:
            result("lose",randomNumber)
        else:
            if_wrong(userNumber,randomNumber,chances)
        return
    else:
        print(f"chances left : {chances}")
        result("win",randomNumber)
        return

def checker(mode):
    #this functions checks the mode and provides the chances

    data= store()
    userNumber = data[0]
    randomNumber = data[1]
    match mode:
        case "easy":
            chances = 100
            data_handler(userNumber,randomNumber,chances)
            return
        case "normal":
            chances = 7
            data_handler(userNumber,randomNumber,chances)
            return
        case "hard":
            chances = 3
            data_handler(userNumber,randomNumber,chances)
            return
        case "brutal":
            chances = 1
            data_handler(userNumber,randomNumber,chances)
            return
        case "idiot":
            result("win",randomNumber)
            return
        



def if_wrong(userNumber,randomNumber,chances):

    #This functions checks for chances , and runs continuously until chances are left

    hint(userNumber,randomNumber)
    chances =  chances -1
    print(f"chances left : {chances}")
    while chances > 0  : 
        newGuess = user_guess()
        if  newGuess == randomNumber:
            result("win",randomNumber)
            return
        elif newGuess != randomNumber:
            if chances == 1:
                result("lose",randomNumber)
                return
            else:
                chances =  chances -1
                hint(newGuess,randomNumber)
                print(f"chances left : {chances}")
                

def hint(userNumber,randomNumber):
    
    # a simple logic is used to provid hints
    
    if (userNumber >=randomNumber +40):
        print("*** very high...try again ***")
    elif (userNumber >=randomNumber +10):
        print("***  high...try again ***")
    elif (userNumber >randomNumber ):
        print("*** high but close...try again ***")
    elif (userNumber <randomNumber-40 ):
        print("*** very low...try again ***")
    elif (userNumber <randomNumber -10):
        print("*** low...try again ***")
    elif (userNumber <randomNumber):
        print("*** low but close...try again ***")
    else:
        print("Some unforeseen event occured")


def modes():
    print("..Welcome to Number Guesser..")
    print("** Choose difficulty **")
    print("1. for easy mode")
    print("2. for normal mode")
    print("3. for hard mode")
    print("4. for brutal mode")
    print("5. for dumb idiot mode")
    
    while True:
        try:
            modeChoice = int(input("Choose mode (1/2/3/4/5): ")  )  
            modes = ["easy","normal","hard","brutal","idiot"]
            match modeChoice:
                case 1:
                    checker(modes[0])
                    return
                    
                case 2:
                    checker(modes[1])
                    return
                case 3:
                    checker(modes[2])
                    return
                case 4:
                    checker(modes[3])
                    return
                case 5:
                    checker(modes[4])
                    return
        except ValueError:
            print("use correct value")


def play_again():

    while True: 
            playAgain = input("do you wanna try again?(Y/N): ").lower()
            if playAgain == "y":
                modes()
            elif playAgain == "n":
                print("** Have a good day!! **")
                return
            else:
                print("please type either (Y or N)")



def result(res,randomNumber):
    if res == "win":
        print("Correct answer , You win ~~")
        play_again()
    elif res == "lose":
        print("*** oops, You chose wrong ***")
        print(f"correct answer : {randomNumber}")
        print("**Game over**")
        play_again()
    else:
        print("Some unforeseen event occured")
        play_again()

modes()
