import os
import subprocess
import keyboard  # For detecting keypresses cross-platform
import fade

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
    base_dir = os.path.dirname(__file__)
    script_path = os.path.join(base_dir, '..', 'hotmail_selector.py')
    subprocess.run(['python', script_path])

def wait_for_keypress():
    """Wait for any key press and then return to the hotmail_selector script."""
    print(fade.purplepink("---------------------------------------------------"))
    print("Press any key to return...")
    keyboard.read_event()  # Wait for a key press

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    # Get the directory where this script is located
    base_dir = os.path.dirname(__file__)

    # Construct the path to dead.txt file
    file_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'modules', 'module_hotmailchecker', 'live.txt'))

    # Get the data from the file
    data = get_data_from_file(file_path)
    clear_console()
    text = """
██╗     ██╗██╗   ██╗███████╗
██║     ██║██║   ██║██╔════╝
██║     ██║██║   ██║█████╗  
██║     ██║╚██╗ ██╔╝██╔══╝  
███████╗██║ ╚████╔╝ ███████╗
╚══════╝╚═╝  ╚═══╝  ╚══════╝"""
    print(fade.purplepink(text))
    print(data)
    
    # Wait for any key press to return
    wait_for_keypress()
    run_hotmail_selector()

if __name__ == '__main__':
    main()
