import os
from configs import config_path

all_file_path = 'config_files'

def save_new_file(source_path, file_name, destination_path):
    try:
        # print(file_name)
        ext = file_name.split('.')[-1] 
        folder_name = file_name.replace(ext, '')

        folder_path = os.path.join(destination_path, folder_name)
        if os.path.exists(folder_path):
            pass
        else:
            os.mkdir(folder_path)

        f = open(source_path)
        a = f.readlines()
        f.close()
        
        file_path = str(os.path.abspath('credential.txt')).replace('\\','/')
        new_data = ''
        for i in a:
            if 'auth-user-pass' in i:
                i = i.replace('auth-user-pass', f'auth-user-pass {file_path}')
                # print(i)
            new_data = new_data + i

        destination_file_name = os.path.join(folder_path, file_name)
        j = open(destination_file_name, 'w')
        j.write(new_data)
        j.close()
    except:
        print(file_name)

def get_udp_tcp_list():
    udp_list = {}
    tcp_list = {}
    k = os.listdir(all_file_path)
    for i in k:
        file_path = os.path.join(all_file_path, i)
        # print(file_path)
        if i.endswith('udp.ovpn'):
            udp_list[i]=file_path
        elif i.endswith('tcp.ovpn'):
            tcp_list[i]=file_path
    return udp_list, tcp_list

k = os.listdir(all_file_path)
for i in k:
    file_path = os.path.join(all_file_path, i)
    save_new_file(file_path, i, config_path)