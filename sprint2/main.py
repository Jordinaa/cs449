# Sprint-2
# Author: Jordan Taranto

from GUI import GUI
import unittest

# init the unit test suite
load = unittest.main()
# will load any test that start with test_ in the sprint2 directory
suite = load.discover("sprint2", pattern="test_*.py")
# create a test run that displays results in console 
run = unittest.TextTestRunner()
# run the tests in test_GUI.py
run.run(suite)

app = GUI()
app.run()