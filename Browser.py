import clipboard, os, webbrowser, sys
from Entity import Entity

class Browser(Entity):

    def __init__(self, session_name):
        super().__init__(session_name)
        self.file = self.format_file_name(f'{self.session_name}-browser.ses')

    def store(self):
        if not self.clipboard_verified():
            print('Error: Not enough tabs found in the clipboard.')
            print('Do you want to store only the software running? [Y/n]')
            user_input = input()
            if user_input.lower() == 'y':
                return
            sys.exit()

        text_in_clipboard = clipboard.paste()

        with open(self.file, 'w') as text_file:
            text_file.write(f'{text_in_clipboard}')

    def restore(self):
        with open(self.file, 'r') as text_file:
            for l in text_file:
                webbrowser.open(l.replace('\n', ''), new=2)

    def clipboard_verified(self):
        links = clipboard.paste()

        links = links.split('\n')

        for link in links[:-1]:
            if not (link.startswith('http://') or link.startswith('https://')):
                return False

        return len(links) > 3


