from setuptools import setup

setup(
    name="Session 2.0",
    py_modules=["session"],
    install_requires=["click", "appdirs", "clipboard"],
    entry_points="""
        [console_scripts]
        session=session:cli
    """,
)
