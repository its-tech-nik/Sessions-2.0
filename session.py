import click

def allow_only(allowables, locals):
    allowable_count = 0
    for a in allowables:
        if a in locals:
            allowable_count += 1
    return len(locals) > 0 and allowable_count == len(locals)

class Config(object):
    def __init(self):
        self.n = None

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.command()
@click.option('-s', 'store', default=None, type=click.STRING, help='Store a session')
@click.option('-r', 'restore', default=None, type=click.STRING, help='Restore a session')
@click.option('-i', 'ignore', default=None, type=click.STRING, help='Ignores from storing an app in a session')
@click.option('-n', 'name', default=None, type=click.STRING, help='Used only with -i to specify a session name')
@click.option('-ls', 'list_sessions', default=None, type=click.STRING, help='List all active sessions')
@click.option('-a', 'list_all_apps', default=None, type=click.STRING, help='Display all running apps')
# @click.option('-d', default=None, type=click.STRING, help='Decouples storage of apps from browser tabs')
def cli(store, restore, ignore, name, list_sessions, list_all_apps):
    f_params = [v for v in locals().keys() if not v == 'config']
    params = []
    for v in f_params:
        if not locals()[v] is None:
            params.append(v)

    if allow_only(['ignore', 'name'], params):
        # ignore files
        print('IGNORE')
    elif allow_only(['store'], params):
        # store a session
        print('STORE')
    elif allow_only(['restore'], params):
        # restore a session
        print('RESTORE')
    elif allow_only(['list_all_apps'], params):
        # show all running apps
        print('LIST ALL APPS')
    elif allow_only(['list_sessions'], params):
        # list all active sessions
        print('LIST SESSIONS')
    # elif allow_only(['d'], params):
    #     decouples storage of apps from browser
    #     pass
    else:
        print('Wrong format. Please check your syntax')
