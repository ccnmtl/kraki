import requests
import os.path
import sys

def get_api_key():
    with open(os.path.expanduser("~/.kraki_api_key.txt"), "r") as kfile:
        return kfile.read()

if __name__ == "__main__":
    try:
        API_KEY = get_api_key()
    except IOError:
        print "Could not read API KEY from ~/.kraki_api_key.txt"
        sys.exit(1)
    
