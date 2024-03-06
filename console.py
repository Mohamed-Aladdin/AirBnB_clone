#!/usr/bin/python3
"Entry point of the command line interpreter module"

import cmd
import json
import re
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
  """HBNBCommand class that inherits from Cmd parent class"""
  
  prompt = "(hbnb) "

  def do_EOF(self, line):
    """EOF character to exit the program.\n"""

    return True
  
  def do_quit(self, line):
    """Quit command to exit the program.\n"""

    return True
  
  def emptyline(self):
    """
    Method to override the original emptyline method to avoid
    repeating the previous prompt when an empty line is presented
    """

    pass

  def do_create(self, line):
    """Create command to create a new instance of a valid object.\n"""

    if line is None or line == "":
      print("** class name missing **")
    elif line not in storage.classes():
      print("** class doesn't exist **")
    else:
      obj = storage.classes()[line]()
      obj.save()
      print(obj.id)

  def do_show(self, line):
    """
    Show command to print the string representation
    of an instance based on the class name and id.\n
    """

    if line is None or line == "":
      print("** class name missing **")
    else:
      args = line.split(" ")
      
      if args[0] not in storage.classes():
        print("** class doesn't exist **")
      elif len(args) < 2:
        print("** instance id missing **")
      else:
        key = "{}.{}".format(args[0], args[1])

        if key not in storage.all():
          print("** no instance found **")
        else:
          print(storage.all()[key])

  def do_destroy(self, line):
    """Destroy command to delete an instance based on the class name and id.\n"""

    if line is None or line == "":
      print("** class name missing **")
    else:
      args = line.split(" ")
      
      if args[0] not in storage.classes():
        print("** class doesn't exist **")
      elif len(args) < 2:
        print("** instance id missing **")
      else:
        key = "{}.{}".format(args[0], args[1])

        if key not in storage.all():
          print("** no instance found **")
        else:
          del storage.all()[key]
          storage.save()

  def do_all(self, line):
    """
    All command to print all string representation of
    all instances based or not on the class name.\n
    """

    if line != "":
      args = line.split(" ")

      if args[0] not in storage.classes():
        print("** class doesn't exist **")
      else:
        ins_list = [str(inst) for key, inst in storage.all().items() if type(inst).__name__ == args[0]]
        print(ins_list)
    else:
      ins_list = [str(inst) for key, inst in storage.all().items()]
      print(ins_list)

  def do_update(self, line):
    """
    Update command to update an instance based on
    the class name and id by adding or updating attribute.\n
    """

    if line is None or line == "":
      print("** class name missing **")
    else:
      args = shlex.split(line, posix=False)
      
      if args[0] not in storage.classes():
        print("** class doesn't exist **")
      elif len(args) < 2:
        print("** instance id missing **")
      else:
        key = "{}.{}".format(args[0], args[1])

        if key not in storage.all():
          print("** no instance found **")
        else:
          if len(args) < 3:
            print("** attribute name missing **")
          elif len(args) < 4:
            print("** value missing **")
          else:
            args[3] = args[3].strip("\"")
            storage.all()[key].__dict__[args[2]] = args[3]
            storage.save()

if __name__ == '__main__':
  HBNBCommand().cmdloop()