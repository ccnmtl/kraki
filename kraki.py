import requests
import os.path
import sys

def get_api_key():
    with open(os.path.expanduser("~/.kraki_api_key.txt"), "r") as kfile:
        return kfile.read()


def run(API_KEY, action, deployment_id):
    if action != "push":
        print "sorry, so far kraki only supports pushing"
        return
    push(API_KEY, deployment_id)

def push(API_KEY, deployment_id):
    url = "https://rolf.ccnmtl.columbia.edu/api/1.0/push/"
    r = requests.post(url, params=dict(API_KEY=API_KEY,
                                       deployment_id=deployment_id),
                      verify=False)
    print r.status_code

if __name__ == "__main__":
    try:
        API_KEY = get_api_key()
    except IOError:
        print "Could not read API KEY from ~/.kraki_api_key.txt"
        sys.exit(1)
    
    if len(sys.argv) < 3:
        print "not enough arguments"
        print "kraki.py ACTION DEPLOYMENT_ID"
        sys.exit(1)
    action = sys.argv[1]
    deployment_id = sys.argv[2]

    run(API_KEY, action, deployment_id)
    
