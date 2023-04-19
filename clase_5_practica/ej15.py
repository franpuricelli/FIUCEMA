#!/usr/bin/python
import re

def mail_correcto(string):
    return bool(re.search("^\w+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?$", string))
print(mail_correcto("lorenzo-nastri@gmail.com"))
print(mail_correcto("lorenzo-&nastri@gmail.com"))