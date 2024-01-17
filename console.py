#!/usr/bin/python3

"""Interactive shell for Airbnb project."""

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class."""
    
    prompt = '(hbnb) '

    def do_help(self, line):
        """Display help."""
        # Your help logic here
    
    def do_quit(self, line):
        """Quit the shell."""
        return True

    def default(self, line):
        """Handle unknown syntax."""
        if line == 'EOF':
            sys.exit(0)
        else:
            self.stdout.write('*** Unknown syntax: %s\n' % line)

    def emptyline(self):
        """Handle empty line"""
        pass


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print("\nExiting...")

