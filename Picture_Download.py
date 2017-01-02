# -*- coding: utf-8 -*-
"""
Task:
    How to download a web picture in Python?
Created on Mon Jan  2 14:05:07 2017

@author: liuxinyu
"""

import urllib.request

url=input('请输入图片的地址:')

req=urllib.request.urlopen(url)
image=req.read()

with open('pic.jpg','wb') as f:
    f.write(image)
