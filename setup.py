import os

from setuptools import setup, find_packages

from Cython.Build import cythonize


setup(
    name='pyipv8-serializer',
    version=os.environ.get('APPVEYOR_REPO_TAG_NAME'),
    packages=find_packages(),
    ext_modules=cythonize('pyipv8_serializer.py'),
)
