#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: GWYNETH CASEY AND GABRIELLA NUTT
# Student ID: 2286584 & 2397512
# Email: gcasey@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: HOMEWORK_OR_CLASSWORK_NUMBER
###


import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import seaborn as sb


"""This module is to practice using classes in python. Our class will be called Particle.
"""


class Particle(object):
    """
    """

    
    def __init__(self, x , y , z):
        """
        """
    
    def mass(self):
        """
        """
        m = 1.0
    
    def momentum(self):
        """
        """
        l = (0.0,0.0,0.0)
     
    def position(self):
        """
        """
        r = (x,y,z)

# Note that the class definition ends when the indentation returns to the
# original indentation (which should be the far left of the file)


###
# Put function definitions after any class definitions.
# For most scientific work, creating a well-designed set of functions
# is often the best way to organize your tasks. Functions can be less
# rigid than classes to change and extend later. As such, functions
# should be your bread and butter for practical work.
###

def your_function(arg1, kwarg1=defaultvalue, *args, **kwargs):
    """Function docstring
    
    All functions should have their own documentation via docstrings.
    Function arguments are positional, unless they are provided a default 
    value to become a "keyword argument".
    Here args is a list of all positional arguments beyond those listed.
    Here kwargs is a list of all keyword arguments beyond those listed.
    
    The function doc string should describe the name of the function, 
    its return value and type (if any), and its list of arguments and
    their expected types (if any). Both positional and keyword arguments
    should be listed separately.
    
    For more detailed examples from Google about how to use docstrings see,
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    
    All indentation should be 4 spaces.  NO TABS IN PYTHON CODE.
    
    Args:
        arg1: Describe the arguments of the function
    
    Keyword Args:
        kwarg1: Describe keyword arguments of function (defaultvalue)

    Returns:
        Describe the type and content of what the function returns here.
        It can be useful to give an example if the type is complicated.
    
    Raises:
        If any exceptions can be raised by the function, describe them.
    """
    
    # Function body here - note the nice extra indented line for whitespace
    
    # The "return" keyword specifies the output of the function
    return return_value_goes_here


def your_generator(arg1, kwarg1=defaultvalue, *args, **kwargs):
    """Generator docstring
    
    A generator is just a function that can pause its operation to
    return a value and then resume where it left off later.
    
    In python, the only difference is the replacement of the "return"
    keyword with the "yield" keyword.
    
    Args:
        arg1: Describe the arguments of the function
    
    Keyword Args:
        kwarg1: Describe keyword arguments of function (defaultvalue)

    Yields:
        Describe the type and content of what the function yields here.
    
    Raises:
        If any exceptions can be raised by the function, describe them.
    """
    
    # Function body here - note the nice extra indented line for whitespace
    
    # The "yield" keyword pauses the generator and returns an output.
    # The next time the generator is called, it resumes at the line after
    # the yield keyword. Very often yield statements are placed inside loops
    # so that many values can be returned in sequence as the generator is
    # called repeatedly.

    while True:  # By convention, this is how to create an infinite loop.
        yield return_value_goes_here



###
#
# After the body of the module, you can optionally create a protected main 
# section to place executable scripting code. This main section should call
# the main function defined below.
#
# Importantly, all the above code consists of definitions, so it can be
# imported and used in other modules. Nothing executes by itself.
#
# Below is where we should place code that should be executed as a program.
#
###


def main(local_argv):
    """Main function
    See below for why this would exist. The local_argv argument lists command
    line arguments taken from sys.argv within the protected main block below.
    """
    # Perform executable tasks here
    pass


# Below is the python convention for defining an executable main section
if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. Importantly is not run when 
    # imported as a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Operating system-specific modules that are needed only during
    # program execution should be imported here rather than at the top of the 
    # module.
    
    # Note that the list sys.argv contains all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
    import sys
    main(sys.argv)

