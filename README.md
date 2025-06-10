step 1.

1.) get your credential from https://my.surfshark.com/vpn/manual-setup/main/openvpn
2.) get openvpn app from https://support.surfshark.com/hc/en-us/articles/360003204233-How-to-set-up-OpenVPN-GUI-app-on-Windows



step.2

1.) put all your config (.ovpn) files in config_files
2.) install openvpn app in Windows machine.
3.) put your credential (your_user_name and your_password) in credential.txt files
4.) run fil_open_close.py (do not forget this to run)



step.3

now use ip_changer.py to connecct vpn, disconnect vpn, get all server list.
1.) from ip_changer.py get all serverlist using get_all_server_list(). this will give you list containing all server.
2.) select your server and use it as input for connect_new_vpn(). this function try to connect vpn.
3.) for disconnect to server use disconnect_all_vpn().
4.) to check current ip address, use ip_check(), this will return either ip_address or None (if any error occur).
