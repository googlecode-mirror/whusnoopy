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
  parser = optparse.OptionParser(usage='%prog [options] LIST_FILE')
  parser.add_option('-o', '--output_path', dest='output',
                    help='Output filename, or will use FILE.ads[n] defaultly')
  parser.add_option('-u', '--update', dest='update',
                    help='Update whether there file exsists')
  options, args = parser.parse_args()

  # the input file process
  if len(args) < 1:
    list_file_path = '/home/cswenye/work/list_of_threads'
    # parser.error('list file to extract not provided.')
  elif len(args) > 1:
    parser.error('Only one list file may be specified.')
  else:
    list_file_path = os.path.abspath(args[0])

  if options.output:
    output_file_prefix = options.output
  else:
    output_file_prefix = "/home/cswenye/adke/data/"

  file_prefix = os.path.split(list_file_path)[0]
  list_file = file(list_file_path, "r")

  while True:
    file_path = list_file.readline()
    if not file_path:
      break

    thread = os.path.splitext(os.path.split(file_path)[1])[0]
    file_path = os.path.join(file_prefix, thread[0:-4], thread + ".html")
    output_file_path = os.path.join(output_file_prefix, thread + ".xml")
    if os.path.exists(output_file_path):
      if not options.update:
        print "[FAULT] %s processed already into %s, skip" % (thread, output_file_path)
        continue
      print "[INFO] %s processed already into %s, but re-process" % (thread, output_file_path)

    posts = []
    for i in range(1,11):
      file_path = "%s%d%s" % (file_path[:-8], i, file_path[-7:])
      print "start process file %s" % file_path

      if not os.path.exists(file_path):
        break
      posts = extractPage(file_path, posts)

    if not posts:
      print '[ERROR] extract no post from %s, skip it' % thread
      continue

    ads = genUpdateAds(posts)

    print "[INFO] gen ads finish, write into %s" % output_file_path
    outputXmlAdsFile(output_file_path, posts, ads)

  return 0


if __name__ == "__main__":
  sys.exit(main())

