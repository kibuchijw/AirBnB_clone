#/usr/bin/python3
"""
Entry point of the command interpreter
Gives help instructions from docstrings
Carries various funtionalities
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
