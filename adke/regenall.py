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
from utilxml import readXmlFile
from utilxml import outputXmlAdsFile

def main():
  # args and options init
  parser = optparse.OptionParser(usage='%prog [options] LIST_FILE')
  parser.add_option('-o', '--output_path', dest='output',
                    help='Output filename, or will use FILE.ads[n] defaultly')
  parser.add_option('-u', '--update', action="store_true", dest='update', default='False',
                    help='Update whether there file exsists')
  options, args = parser.parse_args()

  # the input file process
  if len(args) < 1:
    list_file_path = '/home/cswenye/snoopy/adke/xmllist'
    # parser.error('list file to extract not provided.')
  elif len(args) > 1:
    parser.error('Only one list file may be specified.')
  else:
    list_file_path = os.path.abspath(args[0])

  if options.output:
    output_file_prefix = options.output
  else:
    output_file_prefix = "/home/cswenye/adke/data2/"

  list_file = file(list_file_path, "r")
  files = [t[:-1] for t in list_file.readlines()]
  list_file.close()

  for file_path in files:
    print '[INFO] process %s' % file_path

    output_file_path = os.path.join(output_file_prefix, os.path.split(file_path)[1])
    if os.path.exists(output_file_path):
      if options.update:
        print "[INFO] %s processed already, but re-process" % output_file_path
      else:
        print "[FAULT] %s processed already, skip" % output_file_path
        continue

    posts = readXmlFile(file_path)

    if not posts:
      print '[ERROR] no post in %s, skip it' % file_path
      continue
    print '[INFO] read %d posts from %s' % (len(posts), file_path)

    ads = genUpdateAds(posts)

    print "[INFO] gen ads finish, write into %s" % output_file_path
    outputXmlAdsFile(output_file_path, posts, ads)

  return 0


if __name__ == "__main__":
  sys.exit(main())

