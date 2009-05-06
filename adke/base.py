#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import logging
import time

from idf import idf

def rankTokens(tokens):
  tokens_rank = {}
  for token in tokens:
    text = token.text
    if not tokens_rank.has_key(text):
      tokens_rank[text] = 0
    tokens_rank[text] += idf[text]
  return tokens_rank

# Indent the new ads node for pretty print
def xmlIndent(dom, node, adwords, indent=' ', newl='\n'):
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

def LOGGER(filename='', level='DEBUG') :
  log = logging.getLogger(__name__)
  log.setLevel(getattr(logging, "%s" % level))
  formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d: %(message)s', '%y-%m-%d,%H:%M:%S')

# Console Logger
  ch = logging.StreamHandler()
  ch.setLevel(logging.ERROR)
  ch.setFormatter(formatter)
  log.addHandler(ch)

# If log to file
  if len(filename) == 0 :
    filename = "/home/cswenye/log/adke." + time.strftime('%Y%m%d%H%M%S') + ".log"
  fh = logging.FileHandler(filename)
  fh.setLevel(logging.INFO)
  fh.setFormatter(formatter)
  log.addHandler(fh)
  
  debug_filename = "/home/cswenye/log/adke.debug." + time.strftime('%Y%m%d%H%M%S') + ".log"
  dfh = logging.FileHandler(debug_filename)
  dfh.setLevel(logging.DEBUG)
  dfh.setFormatter(formatter)
  log.addHandler(dfh)

  return log

if __name__ == '__main__' :
  LOG = LOGGER()
  LOG.info("Hello, this is a logger module")
  LOG.debug("this is a debug info")
else :
  logger = LOGGER()

