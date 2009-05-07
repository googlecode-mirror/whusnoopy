#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import os
import sys
import optparse

from xml.dom import minidom
from pymmseg import mmseg

mmseg.dict_load_defaults()

from base import *
from scoreutil import *
from xmlutil import *
from adwordsselector import selectAdWords

def updatePost(posts, pwords, pi):
  pass

def initPost(posts, pwords, pi):
  pass

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

  pwords = {}
  for p in posts:
    post_no = p[0]
    pwords = initPost(posts, pwords, post_no)
    for i in range(1,post_no):
      updatePost(posts, pwords, i)
    
    print '========>'
    print p[0], p[1], p[2].encode('utf-8')
    print p[3].encode('utf-8')
    for ref in p[4]:
      print '----'
      print ref[0], ref[1]
    print '<<'

  if not options.output:
    for token in adks:
      print token
  else:
    doc = xmldoc
    sidebar_ads = doc.createElement("ads")
    doc.documentElement.appendChild(sidebar_ads)
    xmlIndent(doc, sidebar_ads, adks[:3])

    of = file(options.output, "w")
    of.write(doc.toxml(encoding='utf-8'))
    of.close

  return 0


if __name__ == "__main__":
  sys.exit(main())
