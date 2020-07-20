# 从排序数组中删除重复项

给定一个已排序的数组num，就地删除重复项，以使每个元素仅出现一次并返回新的长度。

不要为另一个数组分配额外的空间，必须通过使用O（1）额外的内存就地修改输入数组来做到这一点。

## 示例1

```text
给定一个数组：nums = [1,1,2],

函数应返回长度结果为2，nums数组的前两个元素分别为1，2.

剩下的长度与返回的长度无关.
```

## 示例2

```text
给定一个数组：nums = [0,0,1,1,1,2,2,3,3,4],

函数应返回长度结果为5，nums数组的前5个元素分别为0，1，2，3，4.

剩下的长度与返回的长度无关.
```

## 说明

困惑为什么返回的值是整数但您的答案是数组？

请注意，输入数组是通过引用传递的，这意味着调用者也将知道对输入数组的修改。

```text
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

## 解决思路

### 思路1

使用双指针，一个指针A记录当前数组的位移，另一个指针B用来记录数组中的唯一性值，当指针A所指向的值与指针B所指向的值不同时，移动指针B，并将指针A的值赋值到移动后的指针B所指向的位置

## 解决方案

```Java
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[i] != nums[j]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
}
```

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1
```
