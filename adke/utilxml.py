#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

from xml.dom import minidom

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

def outputXmlAdsFile(file_path, sads, pads):
  '''output ads keywords in sads and pads to a xml file on file_path
  '''

  logger.info('write ads to xml file %(file_path)s' % locals())
  # a new document and the root
  doc = minidom.Document()
  ads = doc.createElement('ads')
  doc.appendChild(ads)
  text = doc.createTextNode('\n')
  ads.appendChild(text)

  # sidebar part
  sidebar_ads = doc.createElement("sidebar")
  doc.documentElement.appendChild(sidebar_ads)
  xmlIndent(doc, sidebar_ads, sads[:3])

  # banner part
  banner_ads = doc.createElement("banner")
  doc.documentElement.appendChild(banner_ads)
  xmlIndent(doc, banner_ads, sads[3:])

  for pno, pad in pads.items():
    post_ads = doc.createElement(pno)
    doc.documentElement.appendChild(post_ads)
    xmlIndent(doc, post_ads, pad)

  xmlstr = doc.toxml(encoding='utf-8')
  of = file(file_path, "w")
  of.write(xmlstr)
  of.close()

def extractXmlFile(file_path):
  '''Extract XML File to posts
  return a posts list that every post is a dictionary like:
    {'no'     : %d,
     'time'   : %f, # in seconds
     'title'  : %s,
     'title_tokens' : [token, token, ...], # seged tokens from title
     'body'   : %s,
     'body_tokens'  : [token, token, ...], # seged tokens from body
     'refs'   : [ref, ref, ...]
    }
  and in refs list, a ref is a dictionary like:
    {'id'    : %d,
     'body'  : %s,
     'tokens': [token, token, ...] # seged tokens from ref body
    }
  '''
  logger.info('extract xml file %(file_path)s' % locals())

  from pymmseg import mmseg
  mmseg.dict_load_defaults()

  xmldoc = minidom.parse(file_path)
  posts = []
  post_nodes = xmldoc.getElementsByTagName('post')

  for post_node in post_nodes:
    post = {}
    post['no'] = int(post_node.getAttribute('id'))

    date_time_node = post_node.getElementsByTagName('date_time')[0]
    if date_time_node.firstChild:
      post['time'] = stringToSeconds(date_time_node.firstChild.data)
    else:
      post['time'] = 0

    title_node = post_node.getElementsByTagName('title')[0]
    if title_node.firstChild:
      post['title'] = title_node.firstChild.data
    else:
      post['title'] = ""
    post['title_tokens'] = [t.text \
        for t in mmseg.Algorithm(post['title'].encode('utf-8'))]

    body_node = post_node.getElementsByTagName('body')[0]
    if body_node.firstChild:
      post['body'] = body_node.firstChild.data
    else:
      post['body'] = ""
    post['body_tokens'] = [t.text \
        for t in mmseg.Algorithm(post['body'].encode('utf-8'))]
    
    logger.debug('Got post_%d "%s" post on %f: %s' % \
                 (post['no'], post['title'], post['time'], post['body']))

    refs = []
    for ref_node in post_node.getElementsByTagName('ref'):
      ref = {}
      ref['id'] = int(ref_node.getAttribute('id'))

      # no refer (ref['id'] == 0)
      if not ref['id']:
        continue

      if ref_node.firstChild:
        ref['body'] = ref_node.firstChild.data
      else:
        ref['body'] = ""
      ref['tokens'] = [t.text
          for t in mmseg.Algorithm(ref['body'].encode('utf-8'))]
      
      logger.debug('Got refer to post_%d: %s' % (ref['id'], ref['body']))
      refs.append(ref)

    post['refs'] = refs

    # Every elements extract already, append this post dictionary to posts
    posts.append(post)

  return posts

if __name__ == '__main__' :
  print 'This is a help module, and it exited'

