import sys
import types
from importlib.util import spec_from_file_location, module_from_spec


def find_dependencies(entrypoint):
    # TODO: configure
    sys.path.append('')

    spec = spec_from_file_location('', entrypoint)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    visited = set()
    dfs(module, visited)
    return list(visited)


def dfs(module, visited: set):
    if not isinstance(module, types.ModuleType):
        return

    if not hasattr(module, '__file__'):
        return

    if module.__file__ in visited:
        return

    visited |= {module.__file__}
    for v in module.__dict__.values():
        dfs(v, visited)
