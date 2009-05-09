#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import os
import sys
import optparse

from base import logger
from extract import extractPage
from utilxml import *
from adsgen import genUpdateAds

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

  posts = extractPage(file_path)
  ads = genUpdateAds(posts)

  if options.output:
    outputXmlAdsFile(options.output, posts, ads)
  return 0


if __name__ == "__main__":
  sys.exit(main())

