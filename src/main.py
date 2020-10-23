import click
from .app import App
from .app.Helpers import allow_only, clear_params

@click.command()
@click.option('-s', 'store', default=None, type=click.STRING, help='Store a session')
@click.option('-r', 'restore', default=None, type=click.STRING, help='Restore a session')
@click.option('-i', 'ignore', default=None, type=click.STRING, help='Ignores apps from ever being stored in a session', multiple=True)
@click.option('-n', 'name', default=None, type=click.STRING, help='Used only with -i to specify a session name')
@click.option('-a', 'list_all_apps', is_flag=True, help='Display all running apps')
@click.option('-ls', 'list_sessions', is_flag=True, help='List all active sessions')
# @click.option('-d', default=None, type=click.STRING, help='Decouples storage of apps from browser tabs')
def cli(store, restore, ignore, name, list_all_apps, list_sessions):
    params = clear_params(locals())
    session_name = store or restore or name

    app1 = App(session_name)

    if allow_only(['ignore', 'name'], params):
        if not ignore or not name:
            return

        app1.ignore(ignore)

    elif allow_only(['store'], params):
        # store a session
        app1.store()

    elif allow_only(['restore'], params):
        # restore a session
        app1.restore()

    elif allow_only(['list_all_apps'], params):
        # show all running apps
        app1.list_running_apps()

    elif allow_only(['list_sessions'], params):
        # list all active sessions
        app1.list_active_sessions()

    # elif allow_only(['d'], params):
    #     decouples storage of apps from browser
    #     pass
    else:
        print('Wrong format. Please check your syntax')