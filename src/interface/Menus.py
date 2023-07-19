import os
import time
from interface.Colors import *

# class for MainMenu
class MainMenu():

    # displays the MainMenu
    def display():

        state = True

        # clear the screen
        os.system('cls')
        
        # print text in the console
        print(f'\n\t╔══════════════════════════════════════════╗')
        print(f"\t║     | - PCJ E-Sports Team Tracker - |    ║")
        print(f'\t╚══════════════════════════════════════════╝')
        print(f"\n\n\n\tWhat do you want to do?")
        print(f"\t[" + Colors.blue + "1" + Colors.def_color + "] Register")
        print(f"\t[" + Colors.blue + "2" + Colors.def_color + "] View/Edit")
        print(f"\t[" + Colors.blue + "3" + Colors.def_color + "] Exit\n\n")
        
        while state:
            user_input = int(input("\t>  "))
            
            if user_input == 1:
                state = False
                return RegisterMenu.display()
            elif user_input == 2:
                state = False
                return ViewEditMenu.display()
            elif user_input == 3:
                state = False
                retval = MainMenu.exit_prompt()
            else:
                print('\tInvalid Input! Please Try again.')
                time.sleep(2)
                state = False
                return MainMenu.display()
    
    # display are you sure prompt
    def exit_prompt():
        
        state = True
        # clear the screen
        os.system('cls')

        print("\n\tDo you really want to exit?")
        print("\n\n\n\t[1] Yes")
        print("\t[2] No")

        while state:
            user_input = int(input("\n\tInput your choice here\t: "))
            if user_input == 1:
                state = False
                return MainMenu.exit_message()
            elif user_input == 2:
                state = False
                return MainMenu.display()
            else:
                print('\tInvalid Input! Please Try again.')
                time.sleep(2)
                state = False
                return MainMenu.display()

    # display an exit message 
    def exit_message():
        # clear the screen
        os.system('cls')

        print("\n\tThank you for using *insert app name*!")
        
# class for the Register Menu
class RegisterMenu():
    def display():
        
        state = True
        # clear the screen
        os.system('cls')
        
        print(f'\n\t╔══════════════════════════════════════════╗')
        print(f'\t║          || ~ REGISTRATION ~ ||          ║')
        print(f'\t╚══════════════════════════════════════════╝')
        print("\n\n\tChoose Option Below:")
        print("\t[" + Colors.yellow + "1" + Colors.def_color + "] Team")
        print("\t[" + Colors.yellow + "2" + Colors.def_color + "] Coach")
        print("\t[" + Colors.yellow + "3" + Colors.def_color + "] Player")
        print("\t[" + Colors.yellow + "4" + Colors.def_color + "] Back\n\n")

# class for the View/Edit Menu
class ViewEditMenu():
    def display():
        
        state = True
        # clear the screen
        os.system('cls')

        print('\n\tNice')