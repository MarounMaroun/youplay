from setuptools import setup

setup(
    name='youplay',
    version='0.1',
    packages=['youplay'],
    entry_points={
        'console_scripts': [
            'youplay=youplay.youplay:main',
        ],
    }
)
