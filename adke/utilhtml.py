#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: cswenye@gmail.com                                

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

if __name__ == '__main__' :
  print 'This is a helper module'

