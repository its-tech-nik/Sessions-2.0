import sys

class App():
    def __init__(self, session_name=None):
        self.session_name = session_name
        print('init')

    def check_for_session_name(self):
        if not self.session_name:
            print('Session name not provided. You cannot use this method without passing a session name in the constructor')
            sys.exit()

    def ignore(self, ignored_app):
        
        self.check_for_session_name()

        print(f'We are about to ignore the app {ignored_app}')

    def store(self):
        self.check_for_session_name()

        print(f'We are about to store the session {self.session_name}')

    def restore(self):
        self.check_for_session_name()

        print(f'We are about to restore the session {self.session_name}')

    def list_running_apps(self):
        print('We are about to list all the running apps')

    def list_active_sessions(self):
        print('We are about to list all the active sessions')

    
