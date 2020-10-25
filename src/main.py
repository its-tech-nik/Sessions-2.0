import click
from .app import App
from .app.Helpers import allow_only, clear_params

def get_app_not_ignored(ctx, args, incomplete):

    app = App()

    return [c for c in app.show_only_apps_not_ignored() if incomplete in c[0]]

def get_active_sessions(ctx, args, incomplete):
    app = App()
    active = app.show_active_sessions()
    asdf = active if len(active) > 0 else ['No Active Sessions']

    return [c for c in asdf if incomplete in c[0]]


@click.command()
@click.option('-s', 'store', default=None, type=click.STRING, help='Store a session', autocompletion=get_active_sessions)
@click.option('-r', 'restore', default=None, type=click.STRING, help='Restore a session', autocompletion=get_active_sessions)
@click.option('-i', 'ignore', default=None, type=click.STRING, help='Ignores apps from ever being stored in a session', multiple=True, autocompletion=get_app_not_ignored)
@click.option('-n', 'name', default=None, type=click.STRING, help='Used only with -i to specify a session name', autocompletion=get_active_sessions)
@click.option('-a', 'list_all_apps', is_flag=True, help='Display all running apps')
@click.option('-ls', 'list_sessions', is_flag=True, help='List all active sessions')
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
    else:
        print('Wrong format. Please check your syntax')
