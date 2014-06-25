#!/bin/env python
# -*- coding: utf-8 -*-


def max_matching(sentence, dic_list, token_list, dicmaxlen):
    def lookup(dic_list, c, i, n):
        ret = -1
        for s in range(i+1, n):
            sub = c[i:s]
#            print sub
#            print sub, sub in dic_list
            if sub in dic_list:
                ret = len(sub)
#                print 'hit', ret
        return ret

    i = 0
    n = len(sentence)
    while i < n:
        j = lookup(dic_list, sentence, i, i + dicmaxlen)
        if j == -1:
#            print sentence[i],
            token_list.append(sentence[i])
            i += 1
        else:
#            print sentence[i:i+j],
            token_list.append(sentence[i:i+j])
            i += j


def print_unilist(uni_list):
    for ele in uni_list:
        print ele,
