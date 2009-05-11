#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

from base import logger
def convertChar(content) :
  html_tags = {
#                '&nbsp;' : ' ',
                '&amp;'  : '&',
                '&lt;'   : '<',
                '&gt;'   : '>',
#                '&quot;' : '"'
              }
  for html_tag, html_char in html_tags.items() :
    content = content.replace(html_char, html_tag)

  return content

def outputXmlAdsFile(file_path, posts, ads):
  '''output ads keywords in sads and pads to a xml file on file_path
  '''

  logger.info('write ads to xml file %(file_path)s' % locals())
  xmlstr = []
  xmlstr.append('<?xml version="1.0" encoding="utf-8"?>')
  xmlstr.append('<page>\n')

  # posts
  xmlstr.append('<topic>\n')
  for post in posts:
    xmlstr.append('<post id="%d">' % post['no'])
    xmlstr.append(' <date_time>%s</date_time>' % post['date'])
    xmlstr.append(' <title>%s</title>' % convertChar(post['title']))
    for ref in post['refs']:
      xmlstr.append(' <ref id="%d">%s</ref>' % (ref['no'], convertChar(ref['body'])))
    xmlstr.append(' <body>%s</body>' % convertChar(post['body']))
    xmlstr.append('</post>\n')
  xmlstr.append('</topic>\n')

  # ads
  xmlstr.append('<ads>\n')
  ts = 0
  for tads in ads:
    ts += 1
    xmlstr.append('<tads id="%d">' % ts)
    # ads for whole page without reinforcement
    kws = ["<kw>%s</kw>" % k for k in tads[0]]
    padstr = "".join(kws)
    xmlstr.append(' <banner>%s</banner>' % padstr)
    # ads for whole page with reinforcement
    kws = ["<kw>%s</kw>" % k for k in tads[1]]
    padstr = "".join(kws)
    xmlstr.append(' <sidebar>%s</sidebar>' % padstr)
    # ads for posts
    pno = 0
    for pads in tads[2:]:
      pno += 1
      kws = ["<kw>%s</kw>" % k for k in pads]
      padstr = "".join(kws)
      xmlstr.append(' <pads id="%d">%s</pads>' % (pno, padstr))
    xmlstr.append('</tads>\n')
  xmlstr.append('</ads>\n')

  xmlstr.append('</page>\n')

  of = file(file_path, "w")
  of.write("\n".join(xmlstr))
  of.close()

if __name__ == '__main__' :
  print 'This is a help module, and it exited'

