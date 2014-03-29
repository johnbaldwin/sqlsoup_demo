SqlSoup Demo
============


Overview
--------

This repository contains the  code for my presentation at the Boston Python lightning talks on July 30, 2013.

Slides
------
Slides are available here:
https://drive.google.com/folderview?id=0B2_Gr4VRB_UvNkRidTUzUmd3X3M&usp=sharing
These slides provide a brief overview of using SQLSoup with SQLite memory. RESTnotes
uses SQLite memory for unit tests

Getting Started
^^^^^^^^^^^^^^^

First: The guide below assumes you are using a Unix variant. The indented lines that begin with dollar sign '$' indicates that this command is to be run at a shell prompt.

For those new to Python, I recommend using .. _Virtualenv: http://www.virtualenv.org/  or .. _Virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/  to explore Python code and developing your own projects.

If you are running virtualenvwrapper, from your shell prompt
::
    $ mkvirtualenv sqlsoup_demo
This will create a virtualenv environment for this demo and set the active environment to sqlsoup_demo for this shell. Navigate to your project folder (The one that contains this README file) and run:
::
    $ pip install -r requirements.txt
This will install the needed Python paackages to run the test code.

Running the test
^^^^^^^^^^^^^^^^

::
    $ python test_notebook.py

And you should see the test output.
