# Python/Itertools 

* Ref:
  * [ itertools — Functions creating iterators for efficient looping](https://docs.python.org/3.6/library/itertools.html#)

* Combinatoric iterators:
  * product(p, q, … [repeat=1])
    * cartesian product, equivalent to a nested for-loop
    * product('ABCD', repeat=2): AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
  * permutations(p[, r])
    * r-length tuples, all possible orderings, no repeated elements
    * permutations('ABCD', 2): AB AC AD BA BC BD CA CB CD DA DB DC
  * combinations(p, r)
    * r-length tuples, in sorted order, no repeated elements
    * combinations('ABCD', 2): AB AC AD BC BD CD
  * combinations_with_replacement(p, r)
    * r-length tuples, in sorted order, with repeated elements
    * combinations_with_replacement('ABCD', 2): AA AB AC AD BB BC BD CC CD DD
  * groupby(terable[, key]
    * sub-iterators grouped by value of key(v)
    * [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    * [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
