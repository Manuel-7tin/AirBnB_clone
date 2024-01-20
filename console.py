#!/usr/bin/python3

"""Interactive shell for Airbnb project."""

import json
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class."""

    prompt = '(hbnb) '
    supported_classes = ["BaseModel"]

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

#    def emptyline(self):
#        """Handle empty line"""
#        pass

    def do_create(self, class_):
        """
        Creates a new instance of a given class and saves it to a given class
        """
        supported_classes = ["BaseModel"]
        if not class_:
            print("** class name missing **")
        elif class_ not in supported_classes:
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            print(instance.id)
            inst_dict = instance.to_dict()
            with open(file="data.json", mode="w") as data_file:
                json.dump(inst_dict, data_file, indent=4)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        class_ = None
        id_num = None
        for n in range(len(args.split())):
            if n > 1:
                break
            elif n == 0:
                class_ = args.split()[n]
            elif n == 1:
                id_num = args.split()[n]
        supported_classes = ["BaseModel"]
        if not class_:
            print("** class name missing **")
        elif class_ not in supported_classes:
            print("** class doesn't exist **")
        elif not id_num:
            print("** instance id missing **")
        else:
            with open(file="data.json", mode="r") as data_file:
                inst_data = json.load(data_file)
            if inst_data["id"] != id_num:
                print("** no instance found **")
            else:
                instance = BaseModel(
                        id=inst_data["id"],
                        created_at=inst_data["created_at"],
                        updated_at=inst_data["updated_at"]
                        )
                print(str(instance))


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print("\nExiting...")
