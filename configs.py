import os
from pathlib import Path

app_location = r"C:\Program Files\OpenVPN\bin\openvpn-gui.exe"
config_path = os.path.join(str(Path.home()), os.path.join('OpenVPN', 'config'))
all_file_path = 'config_files'
ip_check_url = 'https://ipinfo.io/json'