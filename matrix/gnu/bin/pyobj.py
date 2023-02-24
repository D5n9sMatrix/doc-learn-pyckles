#!-*- coding: utf-8 -*-
"""Python doc learn pyckles"""
import requests


def _PyObject_New(PyObj: object,
                  TypeError=None):
    """

            :type TypeError: object
            :param TypeError:
            :type PyObj: object
            """

    PyObj.__doc__ = TypeError.args


class PyObject:
    print("Hello World!")
    pass


def _PyObject_NewVar(PyTypeObject, TypeError=None):
    if PyTypeObject is None:
        try:
            TypeError.args
        except OSError.args:
            return PyTypeObject
        pass
    else:
        return requests.Response
    pass


class PyVarObject:
    print("Pyckles var object open port!")
    pass


class code:
    def __init__(self):
        self.filename = '<console>'
        self.locals = None

    def interactiveConsole(self):
        """Closely emulate the behavior of the interactive Python interpreter. This class builds on InteractiveInterpreter and adds prompting using the familiar sys.ps1 and sys.ps2, and input buffering.
        """
        self.locals = None
        self.filename = '<console>'

