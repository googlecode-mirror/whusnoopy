#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import logging
import time

def stringToSeconds(s):
  return time.mktime(time.strptime(s, '%Y-%m-%d %H:%M'))

def LOGGER(filename='', level='DEBUG'):
  log = logging.getLogger(__name__)
  log.setLevel(getattr(logging, "%s" % level))
  formatter = logging.Formatter('%(asctime)s [%(levelname)s]%(filename)s:'
                                '%(lineno)d: %(message)s', '%m-%d,%H:%M:%S')

  # Console Logger
  ch = logging.StreamHandler()
  ch.setLevel(logging.ERROR)
  ch.setFormatter(formatter)
  log.addHandler(ch)

  '''
  log_file_suffix = time.strftime('%Y%m%d%H%M%S') + ".log"

  # If log to file
  if len(filename) == 0 :
    filename = "/home/cswenye/log/adke." + log_file_suffix
  fh = logging.FileHandler(filename)
  fh.setLevel(logging.INFO)
  fh.setFormatter(formatter)
  log.addHandler(fh)
  
  debug_filename = "/home/cswenye/log/adke.debug." + log_file_suffix
  dfh = logging.FileHandler(debug_filename)
  dfh.setLevel(logging.DEBUG)
  dfh.setFormatter(formatter)
  log.addHandler(dfh)
  '''

  return log

if __name__ == '__main__' :
  print 'This is a help module, and it exited'
else :
  logger = LOGGER()

