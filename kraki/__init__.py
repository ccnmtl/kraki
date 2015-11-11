import requests
import os.path
from blessings import Terminal
import sys
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

term = Terminal()

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
            print term.red("sorry, so far kraki only supports pushing")
            return
        self.push(deployment_id)

    def push(self, deployment_id):
        url = ("%s/api/1.0/deployment/%d/push/"
               % (self.ROLF_BASE, int(deployment_id)))
        r = requests.post(url,
                          headers=dict(ROLF_API_KEY=self.API_KEY),
                          verify=False)

        if r.status_code != 200:
            print term.red(str(r.status_code))
            print term.red(str(r.content))
            return

        for stage in r.json()['stages']:
            print term.bold("\n=== STAGE: %s ===" % stage['name'])
            sr = requests.post(
                self.ROLF_BASE + stage['url'],
                headers=dict(ROLF_API_KEY=self.API_KEY),
                verify=False)
            if sr.status_code != 200:
                print term.red("!!! Error: %d" % sr.status_code)
                print term.red(r.content)
                sys.exit(1)
            if sr.json()['status'] != 'ok':
                print term.red("!!! Stage failed")
                for l in sr.json()['logs']:
                    print_log(l)
                sys.exit(1)
            print term.green("Stage succeeded")
            for l in sr.json()['logs']:
                print_log(l)


def print_log(l):
    if 'command' in l:
        print term.cyan("--- Command ---")
        print term.cyan(indent(l['command'], ">>> "))
    if 'stdout' in l and l['stdout'] != u'':
        print term.magenta("--- STDOUT ---")
        print indent(l['stdout'].encode('ascii', 'ignore'))
    if 'stderr' in l and l['stderr'] != u'':
        print term.yellow('--- STDERR ---')
        print indent(l['stderr'].encode('ascii', 'ignore'))


def indent(t, prefix="    "):
    return '\n'.join([prefix + l for l in t.splitlines()])
