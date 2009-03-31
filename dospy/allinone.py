#!/usr/bin/python
#
# author: cswenye@gmail.com                                
#
# This module used to get a topic page from bbs.dospy.com, then extract them as
# each post with title/date_time infomations, if there are extra pages for this
# topic, this module can get and extract them also
#

import sys, os, urllib2

def main() :
  argvs = sys.argv

  # get the url, and mkdir for this work
  if len(argvs) < 2 :
    printUsage()
    exit(-1)
  else :
    url = "%s" % argvs[1]
  dir_name = url

  # get web page, and save it as a local file
  getUrlAsFile(url, filename)

  # do extraction on current page

  # if there is a multi pages topic, get the after pages, and extract them
  f = file(filename, "r")
  page_content = f.read()
  pages = multiPageChek(page_content)
  if (pages > 1) :
    for page_index in range(2, pages + 1) :
      url = "%s" % argvs[1]
      getUrlAsFile(url, filename)

def printUsage() :
  print 'Usage:'
  print '  ./allinone.py url'
def getUrlAsFile(url, filename) :
  wp = urllib2.urlopen(url)
  wp_content = wp.read()
  f = file(filename, "w")
  f.write(wp_content)

def multiPage(content) :
  if (content) :
    return 
  else :
    return 0

if __name__ == '__main__' :
  main()
