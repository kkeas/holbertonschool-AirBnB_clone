#!/usr/bin/python3

"""console"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = {
        'BaseModel',
        'User',
        'Place',
        'State',
        'City',
        'Amenity',
        'Review'
        }

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

    def do_create(self, arg):
        """create new instance and save it to the json file"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            classd = {'BaseModel': BaseModel,
                     'User': User,
                     'Place': Place,
                     'State': State,
                     'City': City,
                     'Amenity': Amenity,
                     'Review': Review
                     }

            newobj = classd[arg]()
            newobj.save()
            print('{}', format(newobj.id))
            storage.save()

    def do_show(self, line):
        arg = line.split()
        objdict = storage.all() #all method from filestorage 
        if len(arg) == 0:
            print("** class name missing **")
        if arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[1] not in HBNBCommand.__classes:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg[0], arg[1])])
        
        def do_destroy(self,line):
            """ Destroy instance specified by user; save changes to JSON file """
            arg = line.split()
            obj_dict = storage.all()  # all() method from file_storage.py
            if len(arg) == 0:
                print("** class name missing **")
            elif arg[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
                print("** no instance found **")
            else:
                del (obj_dict["{}.{}".format(arg[0], arg[1])])
                storage.save()





if __name__ == '__main__':
    HBNBCommand().cmdloop()
