#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com                                
#

import sys, urllib2, os
from logging import LOG

def crawl(url) :
  filelist = []
  # get web page, translate it to unicode and save it as a local file
  filename = url[url.find('thread-'):]
  if getUrlAsFile(url, filename) == False :
    return []

  filelist.append(filename)

  # if there is a multi pages topic, get the after pages, and extract them
  pages = checkMultiPage(filename)
  if (pages > 1) :
    for page_index in range(2, pages + 1) :
      current_url = url[:url.find("-1-")] + "-%d-1.html" % page_index
      filename = current_url[current_url.find('thread-'):]
      if getUrlAsFile(current_url, filename) == True :
        filelist.append(filename)

  return filelist

def getUrlAsFile(url, filename) :
  # avoid re-crawl, if need update, remove the following line
  if os.path.exists(filename) :
    return True
  try :
    wp = urllib2.urlopen(url)
    wp_content = wp.read()
    decode_content = wp_content.decode('gbk')
    f = file(filename, "w")
    f.write(decode_content.encode('utf-8'))
    f.close()
  except UnicodeDecodeError :
    LOG('ERROR', "Can't decode page %s" % url)
    return False
  except :
    LOG('ERROR', "Unknown Error during crawl %s" % url)
    return False

  return True

def checkMultiPage(filename) :
  f = file(filename, "r")
  content = f.read()
  f.close()
  start_point = content.find('class="p_pages">&nbsp;1/')
  if start_point != -1 :
    start_point += 24
    end_point = content.find('&nbsp;', start_point)
    num = content[start_point:end_point]
    return int(num)
  else :
    return 0

if __name__ == '__main__' :
  crawl(sys.argv[1])

