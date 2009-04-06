#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com                                
#

import sys, time

def extractPage(pagefile, target = time.strftime('%Y%m%d-%H%M%S'), start_no = 0) :
#  print 'Extract %s to %s from %d' % (pagefile, target, start_no)

  exfilelist = []

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
    exfilelist.append(target_file_name)
  
    time_start = page_content.find('<div style="padding-top: 4px;">', time_start)

  return exfilelist

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

if __name__ == '__main__' :
  extractPage(sys.argv[1])

