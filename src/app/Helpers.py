import os, sys, subprocess, urllib
import getpass
from AppKit import NSWorkspace

DEV_MODE=False

# create empty file
def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def allow_only(allowables, locals):
    allowable_count = 0
    for a in allowables:
        if a in locals:
            allowable_count += 1
    return len(locals) > 0 and allowable_count == len(locals)

def clear_params(locals):
    params = []

    for v in locals:
        if not locals[v] is None and locals[v]:
            params.append(v)

    return params

def running_processes():
    user = getpass.getuser()
    command = f'ps aux|grep ^{user} | grep /Applications'
    
    output = subprocess.check_output(command, shell=True)

    return str(output).split('\\n')

def clearURL(asdf):
    return urllib.parse.unquote(str(asdf)).split('/')

def get_login_items():
    login_apps = subprocess.check_output(['osascript', '-e',
                                    'tell application "System Events" to get the path of every login item']).decode('utf-8').split(',')
    
    login_apps = [clearURL(i.split('\n')[0])[-1] for i in login_apps]
    login_apps = [clearURL(i.split('.app')[0])[-1] for i in login_apps]

    return login_apps

def running_apps(specific_app=None):

    processes = running_processes()
    running_apps = []
    login_apps = get_login_items()
    
    for line in processes:
        x = line[line.find('/Applications'):]
        y = x[:x.find('.app')]
        z = y[y.rfind('/')+1:]
        if specific_app and specific_app in line:
            return z
        if not z in running_apps and z != '' and z != 'Application' and z not in login_apps:
            running_apps.append(z)

    return running_apps

def running_from():
    app = running_apps(str(subprocess.check_output('echo $TERM_PROGRAM', shell=True).split()).split('\'')[1])

    if type(app) == list:
        return app[0]

    return app
