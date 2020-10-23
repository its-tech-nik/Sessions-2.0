from appdirs import AppDirs

class Entity():
    def __init__(self, session_name):
        self.session_name = session_name
        self.file_storage = AppDirs('Sessions').user_data_dir

    def format_file_name(self, file_name):
        delimeter = '/' if '/' in self.file_storage else '\\'

        return delimeter.join([self.file_storage, file_name])
