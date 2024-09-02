from subprocess import call
from colorama import Fore, Style, init
import os
import fade

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def gotostart():
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
    input("\nPress Enter to return to the menu...")

def Start():   
    clear_console() 
    text = """
██╗  ██╗ █████╗ ██████╗ ███╗   ███╗ ██████╗ ███╗   ██╗██╗   ██╗
██║  ██║██╔══██╗██╔══██╗████╗ ████║██╔═══██╗████╗  ██║╚██╗ ██╔╝
███████║███████║██████╔╝██╔████╔██║██║   ██║██╔██╗ ██║ ╚████╔╝ 
██╔══██║██╔══██║██╔══██╗██║╚██╔╝██║██║   ██║██║╚██╗██║  ╚██╔╝  
██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝ """
    print(fade.purplepink(text))
    print(fade.purpleblue("Harmony Multi Hotmail + Proxy Tool | deteto_chudo"))
    print(fade.purpleblue("More updates soon! | deteto_chudo"))
    print(("Select an option to continue :"))
    print(fade.purpleblue(" [1] Hotmail Account Checker\n [2] Proxy Tool"))
    user_input = input("Your Choice : ")

    if user_input == "1":
        call(["python", "./init/hotmail_selector.py"])
    elif user_input == "2":
        call(["python", "./initv2/proxy_selector.py"])
    else:
        gotostart()

Start()