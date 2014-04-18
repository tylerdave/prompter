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
  What is your name? Dave
  'Dave'

  >>> prompt('What is your name?', default='Jenn')
  What is your name? [Jenn]
  'Jenn'

  >>> prompt('What is your name?', default='Jenn', suffix='\n > ')
  What is your name? [Jenn]
  >
  'Jenn'

  >>> prompt('Enter text surrounded by spaces.', strip=False)
  Enter text surrounded by spaces.    text
  '   text   '

  >>> yesno('Really?')
  Really? [Y/n]
  True

  >>> yesno('Really?')
  Really? [Y/n] no
  False

  >>> yesno('Really?', default='no')
  Really? [y/N]
  True

  >>> yesno('')
  [Y/n] n
  False

Note
----

Don't be surprised if the behavior changes in later versions as this is a work
in progress. Please open an issue on Github if you notice problems or have
suggestions.
