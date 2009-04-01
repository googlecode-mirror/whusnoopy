#!/usr/bin/python
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

  # get the url, and mkdir for this work
  if len(argvs) < 2 :
    printUsage()
    exit(-1)

  url = "%s" % argvs[1]
  start_point = url.find('thread-')
  end_point = url.find('-1-1.html')
  dir_name = url[start_point:end_point]
  target_prefix = dir_name + '/' + time.strftime("%Y%m%d-%H%M%S")

  if os.path.exists(dir_name) :
    os.removedirs(dir_name)

  os.mkdir(dir_name)
  # TODO: the 'cd' command not work, need to find an other way to change work dir,
  #       if change work dir succussed, need to modify the following settings
  # os.system("cd %s" % dir_name)
  filename = dir_name + "/" + url[start_point:]

  # get web page, translate it to unicode and save it as a local file
  getUrlAsFile(url, filename)

  # do extraction on current page
  extractPage(filename, target_prefix, 0)

  # if there is a multi pages topic, get the after pages, and extract them
  pages = multiPage(filename)
  # print 'we got %d pages' % pages
  if (pages > 1) :
    for page_index in range(2, pages + 1) :
      origin_url = "%s" % argvs[1]
      url = origin_url[:origin_url.find("-1-")] + "-%d-1.html" % page_index
      filename = dir_name + "/" + url[url.find('thread-'):]
      
      # print "now get %s (%d) as %s" % (url, page_index, filename)
      getUrlAsFile(url, filename)
      extractPage(filename, target_prefix, (page_index - 1) * 15)

def printUsage() :
  print 'Usage:'
  print '  ./allinone.py url'

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

def extractPage(pagefile, target = time.strftime('%Y%m%d-%H%M%S"'), start_no = 0) :
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

    content = grepAttach(content)
    content = grepQuote(content)
    content = grepHtmlTag(content)
    content = convertHtmlChar(content)

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
    tsp = content.find('&raquo;', tsp, ttp) + 8
  return content[tsp:ttp]

def grepAttach(content) :
  running = True
  while running :
    tp = content.find('<span style="white-space:nowrap" id="attach_')
    if tp == -1 :
      break
    rp = content.find('</span>', tp) + 8
    content = content[0:tp] + content[rp:]
  return content

def grepQuote(content) :
  running = True
  while running :
    tp = content.find('<div class="msgbody"><div class="msgheader">')
    if tp == -1 :
      break
    rp = content.find('</div></div>', tp) + 13
    content = content[0:tp] + content[rp:]
  return content

def grepHtmlTag(content) :
  running = True
  while running :
    tp = content.find('<')
    if tp == -1 :
      break
    rp = content.find('>', tp) + 2
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
    content = content.replace(html_tag, html_char)

  return content

# Main function call
if __name__ == '__main__' :
  main()

