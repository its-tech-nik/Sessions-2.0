# Sessions-2.0
The improved sessions.

# How to install the command with pipenv (can only be used when the environment is running)
- pip install pipenv (if it is not already installed)
- pipenv shell (if pipenv is not activated yet)
- pipenv install -e .

# How to use the command:
session [options]

Options | What it does
:--- | :---
-**s** [session_name] | Stores a session with name [session_name]
-**r** [session_name] | Restores a session with name [session_name]
-**i** [app_name] -i [session_name] | Ignores from storing an app in a session with name [app_name]
-**la** | Lists all active sessions
-**a** | Displays all running apps
-**d** | Decouples storage of apps from browser tabs  
