#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import os
import sys
import optparse

from base import logger
from utilxml import *
from adsgen import generateAdWords

def updatePost(posts, post):
  return posts

def initPost(posts):
  for p in posts:
    p['weight'] = 1
  return posts

def main():
  # args and options init
  parser = optparse.OptionParser(usage='%prog [options] FILE')
  parser.add_option('-o', '--output', dest='output',
                    help='Output filename, or will use FILE.ads[n] defaultly')
  options, args = parser.parse_args()

  # the input file process
  if len(args) < 1:
    parser.error('File to extract not provided.')
  elif len(args) > 1:
    parser.error('Only one file may be specified.')

  file_path = args[0]
  logger.info('Generate ads keywords for the whole page %s' % file_path)

  # the default output file name
  if options.output:
    output_prefix = options.output
  else:
    output_prefix = os.path.splitext(file_path)[0]

  posts = extractXmlFile(file_path)
  posts = initPost(posts)

  for p in posts:
    #posts = updatePost(posts, p)
    sads, pads = generateAdWords(posts)

    file_path = "%s.ads%d" % (output_prefix, p['no'])
    outputXmlAdsFile(file_path, sads, pads) 

  return 0


if __name__ == "__main__":
  sys.exit(main())

