import os
import subprocess

def run_hotmail_selector():
    base_dir = os.path.dirname(__file__)
    script_path = os.path.join(base_dir, '..', '..', 'initv2', 'proxy_selector.py')
    subprocess.run(['python', script_path])

def process_files():
    # Define the paths
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory
    source_file = os.path.join(current_dir, '..', '..','output.txt')  # The source file in the main directory
    target_file = os.path.join(current_dir, '..', '..','output', 'proxies.txt')  # The target file in the output/ directory

    # Check if the source file exists
    if not os.path.exists(source_file):
        print("Missing file: output.txt")
    else:
        # Read the content from output.txt
        with open(source_file, 'r') as src:
            data = src.read()

        # Overwrite proxies.txt with the data from output.txt
        with open(target_file, 'w') as tgt:
            tgt.write(data)
        print(f"Replaced data in {target_file}")

        # Delete the source file
        os.remove(source_file)
        print(f"Deleted {source_file}")

if __name__ == "__main__":
    process_files()
    run_hotmail_selector()
