import argparse
from pathlib import Path
from .dependency import find_dependencies
from .presenter import Presenter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('entrypoint', help='path to python script')
    args = parser.parse_args()

    deps = find_dependencies(Path(args.entrypoint))
    presenter = Presenter()
    deps = presenter.convert(deps)

    for f in deps:
        print(f)
