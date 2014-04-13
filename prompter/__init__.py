"""
prompter CUI input prompts
~~~~~~~~~~~~~~~~~~~~~~~~~~

Prompter is a tool for displaying simple input prompts with optional defaults.

Usage:

  >>> from prompter import prompt

  >>> prompt('What is your name?')
  What is your name?
  > Dave
  'Dave'

  >>> prompt('What is your name?', default='Dave')
  What is your name?
  [Dave] >
  'Dave'

  >>> prompt('Enter text surrounded by spaces:', strip=False)
  Enter text surrounded by spaces:
  >       text
  '      text  '

:copyright: (c) 2014 by Dave Forgac
:license: MIT, see LICENSE file for details
"""
from __future__ import print_function

__title__ = 'prompter'
__version__ = '0.2.1'
__author__ = 'Dave Forgac'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Dave Forgac'

def get_input(message):
    """ Get user input using raw_input() for Python 2.x and input() for 3.x. """
    try:
        return raw_input(message)
    except NameError:
        return input(message)

def prompt(message, default=None, strip=True):
    """ Print a message and prompt user for input. Return user input. """
    print(message)
    if default is not None:
        prompt_text = "[{0}] > ".format(default)
    else:
        prompt_text = "> "

    input_value = get_input(prompt_text)

    if input_value and strip:
        input_value = input_value.strip()

    if not input_value:
        input_value = default

    return input_value
