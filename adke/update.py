#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import os
import sys
import optparse

from xml.dom import minidom

from base import *
from utilxml import *
from adwordsselector import generateAdWords

def updatePost(posts, post):

  return posts

def initPost(posts, post):
  return posts

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

  xmldoc = minidom.parse(file_path)
  posts = extractXmlFile(xmldoc)

  for p in posts:
    posts = initPost(posts, p)
    posts = updatePost(posts, p)
    sads, pads = generateAdWords(posts)

    for ad in sads:
      print ad
    print '---->'

  return 0


if __name__ == "__main__":
  sys.exit(main())

