#!/usr/bin/env python
# -*- coding: utf-8 -*-
def formulaSplit(val):
    return val.split('+')

def addition(vals):
    total = 0
    for val in vals:
        total = total + int(val)

    return total


str = input("Enter formula>")
print(addition(formulaSplit(str)))


