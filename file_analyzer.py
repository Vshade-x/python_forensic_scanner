import re
import os
import time
import datetime
from pathlib import Path
import math

# --- CONFIGURATION ---
# Define the root directory to start the recursive scan. 
# We use a relative path to the script's location for portability.
SCAN_ROOT_DIRECTORY = Path.cwd() / 'Scan_Target' 
# NOTE: The client must create a folder named 'Scan_Target' and put files inside.

# Define the pattern to search for (Example: N###-#####)
SERIES_PATTERN = r'N\d{3}-\d{5}'
TIMEOUT_SECONDS = 10 

# List to store results
found_series_numbers = []
found_files = []

def search_pattern_in_file(file_path, pattern):
    """Opens a file, reads its content, and searches for the defined pattern."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
            match = re.search(pattern, text)
            return match.group() if match else ''
    except Exception:
        return '' # Return empty if file cannot be opened (e.g., binary files, permissions)

def conduct_scan():
    """Recursively walks through directories to find files containing the series pattern."""
    start_time = time.time()
    
    # 1. Ensure the target directory exists
    if not SCAN_ROOT_DIRECTORY.is_dir():
        print(f"❌ ERROR: Scan directory not found at {SCAN_ROOT_DIRECTORY}")
        return

    # 2. Walk the directory tree
    for root, dirs, files in os.walk(SCAN_ROOT_DIRECTORY):
        for filename in files:
            file_path = Path(root, filename)
            
            result = search_pattern_in_file(file_path, SERIES_PATTERN)
            
            if result: # If a pattern was found
                found_series_numbers.append(result)
                found_files.append(filename)

    # 3. Display Results
    end_time = time.time()
    duration = end_time - start_time
    
    display_report(duration)

def display_report(duration):
    """Prints the final, formatted analysis report."""
    today = datetime.date.today()
    
    print('\n' + '-' * 50)
    print(f'Search Date: {today.day}/{today.month}/{today.year}')
    print('\n')
    print('FILE\t\t\tSERIES_NUMBER')
    print('----\t\t\t-------------')
    
    # Print results
    for i in range(len(found_files)):
        print(f'{found_files[i].title():<20}\t{found_series_numbers[i]}')

    print('\n' + '-' * 50)
    print(f'Total Numbers Found: {len(found_series_numbers)}')
    print(f'Scan Duration: {math.ceil(duration)} seconds')
    print('-' * 50)


# --- EXECUTION ---
if __name__ == "__main__":
    conduct_scan()