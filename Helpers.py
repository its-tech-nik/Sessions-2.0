import os

# create empty file
def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

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

def return_set_variable(*args):
    for i in args:
        if i:
            return i
