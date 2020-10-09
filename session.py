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
@click.option('-s', default=None, type=click.STRING, help='Store a session')
@click.option('-r', default=None, type=click.STRING, help='Restore a session')
@click.option('-i', default=None, type=click.STRING, help='Ignores from storing an app in a session')
@click.option('-n', default=None, type=click.STRING, help='Used only with -i to specify a session name')
@click.option('-la', default=None, type=click.STRING, help='List all active sessions')
@click.option('-a', default=None, type=click.STRING, help='Display all running apps')
# @click.option('-d', default=None, type=click.STRING, help='Decouples storage of apps from browser tabs')
def cli(s, r, i, n, la, a):
    f_params = [v for v in locals().keys() if not v == 'config']
    params = []
    for v in f_params:
        if not locals()[v] is None:
            params.append(v)

    if allow_only(['i', 'n'], params):
        # ignore files
        print('I')
    elif allow_only(['s'], params):
        # store a session
        print('S')
    elif allow_only(['r'], params):
        # restore a session
        print('R')
    elif allow_only(['a'], params):
        # show all running apps
        print('A')
    elif allow_only(['la'], params):
        # list all active sessions
        print('LA')
    # elif allow_only(['d'], params):
    #     decouples storage of apps from browser
    #     pass
    else:
        print('Wrong format. Please check your syntax')
