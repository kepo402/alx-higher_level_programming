#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """Return True if obj is the exact class a_class, otherwise False"""
    return type(obj) is a_class

