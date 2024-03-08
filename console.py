#!/usr/bin/python3
"""This module defined the command interpreter for the AirBnB clone project."""

import cmd
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter."""
        print("")
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file,
        and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            instance_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return
        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(value) for value in storage.all().values()])
        else:
            try:
                class_name = eval(arg).__name__
                print([str(value) for key, value in storage.all().items() if class_name in key])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_name = args[2]
            attribute_value = args[3]
            instance = storage.all()[key]
            setattr(instance, attribute_name, attribute_value.strip('"'))
            instance.save()
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
