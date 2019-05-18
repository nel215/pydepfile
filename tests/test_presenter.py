import os
from pathlib import Path
from pydepfile.presenter import Presenter
from pydepfile.dependency import Dependency


def test_convert():
    presenter = Presenter()
    cwd = os.getcwd()
    deps = [
        Dependency(Path(cwd)/'a.txt', True),
        Dependency(Path('/tmp/b.txt'), False),
    ]
    res = presenter.convert(deps)
    assert res == ['a.txt']
