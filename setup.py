# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:06:08 2021

@author: Vishwesh
"""
import pathlib
from setuptools import setup, find_packages

#HERE = pathlib.Path(__file__).parent

VERSION = '0.3'
PACKAGE_NAME = 'Logic_Py'
AUTHOR = 'Vishwesh'
AUTHOR_EMAIL = 'vishwesh.arush@mail.com'
URL = 'https://github.com/vishwesh-vishwesh/Logic_Py'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Basic and Combinational logic gates'
LONG_DESCRIPTION = 'file: README.md'
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
