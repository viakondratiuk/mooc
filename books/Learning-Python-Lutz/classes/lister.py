class ListInstance:
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (self.__class__.__name__, id(self), self.__attrnames())
    def __attrnames(self):
        res = ''
        for attr in sorted(self.__dict__):
            res += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return res