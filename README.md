# Sessions-2.0
The improved sessions

# How to install the command
- virtualenv venv
- . venv/bin/activate
- pip install --editable .

# How to use the command:
sh session [options]  
**Currently, if you want to use the command, you have to go inside the folder and follow the instructions from there. There is a ticket in the todos list to tackle this problem.**


Options | What it does
:--- | :---
-**s** [session_name] | Stores a session with name [session_name]
-**r** [session_name] | Restores a session with name [session_name]
-**i** [app_name] -**n** [session_name] | Ignores from storing an app in a session with name [app_name], when no [app_name] is provided lists all running apps
-**la** | Lists all active sessions
-**a** | Displays all running apps
-**d** | Decouples storage of apps from browser tabs  
