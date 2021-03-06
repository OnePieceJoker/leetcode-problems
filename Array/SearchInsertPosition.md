## 35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

### Example 1:

Input: [1,3,5,6], 5
Output: 2

### Example 2:

Input: [1,3,5,6], 2
Output: 1

### Example 3:

Input: [1,3,5,6], 7
Output: 4

### Example 4:

Input: [1,3,5,6], 0
Output: 0

### Solution

#### Java

```Java
class Solution {
    public int searchInsert(List[int] nums, int target) {
        int i = 0;
        for (; i < nums.length; i++) {
            if (target > nums[i]) {
                continue;
            } else {
                break;
            }
        }
        return i;
    }
}
```

#### Python3

```python3
class Solution:
    def searchInsert(nums: List[int], target: int) -> int:
        i = 0
        for i in range(len(nums)):
            if nums[i] < target:
                i += 1
                continue
            else:
                break
        return i
```
