from mock import patch
from prompter import yesno

import pytest


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
    ('no', 'yes', True),
    ('no', 'YES', True),
    ('no', 'Yes', True),
    ('no', 'y', True),
    ('no', 'Y', True),
    ('no', '', False),
    ('no', 'no', False),
    ('no', 'NO', False),
    ('no', 'No', False),
    ('no', 'n', False),
    ('no', 'N', False),
    ]

@pytest.mark.parametrize("default,value,expected_result", YESNO_COMBINATIONS)
def test_yesno(default, value, expected_result):
    with patch('prompter.get_input', return_value=value):
        returned_value = yesno('Does this work?', default=default)
        assert returned_value == expected_result

#@patch('prompter.get_input', return_value='        ')
#def test_prompt_returns_default_with_only_whitespace_input(mock_raw_input):
#    returned_value = prompt('What is your name?', default='Dave')
#    assert_equals(returned_value, 'Dave')




