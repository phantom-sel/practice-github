import random
import pyttsx3

def restart_the_game():
    user_restart_input = input("Press '1' for - Play again \nPress any key for - Quit")
    if user_restart_input == '1':
        main()
    else:
        print("Have a nice day sir...")
        quit() 
def score_maintain():
    if user_point == 10:
        print('congratulation, you win the match.')
        print("-------------------------")
        restart_the_game()
    elif pc_point == 10:
        print('you lose the match')
        print("-------------------------")
        restart_the_game()
def speak_function(str1):
    decoration = pyttsx3.init()
    rate = decoration.getProperty('rate')
    decoration.setProperty('rate', 210)
    voice = decoration.getProperty('voices')
    decoration.setProperty('voice', voice[1].id)
    decoration.say(str1)
    decoration.runAndWait()
def main():
    global pc_point
    global user_point
    pc_point = 0
    user_point = 0
    print("------------------------------------------------------")
    print("welcome to Digital Rock,Paper or scicer game by phantom")
    print("------------------------------------------------------")
    speak_function("Welcome buddy let's play together you and me ..")
    while pc_point < 10 or user_point < 10:
        option = ['Rock','Paper', 'Scicer']
        computor_input = random.choice(option)
        
        user_input = input('1.Rock \n2.Paper\n3.Scicer\n\t')
        if user_input == '1':
            if computor_input == 'Paper':
                print('you lose')
                print("-------------------------")
                speak_function("I win,")
                pc_point = pc_point + 1
                score_maintain()
            elif computor_input == 'Scicer':
                print('you win')
                print("-------------------------")
                speak_function("Oh no")
                user_point += 1
                score_maintain()
            else:
                print('Nobody win and lose you called that , tie')
                print("-------------------------")
        elif user_input == '2':
            if computor_input == 'Rock':
                print('you win')
                print("-------------------------")
                speak_function("Oh no")
                user_point += 1      
                score_maintain()      
            elif computor_input == 'Scicer':
                print('you lose')
                print("-------------------------")
                speak_function("I win")
                pc_point += 1
                score_maintain()
            else:
                print('Nobody win and lose you called that , tie')
                print("-------------------------")
        elif user_input == '3':
            if computor_input == 'Rock':
                print('you lose')
                print("-------------------------")
                speak_function("I win")
                pc_point += 1    
                score_maintain()        
            elif computor_input == 'Paper':
                print('you win')
                print("-------------------------")
                speak_function("Oh no")
                user_point += 1
                score_maintain()
            else:
                print('Nobody win and lose you called that , tie')
                print("-------------------------")

main()
# speak_function("hello i am")

        

