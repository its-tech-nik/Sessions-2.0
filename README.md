# Sessions-2.0
The improved sessions.

# How to install the command for development
- `pip install pipenv` if you have not installed it, yet
- `pipenv shell` to activate the environment
- `pipenv install -e .` to install the command and use it "session [option]" (don't forget to use -e flag to activate the editable mode)

# How to use the command:
session [options]

Options | What it does
:--- | :---
-**s** [session_name] | Stores a session with name [session_name]
-**r** [session_name] | Restores a session with name [session_name]
-**i** [app_name] -i [session_name] | Ignores from storing an app in a session with name [app_name]
-**ls** | Lists all active sessions
-**a** | Displays all running apps
