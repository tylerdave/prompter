# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import prompter

setup(
    name='prompter',
    version=prompter.__version__,
    description='Simple CUI input prompt',
    author='Dave Forgac',
    author_email='tylerdave@tylerdave.com',
    url='https://github.com/tylerdave/prompter',
    packages=find_packages(),
    include_package_data=False,
    install_requires=[],
    license='MIT',
)
