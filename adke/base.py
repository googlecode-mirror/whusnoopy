#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

global TITLE_WEIGHT
TITLE_WEIGHT = 2

import logging
import time

def LOGGER(filename='', level='INFO') :
  log = logging.getLogger(__name__)
  log.setLevel(getattr(logging, "%s" % level))
  formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d: %(message)s', '%y-%m-%d,%H:%M:%S')

# Console Logger
  ch = logging.StreamHandler()
  # ch.setLevel(logging.ERROR)
  ch.setFormatter(formatter)
  log.addHandler(ch)

# If log to file
  if len(filename) == 0 :
    filename = "/home/cswenye/log/adke." + time.strftime('%Y%m%d%H%M%S') + ".log"
  fh = logging.FileHandler(filename)
  fh.setLevel(logging.INFO)
  fh.setFormatter(formatter)
  log.addHandler(fh)

  debug_filename = "/home/cswenye/log/adke.debug.log"
  dfh = logging.FileHandler(debug_filename)
  dfh.setLevel(logging.DEBUG)
  dfh.setFormatter(formatter)
  log.addHandler(dfh)

  return log

if __name__ == '__main__' :
  LOG = LOGGER()
  LOG.info("Hello, this is a logger module")
else :
  logger = LOGGER()

