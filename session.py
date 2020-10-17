import click
from App import App

def allow_only(allowables, locals):
    allowable_count = 0
    for a in allowables:
        if a in locals:
            allowable_count += 1
    return len(locals) > 0 and allowable_count == len(locals)

def clear_params(locals):
    params = []

    for v in locals:
        # print(locals[v])
        if not locals[v] is None and locals[v]:
            params.append(v)

    return params

class Config(object):
    def __init(self):
        self.n = None

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.command()
@click.option('-s', 'store', default=None, type=click.STRING, help='Store a session')
@click.option('-r', 'restore', default=None, type=click.STRING, help='Restore a session')
@click.option('-i', 'ignore', default=None, type=click.STRING, help='Ignores from storing an app in a session')
@click.option('-n', 'name', default=None, type=click.STRING, help='Used only with -i to specify a session name')
@click.option('-a', 'list_all_apps', is_flag=True, help='Display all running apps')
@click.option('-ls', 'list_sessions', is_flag=True, help='List all active sessions')
# @click.option('-d', default=None, type=click.STRING, help='Decouples storage of apps from browser tabs')
def cli(store, restore, ignore, name, list_all_apps, list_sessions):

    params = clear_params(locals())

    if allow_only(['ignore', 'name'], params):
        # ignore files
        if not ignore or not name:
            return
        
        app = App(name)
        app.ignore(ignore)

    elif allow_only(['store'], params):
        # store a session
        app = App(store)
        app.store()

    elif allow_only(['restore'], params):
        # restore a session
        app = App(restore)
        app.restore()

    elif allow_only(['list_all_apps'], params):
        # show all running apps
        app = App()
        app.list_running_apps()

    elif allow_only(['list_sessions'], params):
        # list all active sessions
        app = App()
        app.list_active_sessions()

    # elif allow_only(['d'], params):
    #     decouples storage of apps from browser
    #     pass
    else:
        print('Wrong format. Please check your syntax')
