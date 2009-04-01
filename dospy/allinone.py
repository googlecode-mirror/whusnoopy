#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com                                
#
# This module used to get a topic page from bbs.dospy.com, then extract them as
# each post with title/date_time infomations, if there are extra pages for this
# topic, this module can get and extract them also
#

import sys, os, time, urllib2

def main() :
  argvs = sys.argv

  if len(argvs) < 2 :
    printUsage()
    exit(-1)

  url = "%s" % argvs[1]
  start_point = url.find('thread-')
  end_point = url.find('-1-1.html')
  work_dir = '/home/cswenye/dospy_work/' + url[start_point:end_point]
#
#  if len(argvs) < 3 :
#    # check = raw_input('Need use /home/cswenye/dospy_work as work dir? [y/n]')
#    check = 'y'
#    if len(check) == 0 or check[0] == 'Y' or check[0] == 'y' :
#      work_dir = '/home/cswenye/dospy_work'
#    else :
#      work_dir = raw_input('Work dir you like (in absolutely path) :')
#  else :
#    work_dir = "%s" % argvs[2]
#
#  dir_name = workdir + '/' + url[start_point:end_point]

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

def crawl(url) :
  filelist = []
  # get web page, translate it to unicode and save it as a local file
  filename = url[url.find('thread-'):]
  getUrlAsFile(url, filename)
  filelist.append(filename)

  # if there is a multi pages topic, get the after pages, and extract them
  pages = multiPage(filename)
  if (pages > 1) :
    for page_index in range(2, pages + 1) :
      current_url = url[:url.find("-1-")] + "-%d-1.html" % page_index
      filename = current_url[current_url.find('thread-'):]
      getUrlAsFile(current_url, filename)
      filelist.append(filename)

  return filelist

def getUrlAsFile(url, filename) :
  wp = urllib2.urlopen(url)
  wp_content = wp.read()
  decode_content = wp_content.decode('gbk')
  f = file(filename, "w")
  f.write(decode_content.encode('utf-8'))

def multiPage(filename) :
  f = file(filename, "r")
  content = f.read()
  start_point = content.find('class="p_pages">&nbsp;1/')
  if start_point != -1 :
    start_point += 24
    end_point = content.find('&nbsp;', start_point)
    num = content[start_point:end_point]
    return int(num)
  else :
    return 0

def extractPage(pagefile, target = time.strftime('%Y%m%d-%H%M%S'), start_no = 0) :
  print 'Extract %s to %s from %d' % (pagefile, target, start_no)

  pf = file(pagefile, "r")
  page_content = pf.read()

  # detect title
  title = detectTitle(page_content)

  # detect each post
  time_start = page_content.find('<div style="padding-top: 4px;">')
  while time_start != -1 :
    target_file_name = target + ".%04d" % start_no
    start_no += 1
    tf = file(target_file_name, "w")

    time_start += 42
    time_end = page_content.find('&nbsp;', time_start)
    date_time = page_content[time_start:time_end]

    content_start = page_content.find('class="t_msgfont">', time_start) + 18
    content_end = page_content.find('</div>\r\n', content_start)
    content = page_content[content_start:content_end]

    content = grepLastEdit(content)
    content = grepAttach(content)
    content = grepQuote(content)
    content = grepHtmlTag(content)
    content = convertHtmlChar(content)
    content = content.replace('\r', '')

    outcontent = "\n<DOC>\n" \
               + "<DOCNO> %s </DOCNO>\n" % target_file_name \
               + "<DATE_TIME> %s </DATE_TIME>\n" % date_time \
               + "<BODY>\n" \
               + "<CATEGORY> cellphone </CATEGORY>\n" \
               + "<HEADLINE> %s </HEADLINE>\n" % title \
               + "<TEXT>\n" \
               + "%s\n" % content \
               + "</TEXT>\n" \
               + "</BODY>\n" + "</DOC>\n"
    tf.write(outcontent)
  
    time_start = page_content.find('<div style="padding-top: 4px;">', time_start)

def detectTitle(content) :
  tsp = content.find('<div class="subtable nav"')
  ttp = content.find('</div>', tsp)
  while content.find('&raquo;', tsp, ttp) != -1 :
    tsp = content.find('&raquo;', tsp, ttp) + 7
  return content[tsp:ttp]

def grepLastEdit(content) :
  while True :
    tp = content.find('[<i> 本帖最后由')
    if tp == -1 :
      break
    rp = content.find('</i>]', tp) + 5
    content = content[0:tp] + content[rp:]
  return content

def grepAttach(content) :
  while True :
    tp = content.find('<span style="white-space:nowrap" id="attach_')
    if tp == -1 :
      break
    rp = content.find('</span>', tp) + 7
    content = content[0:tp] + content[rp:]

  while True :
    tp = content.find('<div title="menu" class="t_attach"')
    if tp == -1 :
      break
    rp = content.find('</div></div>', tp) + 12
    content = content[0:tp] + content[rp:]

  return content

def grepQuote(content) :
  while True :
    tp = content.find('<div class="msgbody"><div class="msgheader">')
    if tp == -1 :
      break
    rp = content.find('</div></div>', tp) + 12
    content = content[0:tp] + content[rp:]
  return content

def grepHtmlTag(content) :
  while True :
    tp = content.find('<')
    if tp == -1 :
      break
    rp = content.find('>', tp) + 1
#    print '\n>>>>\n in %s grep %s \n>>>> after <<<<\n %s\n<<<<\n' % (content, content[tp:rp], content[0:tp] + content[rp:])
    content = content[0:tp] + content[rp:]
  return content

def convertHtmlChar(content) :
  html_tags = { '&nbsp;' : ' ',
                '&amp;'  : '&',
                '&lt;'   : '<',
                '&gt;'   : '>',
                '&quot;' : '"'
              }
  for html_tag, html_char in html_tags.items() :
#    print '\n>>>> before replace %s as %s >>>>\n%s' % (html_tag, html_char, content)
    content = content.replace(html_tag, html_char)
#    print '\n<<<< after replace %s as %s <<<<\n%s' % (html_tag, html_char, content)

  return content

# Main function call
if __name__ == '__main__' :
  main()

