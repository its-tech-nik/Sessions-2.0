from Entity import Entity
import getpass
import sys, subprocess, os

class Software(Entity):
    def __init__(self, session_name):
        super().__init__(session_name)
        self.ignoreFile = self.format_file_name('sessions.ignore')
        self.file = self.format_file_name(f'{self.session_name}-software.ses')

    def ignore(self, ignored_app):
        # TODO: Create an error message for when an app does not exist in the installed apps
        if not ignored_app in self.running_apps():
            print('Error: This app is not running at the moment.')
            self.list_running_apps()
            print('Choose an app of the above to ignore')
            return

        ignored_apps = self.retrieve_ignored_apps()

        if ignored_app in ignored_apps:
            ignored_apps.remove(ignored_app)
        else:
            ignored_apps.append(ignored_app)

        with open(self.ignoreFile, 'w') as text_file:
            for app in ignored_apps:
                text_file.write(f'{app}\n')

    def store(self):
        ignored_apps = self.retrieve_ignored_apps()

		# store all runing apps that are not ignored
        with open(self.file, 'w') as text_file:
            for app in self.running_apps():
                if not app in ignored_apps:
                    text_file.write(f'{app}\n')
        
        # TODO: close the apps

    def restore(self):
        apps_to_be_loaded = list()

        with open(self.file, 'r') as text_file:
            for application in text_file:
                apps_to_be_loaded.append(application.split('\n')[0] + '.app')

        for app in apps_to_be_loaded:
            os.system('open -a ' + app.replace(' ', '\\ '))

    def list_running_apps(self):
        ignored_apps = self.retrieve_ignored_apps()

        for app in self.running_apps():
            print(app, '(Ignored)' if app in ignored_apps else '')

    def list_active_sessions(self):
        active_sessions = self.active_sessions()

        if len(active_sessions) == 0:
            print('Active Sessions: (no active sessions)')
            return

        print('Active Sessions:')

        for session in active_sessions:
            print(session)

    def active_sessions(self):
        application_folder = os.listdir(self.file_storage)

        return list(set([f.split('-')[0] for f in application_folder if f.endswith('.ses')]))

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

