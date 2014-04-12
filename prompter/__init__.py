from __future__ import print_function

__title__ = 'prompter'
__version__ = '0.1.1'
__author__ = 'Dave Forgac'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Dave Forgac'


# hack while we need to support python 2.6, 2.7 and 3+ :-(
def get_input(message):
    try:
        return raw_input(message)
    except NameError:
        import builtins
        return input(message)

def prompt(message, default=None, strip=True):
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
