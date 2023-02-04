#!/usr/bin/python3

"""console"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """exits the console"""
        return True

    def help_EOF(self):
        print("syntax: EOF"),
        print("-- exits console")

    def do_quit(self, arg):
        """exits console"""
        return True

    def help_quit(self):
        print("syntax: quit"),
        print("-- terminates the application")

    def emptyline(self):
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
