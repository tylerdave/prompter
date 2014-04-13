prompter
========

.. image:: https://travis-ci.org/tylerdave/prompter.svg?branch=master
  :target: https://travis-ci.org/tylerdave/prompter

.. image:: http://badge.fury.io/py/prompter.png
  :target: http://badge.fury.io/py/prompter


Simple CUI prompt input for Python

Installing
----------

Install the latest stable from PyPi::

 pip install prompter

Install the latest development version from master::

  pip install git+git://github.com/tylerdave/prompter

Using
-----

::

  >>> from prompter import prompt, yesno

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

  >>> yesno('Really?')
  Really? [Y/n]
  True

  >>> yesno('Really?')
  Really? [Y/n] no
  False

  >>> yesno('Really?', default='no')
  Really? [y/N]
  True

  >>> yesno('Really?', default='no')
  Really? [y/N] y
  False

  >>> yesno('')
  [Y/n] No
  False

