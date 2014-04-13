# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import prompter

with open('README.rst') as f:
    readme = f.read()

setup(
    name='prompter',
    version=prompter.__version__,
    description='Simple CUI input prompt',
    long_description=readme,
    author='Dave Forgac',
    author_email='tylerdave@tylerdave.com',
    url='https://github.com/tylerdave/prompter',
    packages=find_packages(),
    include_package_data=False,
    install_requires=[],
    license='MIT',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
        )

)
