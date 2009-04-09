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
from pymmseg import mmseg
from tfidf import calcTf, calcTfIdf
from spider import spiderMain
from logging import LOG

# test part begin
def segwords(filename, output_file) :
  f = file(filename, 'r')
  content = f.read()
  title = content[content.find("<HEADLINE>") + 10 : content.find("</HEADLINE>")]
  body =  content[content.find("<TEXT>") + 7 : content.find("</TEXT>") - 1]
  output_file.write("title : %s\n" % title)
  output_file.write("body : %s\n" % body)
  output_file.write("----\n")
  text = title * 2 + body
  tokens = mmseg.Algorithm(text)
  words = []
  for token in tokens :
    # print '%s [%d -> %d]' % (token.text, token.start, token.end)
    words.append(token.text)
  return words
# test part end

def processSinglePage(url) :
  work_dir = root_dir + os.sep + url[url.find('thread-'):url.find('-1-1.html')]

  if os.path.exists(work_dir) :
    os.chdir(work_dir)
#    os.system("rm -rf *")
  else :
    os.mkdir(work_dir)
    os.chdir(work_dir)

  output_file_name = work_dir + os.sep + 'extract_result'
#  print output_file_name, os.path.exists(output_file_name)
  if os.path.exists(output_file_name) :
    LOG('INFO', 'extracted finished, skip this page: %s' % url)
    return

  LOG('INFO', 'start to process page %s' % url)
  webpage_filelist = crawl(url)

  all_extracted_filelist = []
  target_prefix = time.strftime("%Y%m%d-%H%M%S")
  start_no = 0
  for webpage in webpage_filelist :
    extracted_filelist = extractPage(webpage, target_prefix, start_no)
    for extracted_file in extracted_filelist :
      all_extracted_filelist.append(extracted_file)
    start_no += 15

  output_file = file(output_file_name, 'w')
  for ef in all_extracted_filelist :
    output_file.write('>>>>>>>v  %s  v>>>>>>>\n' % ef)
    words = segwords(ef, output_file)
    tf = calcTf(words)
    tfidf = calcTfIdf(tf)
    for wp in tfidf :
#      if wp[1] == 0 :
#        break
      output_file.write('  %s : %lf\n' % (wp[0], wp[1]))
    output_file.write('=======^  %s  ^=======\n\n' % ef)

  output_file.close()

def crawlWholeSite(site) :
  if os.path.exists(root_dir) :
    os.chdir(root_dir)
  else :
    os.mkdir(root_dir)
    os.chdir(root_dir)

  LOG('INFO', 'start to process the whole site : %s' % site)
  thread_list_filename = root_dir + os.sep + 'list_of_threads'
  if os.path.exists(thread_list_filename) :
    LOG('INFO', 'forums extracted already, read threads from %s' % thread_list_filename)
    thread_list_file = file(thread_list_filename, 'r')
    thread_list = thread_list_file.read().split('\n')
    thread_list_file.close()
    for thread in thread_list :
      processSinglePage(thread)
  else :
    LOG('INFO', 'forums not extracted already, extract forums and threads to %s' % thread_list_filename)
    thread_list = spiderMain(site)
    thread_list_file = file(thread_list_filename, 'w')
    for thread in thread_list :
      thread_list_file.write("%s\n" % thread)
    thread_list_file.close()

    for thread in thread_list :
      processSinglePage(thread)

def printUsage() :
  print 'Usage:'
  print '  ./allinone.py [--url=] [--site=] [--work_dir=]'
  print '    --url : if miss, crawl whole site defaultly'
  print '    --site : if miss, crawl http://bbs.dospy.com/ defaultly'
  print '    --work_dir : if miss, use /home/cswenye/work/ defaultly'

if __name__ == '__main__' :
  argvs = sys.argv[1:]

  url = ''
  site = 'http://bbs.dospy.com/'
  global root_dir
  root_dir = '/home/cswenye/work'

  for argv in argvs :
    if argv.startswith('--') :
      if argv.startwith('--url=') :
        url = argv[7:]
      elif argv.startwith('--work_dir=') :
        root_dir = argv[11:]
      else :
        printUsage()
        exit(-1)
    else :
      printUsage()
      exit(-1)

  mmseg.dict_load_defaults()

  if len(url) == 0 :
    crawlWholeSite(site)
  else :
    processSinglePage(url)

