#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: cswenye@gmail.com                                

import time

from base import logger
from base import stringToSeconds

def detectNextPost(page_content, pos=0):
  post_start = page_content.find('<table border="0" cellspacing="0" cellpadding="4" class="t_msg">', pos)
  if post_start < 0:
    return "", pos

  post_end = page_content.find('</table>', post_start) + 8
  post = page_content[post_start:post_end]

  return post, post_end

def detectPostNo(post_content, pos=0):
  '''extract pno and pid from content at postion pos
  return %(pno)d, %(pid)d, %(npos)d
  '''

  no_start = post_content.find('">#', pos) + 3
  no_end = post_content.find('</a>', no_start)
  pno = int(post_content[no_start:no_end])

  id_start = post_content.find('message', no_end) + 7
  id_end = post_content.find("'", id_start)
  pid = int(post_content[id_start:id_end])

  return pno, pid, id_end

def detectDateTime(post_content, pos):
  '''extract date from content at postion pos
  return %(date)s, %(time)f, %(npos)d # time is time in seconds
  '''

  time_start = post_content.find('<div style="padding-top: 4px;">', pos) + 42
  time_end = post_content.find('&nbsp;', time_start)
  date_time = post_content[time_start:time_end]
  seconds = time.mktime(time.strptime(date_time, '%Y-%m-%d %H:%M'))

  return date_time, seconds, time_end

def detectTitleAndReply(post_content, pos):
  '''extract title from content at positon pos
  return %(title)s, %(reply_id)d, %(npos)d
  '''

  title_start = post_content.find('</a>\n</div>\n<span class="bold">', pos)
  # post with no title
  if title_start == -1:
    return "", 0, pos
  
  title_start += 31
  title_end = post_content.find('</span>', title_start)
  title = post_content[title_start:title_end]

  if title.startswith('回复 #'):
    reply_id = int(title[8:title.find(' ', 8)])
    title = ""
  else:
    reply_id = 0

  return title, reply_id, title_end

def detectBodyAndQuotes(post_content, pos):
  '''extract title from content at positon pos
  return %(title)s, %(reply_id)d, %(npos)d
  '''

  body_start = post_content.find('class="t_msgfont">', pos) + 18
  body_end = post_content.find('</div>\r\n<br><font', body_start)
  body_content = post_content[body_start:body_end]

  body_content, quotes = splitQuotes(body_content)
  body_content = grepLastEdit(body_content)
  body_content = grepHtmlTag(body_content)
  body_content = convertHtmlChar(body_content)
  body_content = body_content.replace('\r', '')

  return body_content, quotes, body_end

def splitQuotes(content):
  quotes = []
  while True:
    tp = content.find('<div class="msgbody"><div class="msgheader">')
    if tp == -1 :
      break

    quote = {}
    qids = content.find('&amp;pid=', tp) + 9
    qidt = content.find('&amp;', qids)
    quote['id'] = int(content[qids:qidt])
    qs = content.find('\r\n', tp) + 2
    qt = content.find('</div></div>', tp)
    quote['body'] = content[qs:qt]
    quotes.append(quote)

    rp = qt + 12
    content = content[0:tp] + content[rp:]

  return content, quotes

def grepLastEdit(content) :
  while True :
    tp = content.find('[<i> 本帖最后由')
    if tp == -1 :
      break
    rp = content.find('</i>]', tp) + 5
    content = content[0:tp] + content[rp:]
  return content

def grepHtmlTag(content) :
  while True :
    tp = content.find('<')
    if tp == -1 :
      break
    rp = content.find('>', tp) + 1
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

if __name__ == '__main__':
  print 'This is a help module'

