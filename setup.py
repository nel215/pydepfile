from setuptools import setup, find_packages
with open('pydepfile/version.py') as fp:
    version = fp.read().split('=')[1].strip()

setup(
    name='pydepfile',
    version=version,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pydepfile = pydepfile.main:main',
        ],
    },
)
