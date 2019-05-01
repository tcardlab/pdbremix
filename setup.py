#!/usr/bin/env python
'''NOW FUNCTIONAL... I THINK'''
#from distutils.core import setup
from setuptools import setup, find_packages
import glob

#version = open('pdbremix/_version.py').read().split()[-1][1:-1]

setup(
    name='pdbremix',
    version='1.0',
    author='Bosco Ho',
    author_email='boscoh@gmail.com',
    url='http://github.com/boscoh/pdbremix',
    description='structural biology library',
    long_description='Docs at http://github.com/boscoh/pdbremix',
    license='MIT',
    install_requires=[],
    packages=find_packages(where='pdbremix.pdbremix'),
    scripts=glob.glob('bin/*'),
    include_package_data=True,
)

#package_dir=['pdbremix',],
#package_dir = {'pdbremix': 'pdbremix'}
#package_dir={'': 'pdbremix'}
