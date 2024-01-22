#!/usr/bin/python3

"""Interactive shell for Airbnb project."""

import json
import cmd
import sys
from datetime import datetime
from models.base_model import BaseModel
from models import storage

data_dict = storage.all()


def parse_args(lmt, arg_string):
    """
    Takes a string of words and checks if each is valid for the program to run
    """
    if not isinstance(arg_string, str) or not isinstance(lmt, int) or lmt < 1:
        return (0, ())

    total = 0
    supported_classes = ["BaseModel"]
    class_name, id_num, attr_name, attr_value = None, None, None, None
    attr_list = [class_name, id_num, attr_name, attr_value]
    cert_attr_list = []

    for n in range(len(arg_string.split())):
        if n > caution:
            break
        attr_list[n] = arg_string.split()[n]
    if not attr_list[0]:
        print("** class name missing **")
    elif attr_list[0] not in supported_classes:
        print("** class doesn't exist **")
    elif not attr_list[1] and caution >= 2:
        print("** instance id missing **")
        total = 1
    elif data_dict.get(f"BaseModel.{attr_list[1]}") is None and caution >= 2:
        print("** no instance found **")
        total = 1
    elif not attr_list[2] and caution >= 3:
        print("** attribute name missing **")
        total = 2
    elif not attr_list[3] and caution >= 4:
        print("** value missing **")
        total = 3
    else:
        total = 4
    return (total, attr_list)


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

    def do_create(self, class_):
        """
        Creates a new instance of a given class and saves it to a given class
        """
        if parse_args(1, class_)[0] > 1:
            instance = BaseModel()
            print(instance.id)
            storage.save()
        else:
            pass

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        parsed_input = parse_args(2, args)
        if parsed_input[0] > 2:
            key = parsed_input[1][0] + "." + parsed_input[1][1]
            print(str(data_dict.get(key)))
        else:
            pass

    def do_destroy(self, args):
        """
        Deletes a class instance of given id
        Updates database
        """
        parsed_input = parse_args(2, args)
        if parsed_input[0] > 2:
            key = parsed_input[1][0] + "." + parsed_input[1][1]
            del data_dict[key]
            storage.save()

    def do_all(self, class_):
        """Prints al instances of a given class"""
        if class_:
            parsed_input = parse_args(1, class_)
            if parsed_input[0] >= 1:
                for key in data_dict:
                    if data_dict[key].split()[0] == f"[{class_}]":
                        print(data_dict[key])
        else:
            for key in data_dict:
                print(data_dict[key])

    def do_update(self, args):
        """Update the database"""
        parsed_input = parse_args(4, args)
        if parsed_input[0] > 3:
            key = parsed_input[1][0] + "." + parsed_input[1][1]
            data_string = data_dict[key]
            data = data_string.split(") ")[1]
            data = data.replace("datetime.", "")
            fdata = eval(data)
            fdata[parsed_input[1][2]] = parsed_input[1][3]
            k = f"[{parsed_input[1][0]}] ({parsed_input[1][1]}) {fdata}"
            data_dict[key] = k
            storage.save()


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print("\nExiting...")
