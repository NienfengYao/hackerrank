# Python/Sets 

* Ref:
  * [Set Types in Built-in Types](https://docs.python.org/3.6/library/stdtypes.html#set)

* Operation:
  * Return a new set:
    * isdisjoint(other)
    * issubset(other), set <= other
    * set < other  # proper subset
    * issuperset(other), set >= other
    * set > other  # proper superset
    * union(*others), set | other | ...
    * intersection(*others), set & other & ...
    * difference(*others), set - other - ...
    * symmetric_difference(other), set ^ other
    * copy()
  * Update the set itself
    * update(*others), set |= other | ...
    * intersection_update(*others), set &= other & ...
    * difference_update(*others), set -= other | ...
    * symmetric_difference_update(other), set ^= other
    * add(elem)
    * remove(elem)
    * discard(elem)
    * pop()
    * clear()
