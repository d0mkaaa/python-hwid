import hashlib
import os, platform

def get_hwid():
    node = os.getenv("computername") + platform.processor() + os.getenv("SystemDrive")
    hwid = hashlib.sha256(node.encode()).hexdigest()
    return hwid

# Main program
if __name__ == "__main__":
    hwid = get_hwid()
    print("Your HWID is:", hwid)