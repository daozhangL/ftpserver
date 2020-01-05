#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : ftpserver.py
# @Time    : 2020/1/4 21:55
# @Author  : Stephen Li
# @Email   : lishb0523@163.com
# @Software: PyCharm

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import tkinter
import tkinter.filedialog
import socket


def selectdir(title=u'选择路径', initialdir='.'):
    tkinter.Tk().withdraw()
    filepath = tkinter.filedialog.askdirectory(title=title, initialdir=initialdir)
    return filepath


if __name__ == '__main__':
    sharedir = selectdir("请选择FTP根目录")
    selfip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    pswd = '12345'
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', pswd, sharedir, perm='elradfmwMT')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer((selfip, 21), handler)
    print(f"ftp server: {selfip}:21\npassword:{pswd}\n")
    server.serve_forever()
