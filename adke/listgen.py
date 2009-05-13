#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import os
import sys
import time
import optparse

def genListHtml(dir_path, output_file, ref_only):
  filelist = os.listdir(dir_path)
  print 'All extract xml files on %s: %d' % (time.strftime('%Y-%m-%d %H:%M:%S'), len(filelist))

  newl = 10
  count = 0
  fl = []
  fl.append('<table><tbody>')
  for t in filelist:
    if ref_only:
      cf = file(os.path.join(dir_path, t), "r")
      cs = cf.read()
      cf.close()
      if cs.find('<ref') == -1:
        continue
    if count % newl ==0:
      fl.append('<tr>')
    count += 1
    fl.append('<td><a href="demo.php?doc=%s&p=150" target="_blank">%s</a><td>' % (t, t[7:t.find('-',7)]))
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
  options, args = parser.parse_args()

  # the input dir process
  if len(args) < 1:
    dir_path = '/home/cswenye/adke/data/'
  elif len(args) > 1:
    parser.error('Only one dir may be specified.')
  else:
    dir_path = os.path.abspath(args[0])

  if options.output:
    output_file = os.path.abspath(options.output)
  else:
    output_file = "/home/cswenye/adke/demo/list.html"

  ref_only =  options.ref_only

  return genListHtml(dir_path, output_file, ref_only)

if __name__ == "__main__":
  sys.exit(main())

