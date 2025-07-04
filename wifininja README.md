# WiFiNinja v1.1 Usage Guide

### Overview

WiFiNinja is a professional network reconnaissance tool designed to scan local networks, detect connected devices (including laptops, smartphones, IoT devices, and more), and provide detailed information such as IP addresses, MAC addresses, hostnames, and device types. It features a sleek, hacker-style interface with minimal, professional animations and supports exporting results to CSV or JSON formats, compressed into a ZIP archive. The tool requires root privileges and is optimized for Kali Linux.

### Prerequisites

To run WiFiNinja, ensure the following requirements are met:

1. **Operating System**: Kali Linux (recommended) or any Linux distribution with Python 3 and network capabilities.
2. **Python Version**: Python 3.6 or higher.
3. **Required Python Libraries**:
    - scapy: For network scanning using ARP requests.
    - termcolor: For colored terminal output.
    - netifaces: For detecting network interfaces.
4. **Root Privileges**: The script requires sudo for network scanning operations.
5. **Network Connection**: An active network connection (Wi-Fi or Ethernet) is required.

### Installation

1. **Save the Script**:
    - Copy the provided wifininja.py script into a file named wifininja.py in your desired directory (e.g., ~/Downloads).
    - Example command to save the file:
        
        `nano wifininja.py`
        
2. **Make the Script Executable**:
    - Grant execution permissions to the script:
        
        `chmod +x wifininja.py`
        
3. **Install Dependencies**:
    - Install the required Python libraries using pip:
        
        `sudo pip3 install scapy termcolor netifaces`
        
    - Note: On Kali Linux, scapy is typically pre-installed. If not, the above command will install it.
4. **Verify Network Interface**:
    - Ensure you have an active network interface (e.g., eth0 for Ethernet or wlan0 for Wi-Fi). Check available interfaces with:
        
        `ip link`
        

### Running the Script

1. **Execute with Sudo**:
    - The script requires root privileges for network scanning. Run it using:
        
        `sudo ./wifininja.py`
        
    - If you run without sudo, the script will display an error and exit, prompting you to use sudo.
2. **Command Interface**:
    - Upon running, the script displays a professional startup animation with an ASCII logo and the message "Initializing network reconnaissance."
    - You will be presented with the **WiFiNinja Command Interface**, offering the following options:
        - **1. Start network scan**: Initiates a network scan to detect devices.
        - **2. Export results as CSV**: Saves the last scan results to a CSV file, compressed into a ZIP archive.
        - **3. Export results as JSON**: Saves the last scan results to a JSON file, compressed into a ZIP archive.
        - **4. Exit**: Terminates the script gracefully.
3. **Scanning Process**:
    - Select option 1 to start scanning.
    - The script will:
        - Detect the local IP, netmask, and network interface.
        - Calculate the subnet range (e.g., 192.168.1.1 - 192.168.1.254).
        - Display a professional progress bar during scanning.
        - Show real-time notifications for detected devices (e.g., "Device detected: 192.168.1.100 (hostname) - Laptop (Dell)").
    - Press Ctrl+C to stop the scan and view results.
4. **Viewing Results**:
    - After stopping the scan (or if interrupted with Ctrl+C), results are displayed in a formatted table showing:
        - IP Address
        - MAC Address
        - Hostname
        - Device Type (based on an expanded OUI database, including laptops like ASUS, Acer, MSI, etc.)
        - Connection Time
        - Disconnection Time (if applicable)
    - If no devices are found, a message will indicate "No devices detected on the network."
5. **Saving Results**:
    - Select option 2 (CSV) or 3 (JSON) to save the last scan results.
    - Results are saved with a timestamped filename (e.g., wifininja_scan_20250703_235012.csv or .json) and compressed into a ZIP archive (e.g., wifininja_scan_20250703_235012.zip).
    - The original file is deleted after compression to save space.
6. **Exiting**:
    - Select option 4 to exit. The script will display a termination message: "WiFiNinja terminated successfully."

