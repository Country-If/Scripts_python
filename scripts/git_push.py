#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from git import Repo
import os

print("Start pushing...")
print()

cnt = 0
dir_file = os.path.abspath('../')  # code的文件位置，默认将其存放在根目录下
repo = Repo(dir_file)

g = repo.git

while True:
    cnt += 1
    try:
        g.push()
        print("Try " + str(cnt) + ": Successfully push!")
        break
    except Exception as e:
        print(e)
        print("Try " + str(cnt) + ": Push failed, retrying...")
        print()
        continue
