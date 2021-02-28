# 169. Majority Element

## Overview

Given an array **nums** of size **n**, return the majority element.

The majority element is the element that appears more than n / 2 times. You may assume that the majority element always exists in the array.

### Example

```text
Input: nums = [3,2,3]
Output: 3
```

```text
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Solution

### Approach#1 简单粗暴的循环

```Java
class Solution {
    public int majorityElement(int[] nums) {
        int majorityCount = nums.length / 2;
        for (int num : nums) {
            int count = 0;
            for (int elem : nums) {
                if (num == elem) {
                    count += 1;
                }
            }
            
            if (count > majorityCount) {
                return num;
            }
        }
        
        return -1;
    }
}
```

### Approach#2 使用HashMap

使用HashMap来统计数组中数字重复出现的次数，然后比较次数，返回出现次数最多的key.

```Java
class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> counts = countNums(nums);
        // 使用jdk8 Stream
        // return counts.entrySet().stream()
        //                         .map(Map.Entry<Integer, Integer>::getKey)
        //                         .max(Comparator.comparing(counts::get)).get();

        // 使用for循环
        Map.Entry<Integer, Integer> majorityEntry = null;
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            if (majorityEntry == null || entry.getValue() > majorityEntry.getValue()) {
                majorityEntry = entry;
            }
        }
        return majorityEntry.getKey();
    }
    
    public Map<Integer, Integer> countNums(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<Integer, Integer>();
        for (int num : nums) {
            if (!counts.containsKey(num)) {
                counts.put(num, 1);
            } else {
                counts.put(num, counts.get(num) + 1);
            }
        }
        return counts;
    }
}
```

### Approcah#3 Sort

如果一个数组是有序的，那么该数组中出现次数大于|N/2|的值应该是在该有序数组的中间位置

```Java
class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }
}
```

### Approach#4 Boyer-Moore Voting Algorithm

这个算法的大致思路为：设置一个计数器**count**记录指定数字**majorityNum**出现的次数，遍历过程中，如果当前数字==**majorityNum**，则**count**+1，否则**count**-1，如果**count**==0，则将当前数字设置为**majorityNum**，遍历结束后，**majorityNum**则是该数组最多的数字

```Java
class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        int candidate = Integer.MIN_VALUE;
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }
        return candidate;
    }
}
```
