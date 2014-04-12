from __future__ import print_function

__title__ = 'prompter'
__version__ = '0.1.1'
__author__ = 'Dave Forgac'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Dave Forgac'


# nasty hack while we need to support python 2.7 and 3.x :-(
try:
    raw_input
except NameError:
    import builtins

    original_input = builtins.input
    del builtins.input
    def raw_input(*args, **kwargs):
        return original_input(*args, **kwargs)
    builtins.raw_input = raw_input


def prompt(message, default=None, strip=True):
    print(message)
    if default is not None:
        prompt_text = "[{0}] > ".format(default)
    else:
        prompt_text = "> "

    input_value = raw_input(prompt_text)

    if input_value and strip:
        input_value = input_value.strip()

    if not input_value:
        input_value = default

    return input_value
