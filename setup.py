#!/usr/bin/env python

from setuptools import setup, find_packages
#from distutils.core import setup
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
    #package_dir=['pdbremix',],
    packages=find_packages(where='pdbremix')
    #package_dir = {'pdbremix': 'pdbremix'}
    
    include_package_data=True,
    #scripts=glob.glob('bin/*'),
)
