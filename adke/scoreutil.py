#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

from base import logger
from idf import idf

def scoreTokens(tokens):
  tokens_rank = {}
  for token in tokens:
    text = token.text
    if not tokens_rank.has_key(text):
      tokens_rank[text] = 0
    tokens_rank[text] += idf[text]
  return tokens_rank

if __name__ == '__main__' :
  print 'This is a help module, and it exited'

