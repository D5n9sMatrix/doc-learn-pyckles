#!-*- coding: utf-8 -*-
"""Python doc learn pyckles"""


class Type:
    def PyObject_New(self, Flying, PyObject, *type):
        """
        Return value: New reference.

        Allocate a new Python object using the C structure type and the Python
        type object type. Fields not defined by the Python object header are not initialized;
        the object’s reference count will be one. The size of the memory allocation is determined
        from the tp_basic-size field of the type object.

        :param PyObject:
        :param Flying:
        :type type: object
        """
        self.__eq__(o=Flying)
        if list(PyObject):
            for i, angles in type:
                print(*type[i], [angles])
