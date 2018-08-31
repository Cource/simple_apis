#!/usr/bin/env python3
# opens any apps you tell it to open
import os

app_name = str(input('Enter the name of the app:  '))
name_list = ('firefox', 'atom', 'unity')
# add the paths respective to the item number of the app name
# remember to add the  '\"  at the begining and  \"'  at the end
path_list=( '\"C:/Program Files/Mozilla Firefox/firefox.exe\"',  '\"%appdata%/Local/atom/atom.exe\"' , \
'\"D:/Unity/Editor/Unity.exe\"')

# The working:
x = 0
while x < len(name_list):
    if app_name == name_list[x]:
        break
# Adding 1 to x so that the next list item is scanned 
    x += 1

y = path_list[x]
os.system(y)
