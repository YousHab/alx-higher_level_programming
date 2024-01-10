#!/usr/bin/python3

import os

with open("filetext.txt", 'a', encoding="utf-8") as my_file:
    my_file.write("Random text\nmore text\nmore and more")

with open("filetext.py", 'r', encoding="utf-8") as my_file:
    print(my_file.read())
