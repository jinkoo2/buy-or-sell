import psutil

def get_disk_space_GB():
    disk_info = psutil.disk_usage('/')
    total_space = disk_info.total / (1024 ** 3)  # Convert bytes to GB
    used_space = disk_info.used / (1024 ** 3)    # Convert bytes to GB
    free_space = disk_info.free / (1024 ** 3)    # Convert bytes to GB

    print(disk_info)

    return total_space, used_space, free_space

if __name__ == "__main__":
    total, used, free = get_disk_space_GB()
    print(f"Total disk space: {total:.2f} GB")
    print(f"Used disk space: {used:.2f} GB")
    print(f"Free disk space: {free:.2f} GB")