import argparse
from .dependency import find_dependencies


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('entrypoint', help='path to python script')
    args = parser.parse_args()

    deps = find_dependencies(args.entrypoint)
    for f in deps:
        print(f)
