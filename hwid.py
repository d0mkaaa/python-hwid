import hashlib
import requests
import time

def get_hwid():
    import os, platform
    node = os.getenv("computername") + platform.processor() + os.getenv("SystemDrive")
    hwid = hashlib.sha256(node.encode()).hexdigest()
    return hwid

def check_hwid(hwid):
    # Check the hardware ID against a list stored in a text file
    try:
        with open("hwid_list.txt", "r") as file:
            for line in file:
                if hwid in line:
                    return True
        return False
    except:
        return False

def check_hwid_online(hwid):
    # Check the hardware ID against a list stored on a website
    try:
        headers = {
            "Authorization": "Token <your api key>"
        }
        response = requests.get("https://hastebin.com", headers=headers)
        if response.status_code == 200:
            for line in response.text.splitlines():
                if hwid in line:
                    return True
        return False
    except:
        return False

# Main program
if __name__ == "__main__":
    hwid = get_hwid()
    if check_hwid(hwid) or check_hwid_online(hwid):
        print("Your HWID is on the list. The program can run.")
        # Insert the code for your program here
    else:
        print("Your HWID is not allowed. Your HWID is:", hwid)
        time.sleep(10)
        exit()
