#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import os
import sys
import time
import optparse
from xml.dom import minidom

def suitable(file_path, ref_only, strong_ref):
  if ref_only == 'False':
    return True

  # needs reference
  cf = file(file_path, 'r')
  cs = cf.read()
  cf.close()
  if cs.find('<ref') == -1:
    return False

  # needs strong reference
  if strong_ref == 'False':
    return True

  # check valid xml file or not
  try:
    doc = minidom.parse(file_path)
  except Exception, e:
    return False

  refs = doc.getElementsByTagName('ref')
  if len(refs) < 5:
    return False
  count = 0
  for ref in refs:
    if int(ref.parentNode.attributes['id'].value) < 30:
      count += 1
  if count < 5:
    return False

  return True

def genListHtml(filelist, output_file, ref_only, strong_ref):
  dir_path = '/home/cswenye/adke/data/'
  newl = 10
  count = 0
  fl = []
  fl.append('<table><tbody>')
  for t in filelist:
    if not suitable(os.path.join(dir_path, t), ref_only, strong_ref):
      continue
    if count % newl ==0:
      fl.append('<tr>')
    count += 1
    fl.append('<td><a href="demo.php?doc=%s&p=30" target="_blank">%s</a><td>' % (t, t[7:t.find('-',7)]))
    if count % newl == 0:
      fl.append('</tr>')

  if count % newl != 0:
    fl.append('</tr>')
  fl.append('</tbody></table>')

  htmlstr = "\n".join(fl)
  of = file(output_file, 'w')
  of.write(htmlstr)
  of.close()

  print 'listed files on %s: %d' % (time.strftime('%Y-%m-%d %H:%M:%S'), count)

  return 0

def main():
  # args and options init
  parser = optparse.OptionParser(usage='%prog [options] [dir]')
  parser.add_option('-o', '--output_path', dest='output',
                    help='Output filename, or will use ~/adke/demo/list.html defaultly')
  parser.add_option('-r', '--ref_only', action="store_true", dest='ref_only', default='False',
                    help='List pages only have refences or all pages')
  parser.add_option('-s', '--strong_ref', action="store_true", dest='strong_ref', default='False',
                    help='List pages only have refences or all pages')
  options, args = parser.parse_args()

  # the input dir process
  if len(args) < 1:
    dir_path = '/home/cswenye/adke/data/'
    filelist = os.listdir(dir_path)
    print 'All extract xml files on %s: %d' % (time.strftime('%Y-%m-%d %H:%M:%S'), len(filelist))
  elif len(args) > 1:
    parser.error('Only one dir may be specified.')
  else:
    inf = file(args[0], 'r')
    filelist = inf.readlines()
    filelist = [t[:-1] for t in filelist]
    inf.close()

  if options.output:
    output_file = os.path.abspath(options.output)
  else:
    output_file = "/home/cswenye/adke/demo/list.html"

  return genListHtml(filelist, output_file, options.ref_only, options.strong_ref)

if __name__ == "__main__":
  sys.exit(main())

