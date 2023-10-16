#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a specified class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        new_instance = storage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_instances = storage.all()
        key = class_name + "." + instance_id

        if key in all_instances:
            print(all_instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_instances = storage.all()
        key = class_name + "." + instance_id

        if key in all_instances:
            del all_instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def default(self, line):
        """
        Called on an input line when the command prefix is not recognized.
        This allows us to handle commands like User.all() dynamically.
        """
        parts = line.split(".")
        if len(parts) == 2:
            class_name = parts[0]
            method_name = parts[1]
            if class_name in storage.classes():
                if method_name == "all()":
                    self.do_all(class_name)
                    return
        print("*** Unknown syntax: " + line)
    def do_all(self, arg):
        """Print all instances or all instances of a specific class"""
        args = arg.split()
        all_instances = storage.all()

        if not args:
            instances = list(all_instances.values())
            for instance in instances:
                print(instance)
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return

            class_instances = [str(instance) for key, instance in all_instances.items() if class_name in key]
            for instance in class_instances:
                print(instance)

    def do_update(self, arg):
        """Update an instance attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_instances = storage.all()
        key = class_name + "." + instance_id

        if key not in all_instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        instance = all_instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
