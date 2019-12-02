## 27.Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

### Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.

### Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:
```java
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

### Solution

#### Java

```Java
class Solution1 {
    /**
     * Solution 1: 使用两个指针，一个指针用来遍历比对val，一个指针用来替换数组中的值。
     * 保证返回的长度里的数组值中不包含val。
     * space complexity: O(1)
     * time complexity: O(n)
     */
    public int removeElement(int[] nums, int val) {
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
}

class Solution2 {
    /**
     * 当要替换的元素较少时，上一种solution要做更多的复制操作。
     * 另一种解决方案就是将要替换的值用数组最后的值替换，并减少数组大小，减少过多的复制操作。
     * space complexity: O(1)
     * time complexity: O(n)
     */
    public int removeElement(int[] nums, int val) {
        int i = 0;
        int len = nums.length;
        while (i < len) {
            if (nums[i] == val) {
                nums[i] = nums[len - 1];
                len--;
            } else {
                i++;
            }
        }
        return len;
    }
}
```
#### python3

```python3
class Solution:
    def removeElement(sele, nums: List[int], val: int) -> int:
        int i = 0
        int length = len(nums)
        while i < length:
            if (nums[i] == val):
                nums[i] = nums[length-1]
                length = length - 1
            else:
                i = i + 1
        return length
```
