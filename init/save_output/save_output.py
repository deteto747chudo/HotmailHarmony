from subprocess import call
from colorama import Fore, Style, init
import os
import fade
import shutil
import keyboard
import subprocess

def clear_console():
    """Clear the console screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def delete_existing_files(output_dir):
    """Delete existing files in the output directory."""
    for file_name in os.listdir(output_dir):
        file_path = os.path.join(output_dir, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(Fore.YELLOW + f"Deleted existing file: {file_path}" + Fore.WHITE)

def save_output():
    """Save dead.txt and live.txt to the output folder."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define file paths
    dead_file_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'modules', 'module_hotmailchecker', 'dead.txt'))
    live_file_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'modules', 'module_hotmailchecker', 'live.txt'))
    
    # Define output directory and file paths
    output_dir = os.path.abspath(os.path.join(base_dir, '..', 'output'))
    os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist
    
    # Delete existing files
    delete_existing_files(output_dir)
    
    dead_output_path = os.path.join(output_dir, 'dead.txt')
    live_output_path = os.path.join(output_dir, 'live.txt')
    
    # Copy files to the output directory
    try:
        shutil.copy(dead_file_path, dead_output_path)
        shutil.copy(live_file_path, live_output_path)
        print(Fore.GREEN + "Files have been successfully saved to the output folder." + Fore.WHITE)
    except FileNotFoundError as e:
        print(Fore.RED + f"File not found: {e}" + Fore.WHITE)
    except IOError as e:
        print(Fore.RED + f"An IOError occurred: {e}" + Fore.WHITE)

def get_data_from_file(file_path):
    """Read the content of the file and return it."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except IOError as e:
        return f"An IOError occurred: {e}"

def run_hotmail_selector():
    """Run the hotmail_selector.py script."""
    base_dir = os.path.dirname(__file__)
    script_path = os.path.join(base_dir, '..', 'hotmail_selector.py')
    subprocess.run(['python', script_path])

def wait_for_keypress():
    """Wait for any key press and then return to the hotmail_selector script."""
    print(fade.purplepink("---------------------------------------------------"))
    print("Press any key to return...")
    keyboard.read_event()  # Wait for a key press

def main():
    # Save the files and clear console
    save_output()
    clear_console()
    
    text = """
██████╗  █████╗ ████████╗ █████╗     ███████╗████████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║███████║   ██║   ███████║    ███████╗   ██║   ██║   ██║██████╔╝█████╗  ██║  ██║
██║  ██║██╔══██║   ██║   ██╔══██║    ╚════██║   ██║   ██║   ██║██╔══██╗██╔══╝  ██║  ██║
██████╔╝██║  ██║   ██║   ██║  ██║    ███████║   ██║   ╚██████╔╝██║  ██║███████╗██████╔╝
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ """
    
    print(fade.purplepink(text))
    print("DATA STORED , PATH - output/live.txt , output/dead.txt")
    
    # Wait for any key press to return
    wait_for_keypress()
    run_hotmail_selector()

if __name__ == '__main__':
    main()
