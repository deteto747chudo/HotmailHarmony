from subprocess import call
from colorama import Fore, Style, init
import os
import fade
import shutil
import msvcrt  # For detecting keypress on Windows

def clear_console():
    """Clear the console screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def gotostart():
    """Restart the Start function."""
    Start()

def view_file(file_path):
    """Read and print the contents of a file."""
    clear_console()
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        print(Fore.CYAN + f"Contents of {file_path}:" + Fore.WHITE)
        print(content)
    else:
        print(Fore.RED + f"The file {file_path} does not exist." + Fore.WHITE)
    wait_for_keypress()
    
    wait_for_keypress()

def wait_for_keypress():
    """Wait for any key press and then return to the hotmail_selector script."""
    print("Press any key to return...")
    msvcrt.getch()  # Wait for any key press
    return_to_selector()

def return_to_selector():
    """Return to the hotmail_selector.py script."""
    call(["python", "./init/hotmail_selector.py"])

def Start():   
    clear_console() 
    text = """
██╗  ██╗ ██████╗ ████████╗███╗   ███╗ █████╗ ██╗██╗     
██║  ██║██╔═══██╗╚══██╔══╝████╗ ████║██╔══██╗██║██║     
███████║██║   ██║   ██║   ██╔████╔██║███████║██║██║     
██╔══██║██║   ██║   ██║   ██║╚██╔╝██║██╔══██║██║██║     
██║  ██║╚██████╔╝   ██║   ██║ ╚═╝ ██║██║  ██║██║███████╗
╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝"""
    print(fade.purplepink(text))
    print(fade.purpleblue("Hotmail Checker | deteto_chudo"))
    print("Select an option to continue:")
    print(fade.purpleblue(" [1] Check Hotmail Accounts\n [2] View Live Accounts\n [3] View Dead Accounts\n [4] Save Logs to output Folder\n [99] Exit to main menu"))
    user_input = input("Your Choice : ")

    if user_input == "1":
        call(["python", "./modules/module_hotmailchecker/main.py"])
    elif user_input == "2":
        call(["python", "./init/retrieve/liveretrieve.py"])
    elif user_input == "3":
        call(["python", "./init/retrieve/deadretrieve.py"])
    elif user_input == "4":
        call(["python", "./init/save_output/save_output.py"])
    elif user_input == "99":
        call(["python", "./main.py"])
    else:
        gotostart()

if __name__ == '__main__':
    Start()
