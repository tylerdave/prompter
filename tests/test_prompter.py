from mock import patch
from nose.tools import assert_equals
from prompter import prompt

@patch('__builtin__.raw_input', return_value='Dave')
def test_prompt_returns_input(mock_raw_input):
    returned_value = prompt('What is your name?')
    assert_equals(returned_value, 'Dave')

@patch('__builtin__.raw_input', return_value='')
def test_prompt_returns_default_for_blank_input(mock_raw_input):
    returned_value = prompt('What is your name?', default='Dave')
    assert_equals(returned_value, 'Dave')

@patch('__builtin__.raw_input', return_value=' Dave  ')
def test_prompt_strips_whitespace(mock_raw_input):
    returned_value = prompt('What is your name?')
    assert_equals(returned_value, 'Dave')

@patch('__builtin__.raw_input', return_value=' Dave  ')
def test_prompt_does_not_strip_whitespace(mock_raw_input):
    returned_value = prompt('What is your name?', strip=False)
    assert_equals(returned_value, ' Dave  ')

@patch('__builtin__.raw_input', return_value='        ')
def test_prompt_returns_default_with_only_whitespace_input(mock_raw_input):
    returned_value = prompt('What is your name?', default='Dave')
    assert_equals(returned_value, 'Dave')




