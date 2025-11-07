# PYTHON FORENSIC SCANNER | REGEX PATTERN SEARCH

### 🎯 Project Overview

A robust Python command-line utility designed to perform **basic forensic analysis** by recursively scanning all files within a target directory, searching for a specific, standardized pattern (e.g., product IDs, security tags, or classified references).

### ✨ Key Features & Technical Details

* **Recursive Directory Scan:** Uses the `os` module to walk through the root directory and all subfolders, ensuring comprehensive coverage.
* **Regex Pattern Matching:** Implements the `re` (regular expressions) module to accurately locate complex and standardized text formats (e.g., 'N###-#####' identifiers) within text files.
* **Efficient Output:** Generates a clean, formatted terminal report detailing the file name, the found pattern, and the total duration of the scan.
* **Core Technology:** `os`, `re`, `pathlib`, `time`, `datetime`.

### 🚀 Execution and Usage

**1. Setup:** Create a subfolder named **`Scan_Target`** in the project root. Place all files you want to scan inside this folder.
**2. Execution:** Run the script directly from the command line:

    ```bash
    python file_analyzer.py
    ```

**3. Output:** The console will display a detailed report of all files found to contain the target series pattern.
