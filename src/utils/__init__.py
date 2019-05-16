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