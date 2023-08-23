#!/usr/bin/python3
""" function to define the encoding """


def validUTF8(data):
    """ define the conditions """
    try:
        typeddata = [n & 255 for n in data]
        bytes(typeddata).decode("UTF-8")
        return True
    except Exception:
        return False
