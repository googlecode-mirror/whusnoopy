#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, os
from crawl import getUrlAsFile

def spiderMain() :
  index_page_url = site_prefix + "index.php"
  index_page_filename = "index.html"

  getUrlAsFile(index_page_url, index_page_filename)

  index_file = file(index_page_filename, "r")
  content = index_file.read()

  forum_list = re.findall(ur'forum-[0-9]{1,3}-1\.html', content)

  for forum in forum_list :
    spiderForum(forum)

def spiderForum(forum_name) :
  forum_url = site_prefix + forum_name
  getUrlAsFile(forum_url, forum_name)

  forum_file = file(forum_name, "r")
  content = forum_file.read()

  content = content[content.find("论坛主题"):]
  thread_list = re.findall(ur'<td class="f_folder"><a href="thread-[0-9]{1,10}-1-1\.html', content)

  print "\n>>>> threads in %s >>>>" % forum_name
  for t in thread_list :
    thread = t[t.find("thread"):]
    print "%s" % thread
  print "<<<<<<  END  <<<<<<"

if __name__ == '__main__' :
  global site_prefix
  site_prefix = "http://bbs.dospy.com/"

  work_dir = '/home/cswenye/dospy_work/'

  if os.path.exists(work_dir) :
    os.chdir(work_dir)
    os.system("rm -f *")
  else :
    os.mkdir(work_dir)
    os.chdir(work_dir)

  spiderMain()

