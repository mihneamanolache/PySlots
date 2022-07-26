import random
import os
import inquirer
import json

# LOAD JSON
a_file = open("global.json", "r")
json_object = json.load(a_file)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

class bcolors:
    FAIL = '\033[91m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

initial_score = 100
possible_values = ['7', '@', '#', '$', '%', '»', '€']
print(f'Jackpot: {json_object["jackpot"]}')
print(f'Initial credits: {initial_score}')
print('\n')

profit = json_object["profit"]
profit += initial_score
json_object["profit"] = profit
a_file = open("global.json", "w")
json.dump(json_object, a_file)  

while initial_score > 0:
    questions = [
    inquirer.List('size',
                  message="How much do you want to bet?",
                  choices=['5', '10', '20', '25', '50', initial_score, 'Withdraw']
              ),
    ]   

    user_choice = inquirer.prompt(questions)
    try:
        user_bet = int(user_choice['size'])
    except:
        pass

    def update_jackpot():
        jackpot = json_object["jackpot"]
        jackpot += int(user_bet/2)
        json_object["jackpot"] = jackpot
        a_file = open("global.json", "w")
        json.dump(json_object, a_file)       

    if user_choice['size'] == 'Withdraw':
        profit = json_object["profit"]
        profit = json_object["profit"] - initial_score
        json_object["profit"] = profit
        a_file = open("global.json", "w")
        json.dump(json_object, a_file)  
        exit()

    elif user_bet > 0 and user_bet <= initial_score:
        if initial_score > 0 and user_bet > 0:
            val_1 = random.choice(possible_values)
            val_2 = random.choice(possible_values)
            val_3 = random.choice(possible_values)
            val_4 = random.choice(possible_values)
            val_5 = random.choice(possible_values)

        if val_1 != '7' and val_1 == val_2 and val_2 == val_3:
            profit = json_object["profit"]
            profit -= user_bet*2
            json_object["profit"] = profit
            a_file = open("global.json", "w")
            json.dump(json_object, a_file)  

            clearConsole()  
            update_jackpot()
            initial_score += user_bet*2
            print(f'Congratulationa! YOU WON {user_bet*2} credits!')
            print('\n')
            print(f'Jackpot: {json_object["jackpot"]}')
            print(f'Available Credits: {initial_score}')
            print('\n')
            print(random.choice(possible_values), '|', val_4, '|', random.choice(possible_values))
            print('----------')
            print(f'{bcolors.OKGREEN}{val_1} | {val_2} | {val_3}{bcolors.ENDC}')
            print('----------')
            print(random.choice(possible_values), '|', val_5, '|', random.choice(possible_values))
            print('\n')

        elif val_2 != '7' and val_2 == val_4 and val_4 == val_5:
            profit = json_object["profit"]
            profit -= user_bet*2
            json_object["profit"] = profit
            a_file = open("global.json", "w")
            json.dump(json_object, a_file)  

            clearConsole()  
            update_jackpot()
            initial_score += user_bet*2
            print(f'Congratulationa! YOU WON {user_bet*2} credits!')
            print('\n')
            print(f'Jackpot: {json_object["jackpot"]}')
            print(f'Available Credits: {initial_score}')
            print('\n')
            print(f'{random.choice(possible_values)} | {bcolors.OKGREEN}{val_4}{bcolors.ENDC} | {random.choice(possible_values)}')
            print('----------')
            print(f'{val_1} | {bcolors.OKGREEN}{val_2}{bcolors.ENDC} | {val_3}')
            print('----------')
            print(f'{random.choice(possible_values)} | {bcolors.OKGREEN}{val_5}{bcolors.ENDC} | {random.choice(possible_values)}')
            print('\n')

        elif val_1 != '7' and val_1 == val_2 and val_2 == val_3 and val_3 == val_4 and val_4 == val_5:
            profit = json_object["profit"]
            profit -= user_bet*4
            json_object["profit"] = profit
            a_file = open("global.json", "w")
            json.dump(json_object, a_file)  

            clearConsole()  
            update_jackpot()
            initial_score += user_bet*4
            print(f'Congratulationa! YOU WON {user_bet*4} credits!')
            print('\n')
            print(f'Jackpot: {json_object["jackpot"]}')
            print(f'Available Credits: {initial_score}')
            print(f'{random.choice(possible_values)} | {bcolors.OKGREEN}{val_4}{bcolors.ENDC} | {random.choice(possible_values)}')
            print('----------')
            print(f'{bcolors.OKGREEN}{val_1} | {val_2} | {val_3}{bcolors.ENDC}')
            print('----------')
            print(f'{random.choice(possible_values)} | {bcolors.OKGREEN}{val_5}{bcolors.ENDC} | {random.choice(possible_values)}')
            print('\n')

        elif val_1 == '7' and val_2 == '7' and val_3 == '7':
            profit = json_object["profit"]
            profit -= json_object["jackpot"] - user_bet
            json_object["profit"] = profit
            a_file = open("global.json", "w")
            json.dump(json_object, a_file)  

            clearConsole()  
            update_jackpot()
            initial_score = initial_score + json_object["jackpot"] + user_bet
            json_object["jackpot"] = 0
            a_file = open("global.json", "w")
            json.dump(json_object, a_file)
            print('Congratulationa! YOU WON THE JACKPOT!!!')
            print('\n')
            print(f'Jackpot: {json_object["jackpot"]}')
            print(f'Available Credits: {initial_score}')
            print(f'{random.choice(possible_values)} | {val_4}| {random.choice(possible_values)}')
            print('----------')
            print(f'{bcolors.OKGREEN}{val_1} | {val_2} | {val_3}{bcolors.ENDC}')
            print('----------')
            print(f'{random.choice(possible_values)} | {val_5} | {random.choice(possible_values)}')
            print('\n')

        else:
            profit = json_object["profit"]
            profit += user_bet
            json_object["profit"] = profit
            a_file = open("global.json", "w")
            json.dump(json_object, a_file)   
            clearConsole()
            update_jackpot()
            initial_score -= user_bet
            print('No luck this time. TRY AGAIN!')
            print('\n')
            print(f'Jackpot: {json_object["jackpot"]}')
            print(f'Available Credits: {initial_score}')
            print('\n')
            print(f'{random.choice(possible_values)} | {bcolors.FAIL}{val_4}{bcolors.ENDC} | {random.choice(possible_values)}')
            print('----------')
            print(f'{bcolors.FAIL}{val_1} | {val_2} | {val_3}{bcolors.ENDC}')
            print('----------')
            print(f'{random.choice(possible_values)} | {bcolors.FAIL}{val_5}{bcolors.ENDC} | {random.choice(possible_values)}')
            print('\n')
    else:
        clearConsole()  
        update_jackpot()
        print("That's not a valid option!")
        print('\n')
        print(f'Jackpot: {json_object["jackpot"]}')
        print('\n')
        print(f'Available Credits: {initial_score}')
        print('\n')

print('0 Credits available! Please refill')