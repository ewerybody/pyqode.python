#! /usr/bin/python
# -*- coding: utf-8 -*-
import logging
import sys
import os; os.environ['QT_API'] = 'pyside'
filename = None
if sys.platform == 'win32':
    filename = 'pynotepad.log'
logging.basicConfig(level=logging.INFO, filename=filename)
from pynotepad import main


if __name__ == '__main__':
    main()
