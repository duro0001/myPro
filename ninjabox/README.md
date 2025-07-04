NinjaBox is a powerful, all-in-one Windows utility tool designed for network reconnaissance, system diagnostics, and secure file operations. With a sleek, hacker-inspired interface, it provides features like viewing saved Wi-Fi passwords, gathering system information, checking internet speed, generating random tech quotes, and encrypting/decrypting files. This guide provides step-by-step instructions for installing and using NinjaBox on Windows, optimized for both beginners and professionals.

## 🚀 System Requirements

- **Operating System**: Windows 10 or 11 (64-bit recommended)
- **Python**: Version 3.9 or higher
- **Storage**: At least 100 MB free space for Python and dependencies
- **Internet**: Required for installing dependencies and testing internet speed
- **Administrator Privileges**: Required for certain operations (e.g., Wi-Fi password retrieval)

## 🛠️ Installation Steps

### 1. Install Python

1. **Download Python**:
    - Visit the [official Python website](https://www.python.org/downloads/) and download Python 3.9 or later.
    - Choose the latest stable version (e.g., Python 3.11.x) for compatibility.
2. **Run the Installer**:
    - Double-click the downloaded `.exe` file.
    - **Important**: Check the box labeled **"Add Python to PATH"** during installation.
    - Select **"Install Now"** and follow the prompts.
3. **Verify Installation**:
    - Open Command Prompt (`cmd`) and run:
        
        ```bash
        python --version
        
        ```
        
    - Ensure the output shows Python 3.9 or higher (e.g., `Python 3.11.4`).

### 2. Install Required Libraries

1. Open **Command Prompt** as Administrator:
    - Press `Win + S`, type `cmd`, right-click **Command Prompt**, and select **"Run as administrator"**.
2. Install the necessary Python libraries:
    
    ```bash
    pip install colorama pyfiglet psutil speedtest-cli cryptography wmi requests
    
    ```
    
    - **colorama**: For colored terminal output.
    - **pyfiglet**: For ASCII art in the interface.
    - **psutil**: For system information (CPU, RAM, etc.).
    - **speedtest-cli**: For internet speed testing.
    - **cryptography**: For file encryption/decryption.
    - **wmi**: For Windows-specific system details.
    - **requests**: For fetching external data (e.g., IP location).
3. Verify library installation:
    
    ```bash
    pip list
    
    ```
    
    - Ensure all listed libraries are installed.

### 3. Download and Save NinjaBox

1. **Obtain the Script**:
    - Copy the `ninjabox.py` script from the provided source or repository.
    - Save it to a folder (e.g., `C:\Users\YourUsername\Desktop`).
2. **Set Execution Permissions** (optional):
    - Windows does not require `chmod`, but ensure the script is in a writable directory.

## ▶️ Running NinjaBox

1. **Navigate to the Script Directory**:
    - Open Command Prompt and change to the directory containing `ninjabox.py`:
        
        ```bash
        cd C:\Users\YourUsername\Desktop
        
        ```
        
2. **Launch the Tool**:
    - Run the script with Python:
        
        ```bash
        python ninjabox.py
        
        ```
        
    - The tool will display a hacker-style ASCII banner and load the main menu.

## 📋 Main Menu

Upon launching, NinjaBox presents the following options:

```
=== NinjaBox Command Center ===
1. View Wi-Fi Passwords      → Retrieve saved Wi-Fi SSIDs and passwords
2. System Informationen      → Display CPU, RAM, GPU, Disk, IP, and Antivirus details
3. IP & Internet Speed       → Show public IP, geolocation, and download/upload speeds
4. Random Joke               → Generate a fun, hacker-style tech quote
5. Motivation                → Get inspired with coding-related quotes
6. Encrypt a File            → Securely encrypt a file
7. Decrypt a File            → Decrypt a previously encrypted file
8. Exit                      → Terminate NinjaBox

```

- Select an option by entering the corresponding number (e.g., `1` for Wi-Fi Passwords).
- Follow on-screen prompts for each feature.

## 🔐 File Encryption and Decryption

### Encrypt a File

1. Select option `6` from the main menu.
2. Enter the path to the file you want to encrypt (e.g., `C:\Users\YourUsername\Desktop\secret.txt`).
3. NinjaBox will:
    - Generate an encrypted file (e.g., `secret.txt.enc`).
    - Create a key file (`key.key`) in the same directory.
4. **Important**: Store `key.key` securely, as it is required for decryption.

### Decrypt a File

1. Select option `7` from the main menu.
2. Enter the path to the encrypted file (e.g., `C:\Users\YourUsername\Desktop\secret.txt.enc`).
3. Ensure the `key.key` file is in the same directory as the encrypted file.
4. NinjaBox will decrypt the file and restore the original (e.g., `secret.txt`).

## 🧑‍💻 Usage Tips

- **Run as Administrator**: For features like Wi-Fi password retrieval (using `netsh`), run Command Prompt as Administrator.
- **Keep Key Safe**: Always back up the `key.key` file for encrypted files. Without it, decryption is impossible.
- **Optimal Display**: Use Command Prompt or Windows Terminal for the best experience with ASCII art and animations.
- **File Placement**: Place `ninjabox.py` in an accessible folder (e.g., Desktop) and navigate there using `cd`.
- **Internet Speed Test**: Ensure an active internet connection for option `3` (IP & Internet Speed).
- **Windows Only**: Features like Wi-Fi password retrieval and system information rely on Windows-specific commands (`netsh`, `wmi`), so the tool is not compatible with other operating systems.

## 🛡️ Troubleshooting

1. **Python Not Found**:
    - If `python --version` fails, ensure Python is added to PATH. Reinstall Python and check **"Add to PATH"**.
    - Alternatively, use the full path to Python (e.g., `C:\Python39\python.exe ninjabox.py`).
2. **Library Installation Fails**:
    - Run Command Prompt as Administrator and retry:
        
        ```bash
        pip install colorama pyfiglet psutil speedtest-cli cryptography wmi requests
        
        ```
        
    - Ensure `pip` is up-to-date:
        
        ```bash
        pip install --upgrade pip
        
        ```
        
3. **Wi-Fi Password Retrieval Fails**:
    - Ensure Command Prompt is running as Administrator.
    - Verify Wi-Fi profiles exist using:
        
        ```bash
        netsh wlan show profiles
        
        ```
        
4. **File Encryption/Decryption Errors**:
    - Check that the file and `key.key` are in the specified directory.
    - Ensure the file path is correct (use full paths, e.g., `C:\Users\YourUsername\Desktop\secret.txt`).
5. **Internet Speed Test Fails**:
    - Verify your internet connection.
    - Retry option `3` or check `speedtest-cli` functionality:
        
        ```bash
        speedtest
        
        ```
        
6. **Script Crashes**:
    - Ensure all dependencies are installed.
    - Check for syntax errors in `ninjabox.py` or update to the latest version.

## 🎯 Competition Notes

- **Presentation**: Run NinjaBox in Windows Terminal with a dark theme for a professional, hacker-style look. The ASCII art and green text enhance visual appeal.
- **Showcase Features**: Demonstrate Wi-Fi password retrieval, system information, and file encryption for maximum impact.
- **Output Files**: Export system information or speed test results to a CSV/JSON file (if implemented) for a polished presentation.
- **Customization**: If you need additional features (e.g., network scanning like `wifininja.py`, GUI integration, or HTML reports), let me know, and I can provide tailored code.

## 📬 Support

For issues, feature requests, or further customization, please provide details about your requirements. Examples include:

- Adding new features (e.g., port scanning, network traffic analysis).
- Enhancing animations for a more dynamic interface.
- Integrating with other tools or exporting results in different formats.

NinjaBox is now ready to impress with its professional interface and powerful features. Good luck with your competition!





