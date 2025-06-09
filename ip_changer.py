import subprocess
import os
import requests
from configs import config_path, app_location, ip_check_url

def get_all_vpn_list():
    return os.listdir(config_path)

def connect_new_vpn(vpn_name):
    subprocess.call([
        app_location,
        "--command", "connect", vpn_name
    ])
# print("Disconnect OpenVPN")
def disconnect_all_vpn():
    subprocess.call([
        app_location,
        "--command", "disconnect_all"
    ])

def ip_check():
    try:
        page = requests.get(ip_check_url).json()
        ip = page('ip')
        return ip
    except:
        return None

   