### Example Workflow

1. Run the script:
    
    `sudo ./wifininja.py`
    
2. Output:
    
    `╔════════════════════════════════════╗
    ║       WiFiNinja v2.5               ║
    ║ Network Reconnaissance Tool        ║
    ║ Developed by xAI                   ║
    ╚════════════════════════════════════╝
    Initializing network reconnaissance
    === WiFiNinja Command Interface ===
    1. Start network scan
    2. Export results as CSV
    3. Export results as JSON
    4. Exit
    Select option [1-4]:`
    
3. Enter 1 to scan:
    
    `Local IP: 192.168.1.10, Interface: wlan0, Mask: 255.255.255.0
    Scanning subnet: 192.168.1.1 - 192.168.1.254
    Network scan initiated (press Ctrl+C to stop)...
    Scanning: [████████            ]
    Device detected: 192.168.1.100 (home-router) - Router (TP-Link)
    Device detected: 192.168.1.101 (laptop) - Laptop (ASUS)`
    
4. Press Ctrl+C to stop and view results:
    
    `Processing results...
    === WiFiNinja Scan Results ===
    IP Address      MAC Address       Hostname                  Device Type           Connection Time        Disconnection Time
    --------------------------------------------------------------------------------
    192.168.1.100   00:1a:11:xx:xx:xx home-router             Router (TP-Link)      2025-07-03 23:50:12    Still connected
    192.168.1.101   00:90:fb:xx:xx:xx laptop                  Laptop (ASUS)         2025-07-03 23:50:14    Still connected`
    
5. Save results by selecting 2 or 3:
    
    `Results saved to wifininja_scan_20250703_235012.zip.`
    

### Troubleshooting

1. **Sudo Error**:
    - If you see "Error: This tool requires root privileges," run the script with sudo:
        
        bash
        
        СвернутьПереносИсполнить
        
        Копировать
        
        `sudo ./wifininja.py`
        
2. **Network Interface Not Found**:
    - Ensure you are connected to a network. Check interfaces with:
        
        `ip link`
        
    - If the interface is not detected, specify it manually by modifying the get_network_info function to prioritize your interface (e.g., wlan0).
3. **No Devices Detected**:
    - Ensure the network has active devices.
    - Increase the scapy timeout in the scan_network function (e.g., change timeout=2 to timeout=5).
    - Verify the correct subnet is being scanned (displayed as "Scanning subnet: ...").
4. **Permission Error When Saving**:
    - If you encounter "Insufficient permissions to write file," ensure the directory has write permissions:
        
        `chmod -R u+w /path/to/directory`
        
    - Alternatively, run the script in a directory where you have write access (e.g., ~/).
5. **Missing Libraries**:
    - If a library is missing, install it with pip (as shown in the installation section).

### Advanced Customization

1. **Expand OUI Database**:
    - To add more device types, edit the oui_database dictionary in the get_device_type function. For example, to add a new device:
        
        `"00:xx:xx": "Device (Brand)"`
        
    - Obtain OUI prefixes from sources like macvendors.com or IEEE OUI lists.
2. **Modify Animations**:
    - To adjust the startup animation, edit the logo list in startup_animation.
    - To change the scanning progress bar, modify the loading_animation function (e.g., use a different character instead of █).
3. **Add Features**:
    - **Port Scanning**: Integrate nmap or scapy for port scanning of detected devices.
    - **Traffic Analysis**: Use scapy to monitor packet counts per device.
    - **Web Interface**: Add a Flask-based web interface for browser-based access.
    - Contact me with specific requirements for these features.

### Notes for Competition

- **Presentation**: The script's clean interface, professional animations, and detailed output make it ideal for demonstrations. Consider running it in a terminal with a dark theme for a sleek look.
- **Exporting Results**: Use the JSON export (option 3) for compatibility with other tools or for creating visual reports.
- **Enhancements**: If you need a graphical output (e.g., HTML report) or additional features like device history tracking, let me know, and I can provide tailored code.

###
