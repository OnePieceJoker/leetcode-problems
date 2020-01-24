# 914 X of a Kind in a Deck of Cards

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

- Each group has exactly X cards.
- All the cards in each group have the same integer.

 

## Example 1:

> Input: [1,2,3,4,4,3,2,1]<br>
> Output: true<br>
> Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

## Example 2:

> Input: [1,1,1,2,2,2,3,3]<br>
> Output: false<br>
> Explanation: No possible partition.

## Example 3:

> Input: [1]<br>
> Output: false<br>
> Explanation: No possible partition.

## Example 4:

> Input: [1,1]<br>
> Output: true<br>
> Explanation: Possible partition [1,1]

## Example 5:

> Input: [1,1,2,2,2,2]<br>
> Output: true<br>
> Explanation: Possible partition [1,1],[2,2],[2,2]

## Solution
```python3
import collections
from typing import List
from fractions import gcd
from functools import reduce
# def hasGroupsSizeX(deck: List[int]) -> bool:
#     N = len(deck)
#     # if N is odd
#     if (N < 2):
#         return False
#     count = collections.Counter(deck)
#     for X in range(2, N+1):
#         if N % X == 0:
#             if all(v%X == 0 for v in count.values()):
#                 return True
#     return False

# other Solution
def hasGroupsSizeX(deck: List[int]) -> bool:
    N = len(deck)
    if N < 2:
        return False
    vals = collections.Counter(deck).values()
    # gcd(): Compute the greatest common divisor
    return reduce(gcd, vals) >= 2

if __name__ == '__main__':
    deck: List[int] = [1,1,1,2,2,2]
    print(hasGroupsSizeX(deck))

```
