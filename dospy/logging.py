#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com                                
#

import time

def LOG(level, info) :
  level_map = { 'INFO'  : 4,
                'DEBUG' : 5
              }

  print '[%s] %s: %s' % (level, time.strftime('%Y%m%d-%H%M%S'), info)
