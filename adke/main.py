#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import os
import sys
import optparse

from base import logger
from extract import extractPage
from adsgen import genUpdateAds
from utilxml import outputXmlAdsFile

def main():
  # args and options init
  parser = optparse.OptionParser(usage='%prog [options] FILE')
  parser.add_option('-o', '--output', dest='output',
                    help='Output filename, or will use FILE.ads[n] defaultly')
  parser.add_option('-u', '--update', dest='update',
                    help='Update whether there file exsists')
  options, args = parser.parse_args()

  # the input file process
  if len(args) < 1:
    parser.error('File to extract not provided.')
  elif len(args) > 1:
    parser.error('Only one file may be specified.')

  file_path = "/home/cswenye/work/thread-%s/thread-%s-1-1.html" % (args[0], args[0])
  logger.info('Generate ads keywords for the whole page %s' % file_path)

  posts = extractPage(file_path)
  ads = genUpdateAds(posts)

  if options.output:
    output_file_path = options.output
  else:
    output_file_path = "/home/cswenye/adke/data/thread-%s-1-1.xml" % args[0]

  if os.path.exists(output_file_path):
    if not options.update:
      print "[FAULT] %s processed already into %s, skip" % (file_path, output_file_path)
      return -1
    print "[INFO] %s processed already into %s, but re-process" % (file_path, output_file_path)

  posts = []
  for i in range(1,10):
    file_path = "%s%d%s" % (file_path[:-8], i, file_path[-7:])
    print "start process file %s" % file_path

    if not os.path.exists(file_path):
      print "file %s not exists, skip" % file_path
      break
    posts = extractPage(file_path, posts)

  if not posts:
    print '[ERROR] extract no post from %s, skip it' % thread
    return -2

  ads = genUpdateAds(posts)

  print "gen ads finish, write into %s" % output_file_path
  outputXmlAdsFile(output_file_path, posts, ads)

  return 0


if __name__ == "__main__":
  sys.exit(main())

