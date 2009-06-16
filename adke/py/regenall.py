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
  parser = optparse.OptionParser(usage='%prog [options] FILE')
  parser.add_option('-o', '--output_path', dest='output',
                    help='Output filename, or will use FILE.ads[n] defaultly')
  parser.add_option('-r', '--regen', action="store_true", dest='regen', default=False,
                    help='Re-generate ads from xml files')
  parser.add_option('-u', '--update', action="store_true", dest='update', default=False,
                    help='Update whether there file exsists')
  options, args = parser.parse_args()

  # the input file process
  if len(args) < 1:
    if options.regen:
      list_file = file('/home/cswenye/snoopy/adke/xmllist', "r")
      files = [t[:-1] for t in list_file.readlines()]
      list_file.close()
    else:
      list_file = file('/home/cswenye/work/list_of_threads', "r")
      files = [t[:-1] for t in list_file.readlines()]
      list_file.close()
    # parser.error('list file to extract not provided.')
  else:
    files = args

  if options.output:
    output_file_prefix = options.output
  else:
    output_file_prefix = "/home/cswenye/adke/data/"

  count = 0
  for file_path in files:
    count += 1
    thread = os.path.splitext(os.path.split(file_path)[1])[0]

    output_file_path = os.path.join(output_file_prefix, thread + '.xml')
    if os.path.exists(output_file_path):
      if options.update:
        print "[INFO] %s processed already, but update" % output_file_path
      else:
        print "[FAULT] %s processed already, skip" % output_file_path
        continue

    print '[INFO] process %s' % file_path

    if options.regen:
      posts = readXmlFile(file_path, 30)
    else:
      posts = []
      for i in range(1,11):
        file_path = "%s%d%s" % (file_path[:-8], i, file_path[-7:])
        print "start process file %s" % file_path

        if not os.path.exists(file_path):
          break
        posts = extractPage(file_path, posts)

    if not posts:
      print '[ERROR] no post in %s, skip it' % file_path
      continue
    print '[INFO] read %d posts from %s' % (len(posts), file_path)

    ads = genUpdateAds(posts)

    print "[INFO] {%d} gen ads finish, write into %s" % (count, output_file_path)
    outputXmlAdsFile(output_file_path, posts, ads)

  return 0


if __name__ == "__main__":
  sys.exit(main())

