from builtins import property as _property,tuple as _tuple

from operator import itemgetter as _itemgetter

from collections import OrderedDict

import collections

class NamedTuple(tuple):
    'NamedTuple(x, y)'

    __slots__ = ()

    _fields = ('x','y')

    def __new__(_cls,x,y):

        'Create new instance of NamedTuple(x, y)'

        return _tuple.__new__(_cls,(x,y))

    @classmethod
    def _make(cls,iterable,new=tuple.__new__,len=len):

        'Make a new Point object from a sequence or iterable'

        result = new(cls,iterable)

        if len(result) != 2:
            raise TypeError('Expected 2 arguments, got %d' % len(result))

        return result

    def _replace(_self,**kwds):

        'Return a new NamedTuple object replacing specified fields with new values'

        result = _self._make(map(kwds.pop,('x','y'),_self))

        if kwds:
            raise ValueError('Got unexpected field names: %r' % list(kwds))

        return result

    def __repr__(self):

        'Return a nicely formatted representation string'

        return self.__class__.__name__ + '(x=%r, y=%r)' % self

    @property
    def __dict__(self):

        'A new OrderedDict mapping field names to their values'

        return OrderedDict(zip(self._fields,self))

    def _asdict(self):

        'Return a new OrderedDict which maps field names to their values.'

        return self.__dict__

    def __getnewargs__(self):

        'Return self as a plain tuple.  Used by copy and pickle.'

        return tuple(self)

    def __getstate__(self):

        'Exclude the OrderedDict from pickling'


        return None

    x = _property(_itemgetter(0),doc='Alias for field number 0')

    y = _property(_itemgetter(1),doc='Alias for field number 1')

p = collections.OrderedDict()
files = ['x','y']
values = [1,2]
# update
p.update(zip(files,values))
# print(p.pop('y'))
x = p.pop('x')
y = p.pop('y')
nt = NamedTuple(x,y)

# unittest

# print(nt[0])
# print(nt[1])
# print(nt.x)
# print(nt.y)
# print(repr(nt))
