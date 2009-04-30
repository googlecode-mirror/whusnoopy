#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: cswenye@gmail.com                                
#

__author__ = 'cswenye@gmail.com (Wen YE)'

import sys
import time
import optparse

import logging

def extractPage(pagefile, target = time.strftime('%Y%m%d-%H%M%S'), start_no = 0) :
  log.info('Extract %s to %s from %d' % (pagefile, target, start_no))

  exfilelist = []

  pf = file(pagefile, "r")
  page_content = pf.read()
  pf.close()

  # If ask to output in a single file
  if start_no == -1 :
    target_file_name = target
    tf = file(target_file_name, "w")

  # detect title
  title = detectTitle(page_content)

  # detect each post
  time_start = page_content.find('<div style="padding-top: 4px;">')
  while time_start != -1 :
    if start_no >= 0 :
      target_file_name = target + ".%04d" % start_no
      start_no += 1
      tf = file(target_file_name, "w")

    time_start += 42
    time_end = page_content.find('&nbsp;', time_start)
    date_time = page_content[time_start:time_end]

    content_start = page_content.find('class="t_msgfont">', time_start) + 18
    content_end = page_content.find('</div>\r\n', content_start)
    content = page_content[content_start:content_end]

    reply_start = page_content.find('<span class="bold">回复 #', time_start, content_start)
    log.info('find reply_start from %d to %d at %d: %s' % \
             (time_start, content_start, reply_start, page_content[reply_start+27:reply_start+40]))
    if reply_start == -1 :
      reply_id = -1
    else :
      reply_start += 27
      reply_id = int(page_content[reply_start:page_content.find(' ', reply_start)])
    
    content = grepLastEdit(content)
    content = grepAttach(content)
    content, quote = grepQuote(content)
    content = grepHtmlTag(content)
    content = convertHtmlChar(content)
    content = content.replace('\r', '')

    outcontent = "\n<DOC>\n" \
               + "<DOCNO> %s </DOCNO>\n" % target_file_name \
               + "<DATE_TIME> %s </DATE_TIME>\n" % date_time \
               + "<BODY>\n" \
               + "<CATEGORY> cellphone </CATEGORY>\n" \
               + "<HEADLINE> %s </HEADLINE>\n" % title \
               + "<REPLY> %d </REPLY>\n" % reply_id \
               + "<QUOTE> %s </QUOTE>\n" % quote \
               + "<TEXT>\n" \
               + "%s\n" % content \
               + "</TEXT>\n" \
               + "</BODY>\n" \
               + "</DOC>\n"
    tf.write(outcontent)

    if start_no >= 0 :
      tf.close()
      exfilelist.append(target_file_name)
  
    time_start = page_content.find('<div style="padding-top: 4px;">', time_start)

  if start_no == -1 :
    tf.close()
    exfilelist.append(target_file_name)

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
  quote = ""
  while True :
    tp = content.find('<div class="msgbody"><div class="msgheader">')
    if tp == -1 :
      break
    qs = content.find('\r\n') + 2
    qt = content.find('</div></div>', tp)
    rp = qt + 12
    quote = content[qs:qt]
    content = content[0:tp] + content[rp:]
  return content, quote

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

def main() :
  global log
  log = logging.getLogger(__name__)
  log.setLevel(logging.DEBUG)
  formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d: %(message)s', '%y-%m-%d,%H:%M:%S')
  ch = logging.StreamHandler()
  ch.setFormatter(formatter)
  log.addHandler(ch)

  parser = optparse.OptionParser(usage='%prog [options] FILE')
  parser.add_option('-o', '--output', dest='output',
                    help='Output filename, or use current time defaultly')
  parser.add_option('-s', '--single', dest='single', action='store_true', default=True,
                    help='Output file in a single file or a series files')
  
  options, args = parser.parse_args()

  start_no = options.single and -1 or 0

  if len(args) < 1:
    parser.error('File to extract not provided.')
  elif len(args) > 1:
    parser.error('Only one file may be specified.')

  file_path = args[0]

  if options.output:
    extractPage(file_path, options.output, start_no)
  else:
    extractPage(file_path, start_no=start_no)

  return 0

if __name__ == '__main__' :
  sys.exit(main())

