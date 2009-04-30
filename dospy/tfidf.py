#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: cswenye@gmail.com                                
#

import os
import sys
from math import log

class idf :
  idf = { }

  def __init__(self, dic_name) :
    # from the dic file generate words info
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

  def __getitem__(self, key) :
    if self.idf.has_key(key) :
      return self.idf[key]
    else :
      return 0

  def __len__(self) :
    return len(words)

def calcTf(words) :
  sum = len(words)
  count = { }
  tf = { }

  for w in words :
    if count.has_key(w) :
      count[w] = count[w] + 1
    else :
      count[w] = 1
  
  for w, c in count.items() :
    tf[w] = c * 1.0 / sum
  
  return tf

def calcTfIdf(tf_list) :
  sogou_dic = "/home/cswenye/snoopy/data/sogou_utf8.dic"
  idf_list = idf(sogou_dic)
  tfidf = []
  for w, tf in tf_list.items() :
    wp = (w, tf * idf_list[w])
    tfidf.append(wp)

  tfidf.sort(mycmp)
  return tfidf

def mycmp(x, y) :
  if x[1] > y[1] :
    return -1
  elif x[1] < y[1] :
    return 1
  else :
    return 0

if __name__ == '__main__' :
  words = sys.argv[1:]
  tf = calcTf(words)
  tfidf = calcTfIdf(tf)

  print '>>>>>>>>>>>>>>>>>>'
  print 'The tf*idf info are'
  for wp in tfidf :
    print '  %s : %lf' % (wp[0], wp[1])

