prompter
========

Simple CUI prompt input for Python

Installing
----------

Install the latest from master:

  pip install git+git://github.com/tylerdave/prompter

Usage
-----

  >>> from prompter import prompt

  >>> prompt('What is your name?')
  What is your name?
  > Dave
  'Dave'

  >>> prompt('What is your name?', default='Dave Forgac')
  What is your name?
  [Dave Forgac] > 
  'Dave Forgac'

  >>> prompt('Enter text surrounded by spaces:', strip=False)
  Enter text surrounded by spaces:
  >       test  
  '      test  '
