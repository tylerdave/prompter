from __future__ import print_function

__title__ = 'prompter'
__version__ = '0.1.0'
__author__ = 'Dave Forgac'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Dave Forgac'

def prompt(message, default=None, strip=True):
    print(message)
    if default is not None:
        prompt_text = "[{0}] > ".format(default)
    else:
        prompt_text = "> "

    input_value = raw_input(prompt_text)

    # kept separate so default is used when strip is True and input is only
    # spaces. TODO: add test for this case
    if input_value and strip:
        input_value = input_value.strip()

    if not input_value:
        input_value = default

    return input_value
