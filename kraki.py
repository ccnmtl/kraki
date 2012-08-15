import requests
import os.path
import sys


def read_config():
    with open(os.path.expanduser("~/.kraki_config.txt"), "r") as kfile:
        fields = dict()
        for line in kfile.readlines():
            k, v = [p.strip() for p in line.strip().split("=")]
            fields[k] = v
        return fields['API_KEY'], fields['ROLF_BASE']


class RolfClient(object):
    def __init__(self, ROLF_BASE, API_KEY):
        self.ROLF_BASE = ROLF_BASE
        self.API_KEY = API_KEY

    def run(self, action, deployment_id):
        if action != "push":
            print "sorry, so far kraki only supports pushing"
            return
        self.push(deployment_id)

    def push(self, deployment_id):
        url = ("%s/api/1.0/deployment/%d/push/"
               % (self.ROLF_BASE, int(deployment_id)))
        r = requests.post(url,
                          params=dict(API_KEY=self.API_KEY),
                          verify=False)
        print r.status_code


if __name__ == "__main__":
    try:
        API_KEY, ROLF_BASE = read_config()
    except IOError:
        print "Could not read API KEY from ~/.kraki_config.txt"
        sys.exit(1)

    if len(sys.argv) < 3:
        print "not enough arguments"
        print "kraki.py ACTION DEPLOYMENT_ID"
        sys.exit(1)
    action = sys.argv[1]
    deployment_id = sys.argv[2]
    r = RolfClient(ROLF_BASE, API_KEY)
    r.run(action, deployment_id)
