#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com                                
#

import re, os
from crawl import getUrlAsFile
from logging import LOG

def spiderMain(site_prefix) :
  index_page_url = site_prefix + "index.php"
  index_page_filename = "index.html"

  getUrlAsFile(index_page_url, index_page_filename)

  index_file = file(index_page_filename, "r")
  content = index_file.read()
  index_file.close()

  forum_list = re.findall(ur'forum-[0-9]{1,3}-1\.html', content)

  url_list = []
  for forum in forum_list :
    thread_list = spiderForum(site_prefix, forum)
    for thread in thread_list :
      url_list.append(thread)

  return url_list

def spiderForum(site_prefix, forum_name) :
  LOG('INFO', 'start to process %s' % forum_name)
  forum_url = site_prefix + forum_name
  if getUrlAsFile(forum_url, forum_name) :
    return []

  forum_file = file(forum_name, "r")
  content = forum_file.read()
  forum_file.close()

  content = content[content.find("论坛主题"):]
  t_list = re.findall(ur'<td class="f_folder"><a href="thread-[0-9]{1,10}-1-1\.html', content)

  thread_list = []
  for t in t_list :
    thread = site_prefix + t[t.find("thread"):]
    thread_list.append(thread)

  return thread_list

if __name__ == '__main__' :
  site = "http://bbs.dospy.com/"

  work_dir = '/home/cswenye/work/'

  if os.path.exists(work_dir) :
    os.chdir(work_dir)
    os.system("rm -f *")
  else :
    os.mkdir(work_dir)
    os.chdir(work_dir)

  spiderMain(site)

