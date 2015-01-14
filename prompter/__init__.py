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

__title__ = 'prompter'
__author__ = 'Dave Forgac'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Dave Forgac'
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

def get_input(message=None):
    """ Get user input using raw_input() for Python 2.x and input() for 3.x. """
    try:
        return raw_input(message)
    except NameError:
        return input(message)

def prompt(message, default=None, strip=True, suffix=' '):
    """ Print a message and prompt user for input. Return user input. """
    if default is not None:
        prompt_text = "{0} [{1}]{2}".format(message, default, suffix)
    else:
        prompt_text = "{0}{1}".format(message, suffix)

    input_value = get_input(prompt_text)

    if input_value and strip:
        input_value = input_value.strip()

    if not input_value:
        input_value = default

    return input_value

def yesno(message, default='yes', suffix=' '):
    """ Prompt user to answer yes or no. Return True if the default is chosen,
     otherwise False. """
    if default == 'yes':
        yesno_prompt = '[Y/n]'
    elif default == 'no':
        yesno_prompt = '[y/N]'
    else:
        raise ValueError("default must be 'yes' or 'no'.")

    if message != '':
        prompt_text = "{0} {1}{2}".format(message, yesno_prompt, suffix)
    else:
        prompt_text = "{0}{1}".format(yesno_prompt, suffix)

    while True:
        response = get_input(prompt_text).strip()
        if response == '':
            return True
        else:
            if re.match('^(y)(es)?$', response, re.IGNORECASE):
                if default == 'yes':
                    return True
                else:
                    return False
            elif re.match('^(n)(o)?$', response, re.IGNORECASE):
                if default == 'no':
                    return True
                else:
                    return False

