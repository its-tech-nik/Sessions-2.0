from Entity import Entity
import getpass
import sys, subprocess, os

class Software(Entity):
    def __init__(self, session_name):
        super().__init__(session_name)
        self.ignoreFile = self.format_file_name('sessions.ignore')
        self.file = self.format_file_name(f'{self.session_name}-software.ses')

    def ignore(self, ignored_app):
        if not ignored_app in self.running_apps():
            print('Error: This app is not running at the moment.')
            return

        print(f'Software: We are about to ignore the app {ignored_app}')

        ignored_apps = self.retrieve_ignored_apps()

        if ignored_app in ignored_apps:
            ignored_apps.remove(ignored_app)
        else:
            ignored_apps.append(ignored_app)

        with open(self.ignoreFile, 'w') as text_file:
            for app in ignored_apps:
                text_file.write(f'{app}\n')

    def store(self):
        print(f'Software: We are about to store the session {self.session_name} in {self.file_storage}')
        
        # file = self.format_file_name(f'{self.session_name}-software.ses')
        ignored_apps = self.retrieve_ignored_apps()

		# store all runing apps that are not ignored
        with open(self.file, 'w') as text_file:
            for app in self.running_apps():
                if not app in ignored_apps:
                    text_file.write(f'{app}\n')

    def restore(self):
        print(f'Software: We are about to restore the session {self.session_name}')

    def list_running_apps(self):
        print('Software: We are about to list all the running apps')

    def list_active_sessions(self):
        print('Software: We are about to list all the active sessions')

    def running_apps(self):
        user = getpass.getuser()
        command = f'ps aux|grep ^{user} | grep /Applications'
        
        output = subprocess.check_output(command, shell=True)
        running_apps = []
        
        for line in str(output).split('\\n'):
            x = line[line.find('/Applications'):]
            y = x[:x.find('.app')]
            z = y[y.rfind('/')+1:]
            if not z in running_apps and z != '' and z != 'Application':
                running_apps.append(z)

        return running_apps

    def retrieve_ignored_apps(self):
        ignored_apps = []

        if os.path.isfile(self.ignoreFile):
            with open(self.ignoreFile, 'r') as text_file:
                for app in text_file:
                    ignored_apps.append(app.replace('\n', ''))
        
        return ignored_apps

