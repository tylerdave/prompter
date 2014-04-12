prompter
========

Simple CUI prompt input for Python

Installing
----------

Install the latest from master:

  pip install git+git://github.com/tylerdave/prompter

Using
-----

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
  >       test  
  '      test  '
