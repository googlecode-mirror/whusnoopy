#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

from pymmseg import mmseg

argvs = sys.argv
root_dir = "/home/cswenye/work/"

if len(argvs) < 2 :
  filename = root_dir + "20090401-172019.0002"
else :
  filename = root_dir + "%s" % argvs[1]

f = file(filename, 'r')
text = f.read()

mmseg.dict_load_defaults()

tokens = mmseg.Algorithm(text)
for token in tokens :
  print '%s [%d -> %d]' % (token.text, token.start, token.end)

