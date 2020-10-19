from Entity import Entity
import os
from Helpers import DEV_MODE, running_from, running_apps

class Software(Entity):
    def __init__(self, session_name):
        super().__init__(session_name)
        self.ignoreFile = self.format_file_name('sessions.ignore')
        self.file = self.format_file_name(f'{self.session_name}-software.ses')

    def ignore(self, to_be_ignored_apps):
        # TODO: Create an error message for when an app does not exist in the installed apps

        for ignored_app in to_be_ignored_apps:
            if not ignored_app in running_apps():
                print('Error: This app is not running at the moment.')
                self.list_running_apps()
                print('Choose an app of the above to ignore')
                return

        ignored_apps = self.retrieve_ignored_apps()
        
        for ignored_app in to_be_ignored_apps:
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
            for app in running_apps():
                if not app in ignored_apps:
                    text_file.write(f'{app}\n')
        
        self.close_apps()

    def restore(self):
        apps_to_be_loaded = list()

        with open(self.file, 'r') as text_file:
            for application in text_file:
                apps_to_be_loaded.append(application.split('\n')[0] + '.app')

        for app in apps_to_be_loaded:
            os.system('open -a ' + app.replace(' ', '\\ '))

    def list_running_apps(self):
        ignored_apps = self.retrieve_ignored_apps()
        show_last = []

        for app in running_apps():
            if app in ignored_apps:
                show_last.append(app)
            else:
                print(app)

        for app in show_last:
            print(app, '(Ignored)')

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

    def retrieve_ignored_apps(self):
        ignored_apps = []

        if os.path.isfile(self.ignoreFile):
            with open(self.ignoreFile, 'r') as text_file:
                for app in text_file:
                    ignored_apps.append(app.replace('\n', ''))
        
        return ignored_apps

    def close_apps(self):
        print('Closing all apps')
        
        last_app = running_from()

        with open(self.file, "r") as text_file:
            for application in text_file:
                application = application.split('\n')[0]
                if not application == last_app:
                    if not DEV_MODE:
                        os.system('osascript -e \'quit app "{0}"\''.format(application + '.app'))
                    else:
                        print('osascript -e \'quit app "{0}"\''.format(application + '.app'))

        print(f'Are you sure you want to terminate: {last_app}? [Y/n]')
        user_input = input()
        if user_input.lower() == 'y':
            if not DEV_MODE:
                os.system('osascript -e \'quit app "{0}"\''.format(last_app + '.app'))
            else:
                print('osascript -e \'quit app "{0}"\''.format(last_app + '.app'))
