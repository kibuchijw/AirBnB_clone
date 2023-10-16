#!/usr/bin/python3
"""Unittest test module for console.py"""

import os
import sys
import unittest
from models import storage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models.engine.file_storage import FileStorage


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests to test HBNB command interpreter"""

    def test_prompt_string(self):
        """Checking console prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_enter_line(self):
        """checking when a new empty line is entered"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
