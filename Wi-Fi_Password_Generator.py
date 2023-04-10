import random
import string
from pystyle import Colors, Colorate

color = random.randint(1,7)
if color == 1:
    color=Colors.purple_to_blue
if color == 2:
    color=Colors.cyan_to_blue
if color == 3:
    color=Colors.green_to_blue
if color == 4:
    color=Colors.green_to_yellow
if color == 5:
    color=Colors.green_to_cyan 
if color == 6:
    color=Colors.yellow_to_red
if color == 7:
    color=Colors.purple_to_red

    
#printing the banner
print(Colorate.Vertical(color,'''
 ______                                     _     ______                                              
(_____ \                                   | |   / _____)                             _               
 _____) )___  ___  ___ _ _ _  ___   ____ _ | |  | /  ___  ____ ____   ____  ____ ____| |_  ___   ____ 
|  ____/ _  |/___)/___) | | |/ _ \ / ___) || |  | | (___)/ _  )  _ \ / _  )/ ___) _  |  _)/ _ \ / ___)
| |   ( ( | |___ |___ | | | | |_| | |  ( (_| |  | \____/( (/ /| | | ( (/ /| |  ( ( | | |_| |_| | |    
|_|    \_||_(___/(___/ \____|\___/|_|   \____|   \_____/ \____)_| |_|\____)_|   \_||_|\___)___/|_|    
                                                                                                        
                                                                                                                                                                                                                                                                                                                  
''',True))



word_list = []
password_list = []

def wordlist():
    while True:
        word = input("Enter a word (or enter 'done' to stop): ")
        if word.lower() == 'done':
            break
        word_list.append(word.strip())


def generator():
    password_list.clear()
    while len(password_list) < 10:
        random_word_1 = random.choice(word_list).strip()
        random_word_2 = random.choice(word_list).strip()
        random_number = str(random.randint(1000, 9999))
        random_symbol = random.choice(string.punctuation)

        password_components = [random_word_1.capitalize(), random_word_2.capitalize(), random_number, random_symbol]
        random.shuffle(password_components)

        password = ''.join(password_components)
        if len(password) >= 12:
            password_list.append(password)


while True:
    print("\n*********** Menu ***********")
    choice = int(input("\n 1.Add in word list \n 2.See the word list \n 3.Generate Passwords \n 4.Exit \n Please select an option: "))
    if choice == 1:
        print("\n--------------------------------------------------------------------------------------------")
        wordlist()
        print("\n--------------------------------------------------------------------------------------------")
        input("\nPress Enter to continue ")
    elif choice == 2:
        print("--------------------------------------------------------------------------------------------")
        print(word_list)
        print("--------------------------------------------------------------------------------------------")
        input("\nPress Enter to continue ")
    elif choice == 3:
        generator()
        print("\n--------------------------------------------------------------------------------------------")
        print("\nHere are Strong Wi-Fi passwords that you can use them :\n")
        for password in password_list:
            print(password)
        print("\n--------------------------------------------------------------------------------------------")
        input("\nPress Enter to continue ")
    elif choice == 4:
        print("\n--------------------------------------------------------------------------------------------")
        print("\nGood Bye...")
        exit()
    else:
        print("Choose correct choice ")

