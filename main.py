#!/usr/bin/env python
# -*- coding: utf-8 -*-
import calcFunc as cf
import re

def chkOperator(val):
    if val in ['+','-','*','/']:
        return True
    else:
        return False

data = cf.calcFunc()
print(chkOperator('+'))

str = input("Enter formula>")

numList = []
numList = re.split('\+|\-|\*|\/', str)

print(opeList)
print(numList)

print(data.addition(10))
print(data.addition(10))


