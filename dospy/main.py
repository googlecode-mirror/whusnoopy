#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com                                
#
# This module used to get a topic page from bbs.dospy.com, then extract them as
# each post with title/date_time infomations, if there are extra pages for this
# topic, this module can get and extract them also
#

import sys, os, time
from crawl import crawl
from extract import extractPage

argvs = sys.argv

if len(argvs) < 2 :
  printUsage()
  exit(-1)

if len(argvs) < 3 :
  root_dir = '/home/cswenye/dospy_work/'
else :
  root_dir = argvs[2]

url = "%s" % argvs[1]
work_dir = root_dir + url[url.find('thread-'):url.find('-1-1.html')]

if os.path.exists(work_dir) :
  os.chdir(work_dir)
  os.system("rm -rf *")
else :
  os.mkdir(work_dir)
  os.chdir(work_dir)

filelist = crawl(url)

target_prefix = time.strftime("%Y%m%d-%H%M%S")
start_no = 0
for file in filelist :
  extractPage(file, target_prefix, start_no)
  start_no += 15

def printUsage() :
  print 'Usage:'
  print '  ./allinone.py url [work_dir]'

