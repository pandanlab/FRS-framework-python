<h1>Project Setup Guide</h1>

This document provides instructions for setting up and running the project on both Windows and Linux environments.

<h1>Overview</h1>

This project requires Python and additional modules specified in `requirements.txt`. You can run the project in two modes: Normal Mode and Environment Mode. Follow the instructions below based on your operating system and mode.

<h1>Windows 10/11</h1>

**Normal Mode**

1. Setup Modules\
   pip install -r requirements.txt

2. Run Program\
   python main.py

3. Run Mode Edit FrontApp\
   python FrontApp/tool_edit.py

4. Build .py to Executable\
   pyinstaller main.spec

**Environment Mode**

1. Setup Environment\
   python -m venv venv\
   venv\Scripts\activate

2. Setup Modules\
   pip install -r requirements.txt

3. Run Program\
   python main.py

4. Run Mode Edit FrontApp\
   python FrontApp/tool_edit.py

5. Build .py to Executable\
   pyinstaller main.spec

6. Exit Environment\
   deactivate

<h1>Linux (Debian-based: Ubuntu, Xubuntu, Linux Mint, Debian)</h1>

**Install Dependencies**

   sudo apt-get update\
   sudo apt-get install python3-pip\
   sudo apt-get install python3-tk

**Normal Mode**

1. Setup Modules\
   pip install -r requirements.txt

2. Run Program\
   python main.py

3. Run Mode Edit FrontApp\
   python FrontApp/tool_edit.py

4. Build .py to Executable\
   pyinstaller main.spec

**Environment Mode**

1. Setup Environment\
   python -m venv venv\
   source venv/bin/activate

2. Setup Modules\
   pip install -r requirements.txt

3. Run Program\
   python main.py

4. Run Mode Edit FrontApp\
   python FrontApp/tool_edit.py

5. Build .py to Executable\
   pyinstaller main.spec

6. Exit Environment\
   deactivate

<h1>Additional Notes</h1>

- Requirements File: Ensure that `requirements.txt` contains all the necessary dependencies for the project.
- PyInstaller: For building the executable, make sure that you have a valid `main.spec` file. If you need to customize the build process, refer to the PyInstaller documentation.
- Virtual Environment: Using a virtual environment is recommended to manage project-specific dependencies.

<h1>Troubleshooting</h1>

- Module Not Found Errors: Ensure that all required modules are listed in `requirements.txt` and that they are properly installed.
- Execution Issues: Check if Python is correctly installed and available in your system's PATH. Verify that you are using the correct version of Python.

For further assistance, please contact the project maintainers or consult the project's issue tracker.
