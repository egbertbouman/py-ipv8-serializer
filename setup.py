from setuptools import setup, find_packages

from Cython.Build import cythonize


setup(
    name='pyipv8-serializer',
    version='2.4.1535',
    packages=find_packages(),
    ext_modules=cythonize('pyipv8_serializer.py'),
)
