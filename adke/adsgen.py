#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com

from base import logger
from idf import idf

def scoreTokens(tokens, weight=1, scored_tokens={}):
  '''Help function to generate the tf-idf value for each token in tokens,
  return the sorted tokens dictionary
  '''
  for token in tokens:
    if not scored_tokens.has_key(token):
      scored_tokens[token] = 0
    scored_tokens[token] += idf[token]*weight

  return scored_tokens

def isAdWords(token):
  return True

def isStopWords(token):
  return False

def selectAdWords(scored_tokens, words_number=3, score_limit=1):
  ranked_tokens = sorted(scored_tokens.items(), \
                         cmp=(lambda x, y: cmp(y[1], x[1])))
  ad_words_count = 0
  ad_words = []

  for token, score in ranked_tokens:
    if score < score_limit:
      logger.debug("ad word candidate's score from %(token)s(%(score)f) "
                   "less than limit, skip the following ones" % locals())
      break

    if not isAdWords(token):
      logger.debug('%(token)s(%(score)f) is not ad word, skip it' % locals())
    elif isStopWords(token):
      logger.debug('%(token)s(%(score)f) is stopword, skip it' % locals())
    else:
      ad_words.append(token)
      ad_words_count += 1
      logger.debug('%(token)s(%(score)f) is selected as '
                   '%(ad_words_count)d ad word' % locals())

    if ad_words_count == words_number:
      logger.debug("got enough adwords, exit")
      break

  return ad_words

def generateAdWords(posts, static_num=6, post_num=3):
  '''Generate ad words from posts
  return static_ads, post_ads
    the static_ads is an ads words list for banner and sidebar
    the post_ads is a dictionary contains ads words list for each post, like:
      {'p1' : [adsword, adsword, ...],
       'p2' : [adsword, adsword, ...]
      }
  '''

  # parameters
  mu = 0.9      # for each post, the own part weight
  beta = 2      # quote weight
  alpha = 1.5   # refer weight
  zeta = 2      # title weight
  gamma = 1     # distance weight

  # generate the ads words for the whole page
  for p in posts:
    scored_tokens = scoreTokens(p['title_tokens'], zeta)
    scored_tokens = scoreTokens(p['body_tokens'], scored_tokens=scored_tokens)
    for ref in p['refs']:
      scored_tokens = scoreTokens(ref['tokens'], scored_tokens=scored_tokens)
  static_ads = selectAdWords(scored_tokens, static_num)
  adskeywords = " ".join(static_ads)
  logger.info('got static ads as %(adskeywords)s' % locals())

  post_ads = {}
  for p in posts:
    # original weight
    scored_tokens = {}
    scored_tokens = scoreTokens(p['title_tokens'], zeta*p['weight']*mu, scored_tokens)
    scored_tokens = scoreTokens(p['body_tokens'], p['weight']*mu, scored_tokens)
    # for bref in p['brefs']:

    # other posts' token value
    for ref in p['refs']:
      refp = posts[ref['id']]
      if ref['tokens']:
        # part quote
        scored_tokens = scoreTokens(ref['tokens'], beta*refp['weight']*(1.0-mu))
      else:
        # refer, consier the body only
        scored_tokens = scoreTokens(refp['body_tokens'], alpha*refp['weight']*(1.0-mu))
     
    ads = selectAdWords(scored_tokens, post_num)
    key = 'p%d' % p['no']
    post_ads[key] = ads
    adskeywords = " ".join(ads)
    logger.info('got %(key)s ads as %(adskeywords)s' % locals())

  return static_ads, post_ads

if __name__ == '__main__':
  print 'This is a help module'

