#! -*- coding: utf8 -*-

class SetAnalizer(object):
    def __init__(self, data_set, relations_set):
        """data_set is a set of objects, relations_set is a set of two element tuples"""
        self.data_set = data_set
        self.relations_set = relations_set
        self.cache = {}
    def isReflexive(self):
        """Returns True if relation is Reflexive, in relations_set exists (a, b) tuple and (b, a) tuple, foreach relation in relations"""
        if not self.cache['isReflexive']:
            self.cache['isReflexive'] = True
            for relation in self.relations_set:
                if not (relation[1], relation[0]) in self.relations_set:
                    self.cache['isReflexive'] = False
                    break
            
        return self.cache['isReflexive']
    def isSimetric(self):
        pass
    def isAntiSimetric(self):
        pass
    def isTransitive(self):
        pass

if __name__ == '__main__':
    a = set(['a', 'b', 'c'])
    b = set([('a', 'b'),('b', 'a')])
    c = SetAnalizer(a, b)
    print c.isReflexive()
    print c.isReflexive()
