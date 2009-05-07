#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

from base import logger
from base import stringToSeconds

def xmlIndent(dom, node, adwords, indent=' ', newl='\n'):
  '''Insert the adwords as new child nodes of node with pretty print format
  '''
  # Indent each child node
  for token in adwords:
    text = dom.createTextNode(newl + indent)
    node.appendChild(text)
    keyword = dom.createElement("keyword")
    text = dom.createTextNode(token.decode('utf-8'))
    keyword.appendChild(text)
    node.appendChild(keyword)

  # Newline before the end-tag
  text = dom.createTextNode(newl)
  node.appendChild(text)

  # Newlines after the whole node
  text = dom.createTextNode(newl + newl)
  node.parentNode.appendChild(text)

def extractXmlFile(xmldoc):
  '''Extract XML File to posts
  return a posts list that every post is a tuple like:
    ((post_no)d, (date_time)f, (title)s, (body)s, [ref list])
  and in ref list, a ref is a (ref_no, ref_body) tuple
  '''
  posts = []
  post_nodes = xmldoc.getElementsByTagName('post')

  for post_node in post_nodes:
    post_no = int(post_node.getAttribute('id'))

    date_time_node = post_node.getElementsByTagName('date_time')[0]
    if date_time_node.firstChild:
      date_time = stringToSeconds(date_time_node.firstChild.data)
    else:
      date_time = 0

    title_node = post_node.getElementsByTagName('title')[0]
    if title_node.firstChild:
      title = title_node.firstChild.data
    else:
      title = ""

    body_node = post_node.getElementsByTagName('body')[0]
    if body_node.firstChild:
      body = body_node.firstChild.data
    else:
      body = ""
    
    logger.debug('Got post_%(post_no)d "%(title)s" post on %(date_time)d: \
                  %(body)s' % locals())

    refs = []
    for ref_node in post_node.getElementsByTagName('ref'):
      ref_no = int(ref_node.getAttribute('id'))

      # no refer (ref_no == 0)
      if not ref_no:
        continue

      if ref_node.firstChild:
        ref_body = ref_node.firstChild.data
      else:
        ref_body = ""
      logger.debug('Got post_%(post_no)d refer to post_%(ref_no)d: \
                    %(ref_body)s' % locals())

      refs.append((ref_no, ref_body))

    # Every elements extract already, append this to posts as a tuple
    posts.append((post_no, date_time, title, body, refs))

  return posts

if __name__ == '__main__' :
  print 'This is a help module, and it exited'

