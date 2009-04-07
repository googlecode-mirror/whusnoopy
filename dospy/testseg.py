#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

from pymmseg import mmseg

argvs = sys.argv

if len(argvs) < 2 :
  filename = "20090401-172019.0002"
else :
  filename = "%s" % argvs[1]

f = file(filename, 'r')
text = f.read()

mmseg.dict_load_defaults()

tokens = mmseg.Algorithm(text)
for token in tokens :
  print '%s [%d -> %d]' % (token.text, token.start, token.end)

