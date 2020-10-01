#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='nda',
    version='0.0.1',
    description='Datajoint schemas and related methods for MICrONS phase3',
    author='Stelios Papadopoulos',
    author_email='spapadop@bcm.edu',
    packages=find_packages(exclude=[]),
    install_requires=['numpy', 'tqdm', 'scipy', 'pandas', 'datajoint', 'pykdtree', 'ipyvolume', 'matplotlib', 'decorator', 'torch', 'cloud-volume']
)
