#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import os
import sys
import optparse

from xml.dom import minidom

from base import logger
from idf import idf
from pymmseg import mmseg

def generalAdKe(filename, output_path=""):
  xmldoc = minidom.parse(filename)
 
  titles = []
  for title_node in xmldoc.getElementsByTagName('title'):
    if title_node.firstChild:
      titles.append(title_node.firstChild.data)
  title = "".join(titles)
  logger.info('Got titles as %(title)s' % locals())

  bodys = []
  for body_node in xmldoc.getElementsByTagName('body'):
    bodys.append(body_node.firstChild.data)
  for ref_node in xmldoc.getElementsByTagName('ref'):
    if ref_node.firstChild:
      bodys.append(body_node.firstChild.data)
  body = "".join(bodys)
  logger.info('Got titles as %(body)s' % locals())

  title_tokens = mmseg.Algorithm(title)
  body_tokens = mmseg.Algorithm(body)

  all_tokens = title_tokens * TITLE_WEIGHT + body_tokens
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

  mmseg.dict_load_defaults()

  logger.info('Generate ads keywords for the whole page %s' % file_path)
  if options.output:
    generalAdKe(file_path, options.output)
  else:
    generalAdKe(file_path)

  return 0

if __name__ == "__main__" :
  sys.exit(main())
