from appdirs import AppDirs

class Software():
    def __init__(self, session_name=None):
        self.session_name = session_name
        self.file_storage = AppDirs('Sessions').user_data_dir

    def ignore(self, ignored_app):
        print(f'We are about to ignore the app {ignored_app}')

    def store(self):
        print(f'We are about to store the session {self.session_name} in {self.file_storage}')

    def restore(self):
        print(f'We are about to restore the session {self.session_name}')

    def list_running_apps(self):
        print('We are about to list all the running apps')

    def list_active_sessions(self):
        print('We are about to list all the active sessions')
