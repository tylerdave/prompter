"""
prompter CUI input prompts
~~~~~~~~~~~~~~~~~~~~~~~~~~

Prompter is a tool for displaying simple input prompts with optional defaults.

Usage:

    >>> from prompter import prompt, yesno

    >>> prompt('What is your name?')
    What is your name? Dave
    'Dave'

    >>> prompt('What is your name?', default='Jenn')
    What is your name? [Jenn]
    'Jenn'

    >>> prompt('What is your name?', default='Jenn', suffix='\n > ')
    What is your name? [Jenn]
     >
    'Jenn'

    >>> prompt('Enter text surrounded by spaces.', strip=False)
    Enter text surrounded by spaces.    text
    '   text   '

    >>> yesno('Really?')
    Really? [Y/n]
    True

    >>> yesno('Really?')
    Really? [Y/n] no
    False

    >>> yesno('Really?', default='no')
    Really? [y/N]
    True

    >>> yesno('')
    [Y/n] n
    False

:copyright: (c) 2014 by Dave Forgac
:license: MIT, see LICENSE file for details
"""
from __future__ import print_function

import re
import os
import readline

__title__ = 'prompter'
__author__ = 'Dave Forgac'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Dave Forgac'
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def get_input(message=None):
    """
    Get user input using raw_input() for Python 2.x and input() for 3.x.
    """
    try:
        return raw_input(message)
    except NameError:
        return input(message)


def prompt(
    message, default=None, strip=True, suffix=' ', input_required=True
):
    """
    Print a message and prompt user for input. Return user input.
    """
    if default is not None:
        prompt_text = "{0} [{1}]{2}".format(message, default, suffix)
    else:
        prompt_text = "{0}{1}".format(message, suffix)

    while True:
        input_value = get_input(prompt_text)

        if input_value and strip:
            input_value = input_value.strip()

        if not input_value:
            input_value = default

        if (
            (input_required is False) or
            ((input_required is True) and (input_value is not None))
        ):
            break

    return input_value


def yesno(message, default=None, suffix=' '):
    """
    Prompt user to answer yes or no. Return True if the default is chosen,
    otherwise False.
    """
    if default == 'yes':
        yesno_prompt = '[Y/n]'
    elif default == 'no':
        yesno_prompt = '[y/N]'
    elif default is None:
        yesno_prompt = '[y/n]'
    else:
        raise ValueError("default must be 'yes' or 'no'.")

    if message != '':
        prompt_text = "{0} {1}{2}".format(message, yesno_prompt, suffix)
    else:
        prompt_text = "{0}{1}".format(yesno_prompt, suffix)

    while True:
        response = get_input(prompt_text).strip() or default or ""
        if response != "":
            if re.match('^(y)(es)?$', response, re.IGNORECASE):
                return True
            elif re.match('^(n)(o)?$', response, re.IGNORECASE):
                return False


def _filesystem(
    message, default=None, strip=True, suffix=' ', input_required=True,
    must_exist=True, tab_completion=True, ftype="file"
):
    """
    internal helper function that print a message and
    prompt user for input of a filename/directory.
    Return user input.
    """
    if ftype not in ("file", "directory"):
        raise ValueError("ftype must be 'file' or 'directory'.")

    if tab_completion:
        # activate tab completion; remove delimiter for file system access
        readline.set_completer_delims(
            readline.get_completer_delims().replace("/", "")
        )
        readline.parse_and_bind('tab: complete')

    while True:
        filename = prompt(message, default, strip, suffix, input_required)
        if must_exist is True:
            if not os.path.exists(filename):
                print("'{}' does not exist!".format(filename))
                continue
            elif ftype == "file" and not os.path.isfile(filename):
                print("'{}' is not a file!".format(filename))
                continue
            elif ftype == "directory" and not os.path.isdir(filename):
                print("'{}' is not a directory!".format(filename))
                continue

        if tab_completion:
            # deactivate tab completion
            readline.parse_and_bind('tab: self-insert')

        return filename


def file(
    message, default=None, strip=True, suffix=' ', input_required=True,
    must_exist=True, tab_completion=True
):
    """
    Print a message and prompt user for input of a filename
    Return user input.
    """
    return _filesystem(
        message, default, strip, suffix, input_required,
        must_exist, tab_completion, ftype="file"
    )


def directory(
    message, default=None, strip=True, suffix=' ', input_required=True,
    must_exist=True, tab_completion=True
):
    """
    Print a message and prompt user for input of a directory.
    Return user input.
    """
    return _filesystem(
        message, default, strip, suffix, input_required,
        must_exist, tab_completion, ftype="directory"
    )
