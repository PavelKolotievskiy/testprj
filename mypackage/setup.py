from setuptools import setup

setup(
    name='src',
    version='1.0',
    author='pk',
    packages=['src'],
    packafe_data={'': ['*.txt']},
    entry_points={'console_scripts': ['src = src.mydate:curdate']},
)
