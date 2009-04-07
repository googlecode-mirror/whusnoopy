#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com                                
#

import os, sys
from math import log

class idf :
  idf = { }

  def __init__(self, dic_name) :
    # from the dic file generate words info
    print 'generate idf info from %s' % dic_name
    f = file(dic_name, "r")
    while True :
      word_info = f.readline()
      if len(word_info) == 0 :
        break
      infos = word_info.split()
      word = "%s" % infos[0]
      freq = float(infos[1])
      self.idf[word] = float(log(1000000000.0 / freq))

      '''
      # add the part of speech info
      if len(infos[2]) > 0
        s
      '''

    f.close()
    print 'generate idf info finished'

  def __getitem__(self, key) :
    if self.idf.has_key(key) :
      return self.idf[key]
    else :
      return 0

  def __len__(self) :
    return len(words)

def calcTfIdf(tf_list) :
  sogou_dic = "/home/cswenye/snoopy/data/sogou_utf8.dic"
  idf_list = idf(sogou_dic)
  tfidf = { }
  for w, tf in tf_list.items() :
    tfidf[w] = tf * idf_list[w]

#  tfidf.sort(my_cmp)
  return tfidf

def my_cmp(x, y) :
  return x[2] - y[2]

if __name__ == '__main__' :
  filename = sys.argv[1]
  sum = len(words)
  count = { }
  tf = { }

  for w in words :
    if count.has_key(w) :
      count[w] = count[w] + 1
    else :
      count[w] = 1

  print '>>>>>>>>>>>>>>>>>>'
  print 'There are %d words' % sum
  for w, c in count.items() :
    print '  %s : %d' % (w, c)

  for w, c in count.items() :
    tf[w] = c * 1.0 / sum

  print '>>>>>>>>>>>>>>>>>>'
  print 'The tf info are'
  for w, f in tf.items() :
    print '  %s : %lf' % (w, f)

  tfidf = calcTfIdf(tf)

  print '>>>>>>>>>>>>>>>>>>'
  print 'The tf*idf info are'
  for w, f in tfidf.items() :
    print '  %s : %lf' % (w, f)

