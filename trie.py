#!/bin/env python
# -*- coding: utf-8 -*-


class Trie(object):

    def __init__(self):
        self.path = {}
        self.value = None
        self.value_valid = False
        self.debug = True

    def dprint(self, *strlist):
        if self.debug:
            for s in strlist:
                if type(s) != list:
                    print s,
                else:
                    print '[',
                    for e in s:
                        print e, ',',
                    print ']',
            print

    def __setitem__(self, key, value):
        '''
        trie["test"] = true
        '''
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            node = Trie()
            self.path[head] = node

        if len(key) > 1:
            remains = key[1:]
            node.__setitem__(remains, value)
        else:
            node.value = value
            node.value_valid = True

    def __getitem__(self, key):
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            raise KeyError(key)
        if len(key) > 1:
            remains = key[1:]
            try:
                return node.__getitem__(remains)
            except KeyError:
                raise KeyError(key)
        elif node.value_valid:
            return node.value
        else:
            raise KeyError(key)

    def __contains__(self, key):
        try:
            self.__getitem__(key)
        except KeyError:
            return False
        return True

    def keys(self, prefix=[]):
        return self.__keys__(prefix)

    def __keys__(self, prefix=None, seen=None):
        if prefix is None:
            prefix = []
        if seen is None:
            seen = []
        result = []
        if self.value_valid:
            isStr = True
            val = u""
            for k in seen:
                if type(k) != unicode or len(k) > 2:
                    isStr = False
                    break
                else:
                    val += k
            if isStr:
                result.append(val)
            else:
                result.append(prefix)
        if len(prefix) > 0:
            head = prefix[0]
            prefix = prefix[1:]
            if head in self.path:
                nextpaths = [head]
            else:
                nextpaths = []
        else:
            nextpaths = self.path.keys()
        for k in nextpaths:
            nextseen = []
            nextseen.extend(seen)
            nextseen.append(k)
            result.extend(self.path[k].__keys__(prefix, nextseen))
        return result

    def __len__(self):
        n = 1 if self.value_valid else 0
        for k in self.path.keys():
            n = n + len(self.path[k])
        return n

    def setitems(self, itemlist):
        for item in itemlist:
            self.__setitem__(item, True)
