#!/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import datetime
import segmenter
from trie import Trie

'''
This program works in python 2.7.

usage: python __init__.py dictionary_path text_input_path
output RESULT{time}

I use maximum matching.
'''

if len(sys.argv) == 3:
    d = datetime.datetime.today()
    with codecs.open(sys.argv[1], 'r', 'utf-8') as dic_file,\
        codecs.open(sys.argv[2], 'r', 'utf-8') as text_input,\
        codecs.open('RESULT_' + str(d), 'w', 'utf-8') as result:
        dic_list = [dic_ele.rstrip() for dic_ele in dic_file.readlines()]
        trie = Trie()
        trie.setitems(dic_list)
        input_list = text_input.readlines()
        dicmaxlen = max(map(len, dic_list))
        print 'maxlen', dicmaxlen
        cnt = 0
        for sentence in input_list:
            cnt = cnt + 1
            if cnt % 100 == 0:
                print 'cnt:', cnt
            token_list = []
            segmenter.max_matching(sentence, trie, token_list, dicmaxlen)
#             max_matching method also works dic_list instead of trie, but too heavy
#             segmenter.max_matching(sentence, dic_list, token_list, dicmaxlen)
#             print(u' '.join(token_list))
            result.write(' '.join(token_list))
else:
    print 'Please input correct arguments.'
    print 'usage: python __init__.py dictionary_path text_input_path'
