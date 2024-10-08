from setuptools import setup, find_packages

setup(
    name = 'example',
    version = '0.2', 
    packages = find_packages(exclude=['tests*']),
    license='MIT',
    description = 'example calculator package', 
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'url',
    author = 'Claudia', 
    author_email = 'email'
)