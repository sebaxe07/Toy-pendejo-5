# setup.py

from setuptools import setup, find_packages

setup(
    name='my_python_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'my_python_project = my_python_project.main:main',
        ],
    },
)
