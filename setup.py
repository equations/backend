# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='eqs_backend',
    version='0.0.1',
    description='Backend for the Equations database',
    long_description=readme,
    author='Herman Bergwerf',
    author_email='hermanbergwerf@gmail.com',
    url='https://github.com/equations/backend',
    license=license,
    packages=find_packages(exclude=('tests', 'doc'))
)
