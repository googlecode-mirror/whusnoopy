#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

from base import logger

if __name__ == "__main__" :
  argvs = sys.argv[1:]

  global root_dir
  root_dir = '/home/cswenye/work'

  logger.info('Hello')

