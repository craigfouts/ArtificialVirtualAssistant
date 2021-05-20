from setuptools import setup, find_packages

with open('README.rst') as file:
    readme = file.read()

with open('LICENSE') as file:
    license = file.read()

setup(
    name='Artificial-Virtual-Assistant',
    version='1.0',
    description='Artificial virtual assistant.',
    long_description=readme,
    author='Craig Fouts',
    author_email='foutscw@gmail.com',
    url='https://github.com/foutscw/Artificial-Virtual-Assistant',
    packages=find_packages(exclude=('docs', 'tests')),
    license=license
)
