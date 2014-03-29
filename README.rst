SqlSoup Testing with SQLite 
===========================

Overview
--------

This repository contains the  code for my presentation at the Boston Python lightning talks on July 30, 2013.

Slides
------
Slides are available `here <https://drive.google.com/folderview?id=0B2_Gr4VRB_UvNkRidTUzUmd3X3M&usp=sharing>`_
These slides provide a brief overview of using SQLSoup with SQLite memory with accompanying unit test code.  

Installation
------------

First: The guide below assumes you are using a Unix variant. The indented lines that begin with dollar sign '$' indicates that this command is to be run at a shell prompt.

For those new to Python, I recommend using `Virtuanenv <http://www.virtualenv.org/>`_  or `Virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/>`_  to explore Python code and developing your own projects.

If you are running virtualenvwrapper, from your shell prompt, run:

.. code-block:: bash

   $ mkvirtualenv sqlsoup_demo

This will create a virtualenv environment for this demo and set the active environment to sqlsoup_demo for this shell. Navigate to your project folder (The one that contains this README file) and run:

.. code-block:: bash

   $ pip install -r requirements.txt

This will install the needed Python paackages to run the test code.

Running the test
----------------

Run the following to execute the test:

.. code-block:: bash

   $ python test_notebook.py

And you should see the test output.
