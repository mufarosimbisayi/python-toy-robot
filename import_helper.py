import sys
import os
from importlib import import_module
  
# dynamic import  
def dynamic_import(arguments): 
    """
    Returns maze depending on arguments

    Args:
        arguments: A list of args from sys.

    Returns:
        _: A maze or nothing.
    """

    if len(arguments) == 3 and os.path.exists(f"maze/{arguments[2].lower()}.py"):
        return import_module(f"maze.{arguments[2].lower()}")
    if 'unittest' in sys.modules.keys():
        return import_module("maze.mufaros_maze")
    
    return None


def dynamic_world_import(arguments):
    """
    Returns turtle or text world depending on the arguments.

    Args:
        arguments: A list of args from sys.

    Returns:
        _: A turtle or text world module.
    """

    if len(arguments) >= 2 and arguments[1].lower() == "turtle":
        return import_module("world.turtle.world")
    else:
        return  import_module("world.text.world")

