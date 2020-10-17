import clipboard, os
from Entity import Entity

class Browser(Entity):
    def store(self):
        print(f'Browser: We are about to store the session {self.session_name} in {self.file_storage}')

        if not self.clipboard_verified():
            print('Error: Not enough tabs found in the clipboard.')
            return

        text_in_clipboard = clipboard.paste()

        file = self.format_file_name(f'{self.session_name}-browser.ses')

        with open(file, "w") as text_file:
            text_file.write("%s" % text_in_clipboard)

    def restore(self):
        print(f'Browser: We are about to restore the session {self.session_name}')

    def list_running_apps(self):
        print('Browser: We are about to list all the running apps')

    def list_active_sessions(self):
        print('Browser: We are about to list all the active sessions')

    def clipboard_verified(self):
        links = clipboard.paste()

        links = links.split('\n')

        for link in links[:-1]:
            if not (link.startswith('http://') or link.startswith('https://')):
                return False

        return len(links) > 3


