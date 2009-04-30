#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import os
import sys
import optparse

from base import logger
from idf import idf

def generalAdKe(filename, output_path=""):
  xmlInfo = readXmlFile(filename)
  title = xmlInfo.title
  body = xmlInfo.body
  return 0

def main():
  parser = optparse.OptionParser(usage='%prog [options] FILE')
  parser.add_option('-o', '--output', dest='output',
                    help='Output filename, or will use FILE.ads defaultly')

  options, args = parser.parse_args()

  if len(args) < 1:
    parser.error('File to extract not provided.')
  elif len(args) > 1:
    parser.error('Only one file may be specified.')

  file_path = args[0]

  logger.info('Generate ads keywords for the whole page %s' % file_path)
  if options.output:
    generalAdKe(file_path, options.output)
  else:
    generalAdKe(file_path)

  return 0

if __name__ == "__main__" :
  sys.exit(main())
