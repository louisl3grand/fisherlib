import setuptools
from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration
import glob
with open("README.md", "r") as fh:
    long_description = fh.read()


def configuration(parent_package='', top_path=''):
    config = Configuration('', parent_package, top_path)
    return config

setup(
    name='Fisherlib',
    version='0.1',
    packages=['fishlib'],
    url='https://github.com/louisl3grand/fisherlib',
    author='Louis Legrand',
    author_email='to.louis.legrand@unige.ch',
    description='Useful functions for fisher analysis',
    install_requires=['numpy'],
    long_description=long_description,
    configuration=configuration)

