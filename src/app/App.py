import sys, appdirs, os, clipboard
from appdirs import AppDirs
from .Helpers import touch
from .Entity import Browser
from .Entity import Software

class App():
    def __init__(self, session_name=None):
        self.session_name = session_name
        self.file_storage = AppDirs('Sessions').user_data_dir
        self.browser = Browser(self.session_name)
        self.software = Software(self.session_name)

        if not session_name:
            return

        # create session directory
        if not os.path.exists(self.file_storage):
            os.mkdir(self.file_storage)
        
        if self.session_name:
            self.create_file('.ignore')
            self.create_file(f'{self.session_name}-browser.ses')
            self.create_file(f'{self.session_name}-software.ses')

    def create_file(self, file_name):
        delimeter = '/' if '/' in self.file_storage else '\\'

        file = delimeter.join([self.file_storage, file_name])

        if not os.path.exists(file):
            touch(file)

    def ignore(self, ignored_app):
        self.software.ignore(ignored_app)

    def store(self):
        self.browser.store()
        self.software.store()

    def restore(self):
        self.browser.restore()
        self.software.restore()

    def list_running_apps(self):
        print('We are about to list all the running apps')
        self.software.list_running_apps()

    def list_active_sessions(self):
        print('We are about to list all the active sessions')
        self.software.list_active_sessions()

    def show_only_apps_not_ignored(self):
        return self.software.show_only_apps_not_ignored()

    def show_active_sessions(self):
        return self.software.active_sessions()
