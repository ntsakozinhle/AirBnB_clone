# tests/test_hbnb_command.py

import unittest
from unittest.mock import patch
from io import StringIO
from hbnb_command import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('quit'))
            self.assertEqual(fake_out.getvalue().strip(), '')

    def test_EOF_command(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('EOF'))
            self.assertEqual(fake_out.getvalue().strip(), '')

if __name__ == '__main__':
    unittest.main()
