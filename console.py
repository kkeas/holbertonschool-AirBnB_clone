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
           
        def do_all(self, arg):
            """ Print all objects or all objects of specified class """
            yes = 0
            all_obj = [str(v) for v in storage.all().values()]
            if not arg:
                yes = 1
                print('{}'.format(all_obj))
            elif arg:
                arg_list = arg.split()
            if arg and arg_list[0] in HBNBCommand.__classes:
                yes = 1
                all_obj = storage.all()  # all() method from file_storage.py
                name = arg_list[0]
                all_obj = [str(v) for k, v in all_obj.items()
            if name == v.__class__.__name__]
            print(all_obj)
            
            if yes == 0:
                print("** class doesn't exist **")





if __name__ == '__main__':
    HBNBCommand().cmdloop()
