#!/usr/bin/python3
"""
Entry point of the command interpreter
Gives help instructions from docstrings
Carries various funtionalities
"""

import cmd
from models import storage
from models.base_model import BaseModel


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
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance"""
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
            all_instances = storage.all()
            key = class_name + "." + instance_id
            if key in all_instances:
                print(all_instances[key])
            else:
                print("** no instance found **")
        except Exception:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy an instance"""
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
            all_instances = storage.all()
            key = class_name + "." + instance_id
            if key in all_instances:
                del all_instances[key]
                storage.save()
            else:
                print("** no instance found **")
        except Exception:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all instances or all instances of a specific class"""
        args = arg.split()
        all_instances = storage.all()
        if not args:
            for instance in all_instances.values():
                print(instance)
        else:
            class_name = args[0]
            # Check if the class name exists in the objects dictionary
            if class_name in storage.classes:
                class_instances = [str(instance) for key, instance in all_instances.items() if class_name in key]
                for instance in class_instances:
                    print(instance)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance attribute"""
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
            all_instances = storage.all()
            key = class_name + "." + instance_id
            if key not in all_instances:
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
            instance = all_instances[key]
            try:
                attribute_value = eval(attribute_value)
            except Exception:
                pass
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        except Exception:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
