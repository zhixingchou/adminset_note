#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os


def get_roles(args):
    dir_list = []
    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
    dirs = os.listdir(args) # roles_path = /var/opt/adminset/data/ansible/roles/
    for d in dirs:
        if d[0] == '.':
            pass    # pass是空语句，是为了保持程序结构的完整性;不做任何事情，一般用做占位语句。
        elif os.path.isfile(args+d):    # os.path.isfile() 如果path是一个存在的文件，返回True。否则返回False。
            pass
        else:
            dir_list.append(d)
    return dir_list


def get_playbook(args):
    files_list = []
    dirs = os.listdir(args)
    for d in dirs:
        if d[0] == '.':
            pass
        elif os.path.isdir(args+d):
            pass
        elif d.endswith(".retry"):  # 用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
            os.remove(args+d)
        else:
            files_list.append(d)
    return files_list


def get_scripts(args):
    files_list = []
    dirs = os.listdir(args)
    for d in dirs:
        if d[0] == '.':
            pass
        elif os.path.isdir(args+d):
            pass
        else:
            files_list.append(d)
    return files_list
