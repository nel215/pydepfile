import os
import sys
import types
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec


class Dependency:

    def __init__(self, path: Path, is_child: bool):
        self.path = path
        self.is_child = is_child

    def __repr__(self):
        return str(self.__dict__.copy())


def convert(deps):
    cwd = os.getcwd()
    res = []
    for dep in deps:
        is_child = dep.find(cwd) == 0
        res.append(Dependency(Path(dep), is_child))

    return res


def find_dependencies(entrypoint: str):
    entrypoint = Path(entrypoint).absolute()
    sys.path.append(str(entrypoint.parent))

    spec = spec_from_file_location('', entrypoint)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    deps = dfs(module)
    deps = convert(deps)

    return deps


def dfs(module):
    visited = set()
    _dfs(module, visited)
    return list(visited)


def _dfs(module, visited: set):
    if not isinstance(module, types.ModuleType):
        return

    if not hasattr(module, '__file__'):
        return

    if module.__file__ in visited:
        return

    visited |= {module.__file__}
    for v in module.__dict__.values():
        _dfs(v, visited)
