import sys, appdirs, os
from appdirs import AppDirs

class HelperFunctions():
    def touch(self, path):
        with open(path, 'a'):
            os.utime(path, None)

    def check_for_session_name(self, session_name):
        if not session_name:
            print('Session name not provided. You cannot use this method without passing a session name in the constructor')
            sys.exit()

Helpers = HelperFunctions()

class App():

    def __init__(self, session_name=None):
        self.session_name = session_name
        self.file_storage = AppDirs('Sessions').user_data_dir



    def ignore(self, ignored_app):
        Helpers.check_for_session_name(self.session_name)

        print(f'We are about to ignore the app {ignored_app}')

    def store(self):
        Helpers.check_for_session_name(self.session_name)

        print(f'We are about to store the session {self.session_name} in {self.file_storage}')

    def restore(self):
        Helpers.check_for_session_name(self.session_name)

        print(f'We are about to restore the session {self.session_name}')

    def list_running_apps(self):
        print('We are about to list all the running apps')

    def list_active_sessions(self):
        print('We are about to list all the active sessions')

    
