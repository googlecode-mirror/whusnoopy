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
from utilscore import *
from utilxml import *
from adwordsselector import selectAdWords

def staticAdKe(titles, bodys, refs):
  title = "".join(titles)
  body = "".join(bodys)
  ref = "".join(refs)
  all_text = title * 2 + body + ref
  all_text = all_text.encode('utf-8')

  all_tokens = mmseg.Algorithm(all_text)

  tokens_rank = scoreTokens(all_tokens)

  ad_keywords = selectAdWords(tokens_rank, 6)

  return ad_keywords

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
 
  titles = [p[2] for p in posts]
  bodys = [p[3] for p in posts]
  refs = [p[4][0][1] for p in posts if p[4]]

  adks = staticAdKe(titles, bodys, refs)

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
