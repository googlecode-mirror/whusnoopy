#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

import sys

from base import logger

def my_cmp(E1, E2):
  return -cmp(E1[1], E2[1])

def isAdWords(token):
  return True

def selectAdWords(ranked_tokens, words_number=3):
  tokens = 0
  ad_words = []

  for token, score in sorted(ranked_tokens.items(), cmp=my_cmp):
    logger.debug('ad word candidate %(token)s(%(score)f)' % locals())
    if tokens >= words_number:
      continue
    if isAdWords(token):
      ad_words.append(token)
      tokens += 1
      logger.debug('%(token)s(%(score)f) is selected as %(tokens)d ad word' % locals())
    else:
      logger.debug('%(token)s(%(score)f) is not ad word, skip it' % locals())
    '''
    if tokens >= words_number:
      break
    '''

  return ad_words

if __name__ == '__main__':
  ranked_tokens = {
    'blue' : 33,
    'orange' : 25.3,
    'red' : 34.2,
    'yellow' : 28
  }
  sys.exit(selectAdWords(ranked_tokens))
