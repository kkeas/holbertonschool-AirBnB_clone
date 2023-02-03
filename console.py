#!/usr/bin/python3

import cmd, sys

class HBNBCommand(cmd.Cmd):
    cmd.prompt = '(hbnb)'
    
    def quit(self, arg):
        self.quit()
        
    """override emptyline cmmd to print new line when empty"""
    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
