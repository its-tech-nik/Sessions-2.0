from setuptools import setup

setup(
    name='Session 2.0',
    py_modules=['session'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        session=session:cli
    '''
)
