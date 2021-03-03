# 283. Move Zeros

## Overriew

Given an array **nums**, write a function to move all **0**'s to then end of it while maintaining the relative order of the non-zero elements.

### Example

```text
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

## Solution

### Approach#1 指针记录

使用一个指针j来记录数组中最靠前的0的位置，如果下一个非零数字的位置是在j之后，则将该非零数字放到当前j的位置，指针j后移一步。

```Java
class Solution {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length < 1) return;
        
        for (int i = 0, firstZeroFoundAt = nums.length; i < nums.length; i++) {
            if (nums[i] == 0 && i < firstZeroFoundAt) {
                firstZeroFoundAt = i;
                continue;
            }
            if (nums[i] != 0 && i > firstZeroFoundAt) {
                nums[firstZeroFoundAt++] = nums[i];
                nums[i] = 0;
            }
        }
    }
}
```

### Approach#2 非零位置记录

循环数组，将该数组中的非零数字往前移动，用一个指针lastNonZeroFoundAt来记录当前数组非零数字的位置，然后再在lastNonZeroFoundAt位置开始，往数组后续位置填0

```Java
class Solution {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length < 1) return;
        int lastNonZeroFoundAt = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[lastNonZeroFoundAt++] = nums[i];
            }
        }
        for (int i = lastNonZeroFoundAt; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}
```
