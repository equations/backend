# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='template',
    version='0.0.1',
    description='Herman Bergwerfs Python package template',
    long_description=readme,
    author='Herman Bergwerf',
    author_email='hermanbergwerf@gmail.com',
    url='https://github.com/hermanbergwerf/python-template',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
