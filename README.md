# Surfshark VPN Automation with Python

This project automates VPN connection management using Surfshark and OpenVPN with Python scripts.

---

## 🔧 Step 1: Get Credentials and OpenVPN App

1. Get your Surfshark credentials from:  
   👉 [Surfshark Manual Setup](https://my.surfshark.com/vpn/manual-setup/main/openvpn)

2. Download and install the OpenVPN GUI app for Windows:  
   👉 [OpenVPN Setup Guide](https://support.surfshark.com/hc/en-us/articles/360003204233-How-to-set-up-OpenVPN-GUI-app-on-Windows)

---

## 📁 Step 2: Prepare Configuration

1. Place all your `.ovpn` configuration files into the `config_files` folder.
2. Install the OpenVPN app on your Windows machine.
3. Create a `credential.txt` file and add your Surfshark username and password:  
   ```
   your_username
   your_password
   ```
4. Run `fil_open_close.py`.  
   ✅ **Important:** This script must be run once to prepare the environment.

---

## 🧠 Step 3: Use `ip_changer.py`

You can now use `ip_changer.py` to connect, disconnect, and manage VPN servers.

### 🗂 Get All Server List
```python
get_all_server_list()
```
Returns a list of all available servers.

---

### 🔌 Connect to a VPN Server
```python
connect_new_vpn(server_name)
```
Connects to a specific server from the list above.

---

### 🔌 Disconnect from VPN
```python
disconnect_all_vpn()
```
Disconnects all active VPN connections.

---

### 🌐 Check Current IP Address
```python
ip_check()
```
Returns your current IP address or `None` if an error occurs.

---

## 📌 Notes

- Make sure the OpenVPN app is installed and working properly.
- Always run `fil_open_close.py` once before using `ip_changer.py`.
- Ensure that server names match the `.ovpn` file names in the `config_files` directory.

---

## 📂 Project Structure

```
.
├── config_files/
│   └── your .ovpn files
├── credential.txt
├── fil_open_close.py
├── ip_changer.py
└── README.md
```

---

Happy surfing with Surfshark! 🌊
