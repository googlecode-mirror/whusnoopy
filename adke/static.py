#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import os
import sys
import optparse

from xml.dom import minidom

from base import logger
from utilxml import *
from adwordsselector import generateAdWords

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
 
  adks, ua = generateAdWords(posts)

  if not options.output:
    for token in adks:
      print token
  else:
    doc = xmldoc
    sidebar_ads = doc.createElement("sidebar_ads")
    doc.documentElement.appendChild(sidebar_ads)
    xmlIndent(doc, sidebar_ads, adks[:3])

    banner_ads = doc.createElement("banner_ads")
    doc.documentElement.appendChild(banner_ads)
    xmlIndent(doc, banner_ads, adks[3:])

    of = file(options.output, "w")
    of.write(doc.toxml(encoding='utf-8'))
    of.close

  return 0

if __name__ == "__main__" :
  sys.exit(main())
