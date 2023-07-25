import socket
import math

def get_hostname():
    return socket.gethostname()

def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.getaddrinfo(hostname, None, socket.AF_INET)[0][4][0]
        return local_ip
    except socket.error as e:
        print("An error occurred:", e)
        return None

import psutil
def get_disk_space_GB():
    disk_info = psutil.disk_usage('/')
    total_space = disk_info.total / (1024 ** 3)  # Convert bytes to GB
    used_space = disk_info.used / (1024 ** 3)    # Convert bytes to GB
    free_space = disk_info.free / (1024 ** 3)    # Convert bytes to GB

    return total_space, used_space, free_space

def get_disk_info_string():
    
    total, used, free = get_disk_space_GB()
    
    total_s = "{:.1f}GB".format(total)
    used_s = "{:.1f}GB".format(used)
    free_s = "{:.1f}GB".format(free)
    percent_s = "{:.1f}%".format(math.floor(free/total*100))
    
    return f'{total_s}, {used_s}, {free_s}[{percent_s}]'