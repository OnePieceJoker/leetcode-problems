# 167.Two Sum 2 - input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

## Note:

> Your returned answers (both index1 and index2) are not zero-based.<br>
> You may assume that each input would have exactly one solution and you may not use the same element twice.

## Example:

> Input: numbers = [2,7,11,15], target = 9<br>
> Output: [1,2]<br>
> Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

## Solution
```python3
from typing import List
# def twoSum(numbers: List[int], target: int) -> List[int]:
#     size = len(numbers)
#     my_map = {}
#     for i in range(size):
#         my_map[numbers[i]] = i
#     for i in range(size):
#         if target - numbers[i] in my_map:
#             return [i+1, my_map[target-numbers[i]]+1]
#     return []

# other Solution
def twoSum(numbers: List[int], target: int) -> List[int]:
    low: int = 0
    high: int = len(numbers)-1
    total: int = numbers[low] + numbers[high]
    if total == target:
        return [low+1, high+1]
    while(total != target):
        if total > target:
            high = high - 1
        elif total < target:
            low = low + 1
        total = numbers[low] + numbers[high]
    return [low+1, high+1]

if __name__ == '__main__':
    numbers = [2,7,11,15]
    print(twoSum(numbers, 9)
```
