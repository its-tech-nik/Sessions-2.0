from setuptools import setup
import subprocess
from setuptools.command.install import install

class InstallWrapper(install):
    """
    Overriding the default installation process in order
    to setup the tab completion script in the right folder
    with the appdirs module
    """
    def run(self):
        pass
        # from appdirs import AppDirs
        # file_storage = AppDirs('Sessions').user_data_dir
        # file_storage = file_storage.split()
        # file_storage = "\ ".join(file_storage)
        # subprocess.Popen(['bash', 'post-install.sh', f'\'{file_storage}\''])
        # install.run(self)


setup(
    name="Session 2.0",
    py_modules=["session"],
    install_requires=["click", "appdirs", "clipboard"],
    entry_points="""
        [console_scripts]
        session=src.main:cli
    """,
    include_package_data=True,
    cmdclass={
        'install': InstallWrapper
    },
)

