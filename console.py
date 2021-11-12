#!/usr/bin/env python3
"""Interpreter module"""


import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage 

class HBNBCommand(cmd.Cmd):
    """Class contains various AirBnB commands"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Command indicates the end of line"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """If no argument is given return nothing"""
        return False

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        instance_n = BaseModel()
        instance_n.save()
        print(instance_n.id)

    def do_show(self, line):
        """Prints th string representation of an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False
        key = "BaseModel." + args[1]
        #file_inst = FileStorage()
        di_ct = models.storage.all()
        if key in di_ct:
            print(di_ct[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes instances based on the class name and id and save
        the changes into JSON File"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False
        key = "BaseModel." + args[1]
        di_ct = models.storage.all()
        if key in di_ct:
            del di_ct[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line=None):
        """Prints all string representatoin of all instances"""
        if line is not None:
            args = line.split()
            if len(args) > 0:
                if args[0] != "BaseModel":
                    print("** class doesn't exist **")
                    return False
        di_ct = models.storage.all()
        dict_list = []
        for key in di_ct:
            dict_list.append(str(di_ct[key]))
        print("[", end="")
        print(", ".join(dict_list), end="")
        print("]")

    def do_update(self, line):
        """Updates the instances based on class name and Id by
        adding or updating the attributes
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False
        key = "BaseModel." + args[1]
        di_ct = models.storage.all()
        if key in di_ct:
            obj = di_ct[key]
        else:
            print("** no instance found **")
            return False
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        obj[args[2]] = args[3]


    

if __name__ == '__main__': #cod should not be executed when imported
    HBNBCommand().cmdloop()
