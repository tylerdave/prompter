from mock import patch
from nose.tools import assert_equals
from prompter import yesno

YESNO_COMBINATIONS = [
    ('yes', 'yes', True),
    ('yes', 'YES', True),
    ('yes', 'Yes', True),
    ('yes', 'y', True),
    ('yes', 'Y', True),
    ('yes', '', True),
    ('yes', 'no', False),
    ('yes', 'NO', False),
    ('yes', 'No', False),
    ('yes', 'n', False),
    ('yes', 'N', False),
    ('no', 'yes', False),
    ('no', 'YES', False),
    ('no', 'Yes', False),
    ('no', 'y', False),
    ('no', 'Y', False),
    ('no', '', True),
    ('no', 'no', True),
    ('no', 'NO', True),
    ('no', 'No', True),
    ('no', 'n', True),
    ('no', 'N', True),
    ]

def test_yesno_combinations():
    for (default, value, expected_result) in YESNO_COMBINATIONS:
        yield yesno_checker, default, value, expected_result

def yesno_checker(default, value, expected_result):
    with patch('prompter.get_input', return_value=value):
        returned_value = yesno('Does this work?', default=default)
        assert_equals(returned_value, expected_result)

#@patch('prompter.get_input', return_value='        ')
#def test_prompt_returns_default_with_only_whitespace_input(mock_raw_input):
#    returned_value = prompt('What is your name?', default='Dave')
#    assert_equals(returned_value, 'Dave')




