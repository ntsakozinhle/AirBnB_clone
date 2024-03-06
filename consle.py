#!/usr/bin/python3
"""This module defined the command interpreter for the AirBnB clone project."""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone project."""

    prompt = 'hbnb '

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter."""
        print()
        return Ture

if __name__ == '__main__':
    HBNBCommand().cmdloop()
