import subprocess
import os

def run_proxy_scraper():
    """Run proxyScraper.py with the -p http argument."""
    try:
        # Get the directory of the current script (run_proxy_scraper.py)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the path to proxyScraper.py
        script_path = os.path.join(base_dir, '..', '..', 'modules', 'module_proxytool', 'proxyChecker.py')
        
        # Define the command and arguments
        command = ['python', script_path, '-p', 'http']
        
        # Run the command
        subprocess.run(command, check=True)
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the script: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    run_proxy_scraper()
