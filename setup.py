# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in stockmarket/__init__.py
from linefood import __version__ as version

setup(
	name='linefood',
	version=version,
	description='linefood application ',
	author='ahmadragheb',
	author_email='ahmedragheb75@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
