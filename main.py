#!/usr/bin/env python
# -*- coding: utf-8 -*-
import calcFunc as cf
import re

data = cf.calcFunc()
str = input("Enter formula>")

numList = []
numList = re.split('\+|\-|\*|\/', str)

stackNum = re.split('[1-9]', str)
stackOpe = list(filter(None, stackNum))

num = 0
ope = ''

num = numList.pop()

for i,item in enumerate(numList):
    print(item)
    data.addition(item)
    if len(stackOpe) > 0:
        ope = stackOpe.pop()
        print(ope)
#    if i == 0:
#        num = int(numList.pop())
#        data.addition(num)
#    else:


#    num = int(numList.pop())
#    ope = stackOpe.pop()
#    print(item)
#
#    if ope == '+':
#        data.addition(num)



