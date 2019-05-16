#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoqiang.pei on 2019/5/16

import logging
import sys
import json
import time
import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)d %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S'
)

import os
import re
import codecs


stop_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'stopwords.txt')

stop = set()
fr = codecs.open(stop_path, 'r', 'utf-8')
for word in fr:
    stop.add(word.strip())
fr.close()
re_zh = re.compile('([\u4E00-\u9FA5]+)')


def filter_stop(words):
    return list(filter(lambda x: x not in stop, words))


def get_sentences(doc):
    line_break = re.compile('[\r\n]')
    delimiter = re.compile('[，。？！；]')
    sentences = []
    for line in line_break.split(doc):
        line = line.strip()
        if not line:
            continue
        for sent in delimiter.split(line):
            sent = sent.strip()
            if not sent:
                continue
            sentences.append(sent)
    return sentences