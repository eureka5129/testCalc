#!/usr/bin/env python
# -*- coding: utf-8 -*-
import calcFunc as cf
import re

data = cf.calcFunc()
str = input("Enter formula>")

numList = []
numList = re.split('\+|\-|\*|\/', str)

opeList = re.split('[0-9]{0,}', str)
stackOpe = list(filter(None, opeList))

num = 0
ope = ''


for i,item in enumerate(numList):
    if len(stackOpe) != 0:
        ope = stackOpe.pop()

    if i == 0:
        data.addition(item)
    else:
        if ope == '+':
            data.addition(item)
        elif ope == '-':
            data.subtraction(item)
        elif ope == '*':
            data.multiplication(item)
        elif ope == '/':
            data.division(item)

print(data.total)



