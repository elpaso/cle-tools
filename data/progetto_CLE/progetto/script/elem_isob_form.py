# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:		elem_isob_form.py
# Author:	  Tarquini E.
# Created:	 22-09-2018
#-------------------------------------------------------------------------------

from qgis.core import *
from qgis.PyQt.QtWidgets import *
import webbrowser


def elem_isob_form(dialog, layer, feature):

	help_button = dialog.findChild(QPushButton, "help_button")

	help_button.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/watch?v=dnJIjTNzQJQ&t=115s'))