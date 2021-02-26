# 412. Fizz Buzz

## Overview

Write a programe that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output "Fizz" instead of the number and for the multiples of five output "Buzz". For numbers which are multiples of both three and five output "FizzBuzz".

### Example

```text
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```

## Solution

### Approach: 取余

对数字进行取余操作，对满足要求的数据进行相应的逻辑处理。后面在Discuss中看到一种新的思路，通过定义两个变量来表示3或5的倍数，无需进行取余操作，进行数字大小比较操作即可

```java
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> result = new ArrayList<>(n);
        if (n < 1) return result;
        // 取余操作
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                result.add("FizzBuzz");
            } else if (i % 3 == 0) {
                result.add("Fizz");
            } else if (i % 5 == 0) {
                result.add("Buzz");
            } else {
                result.add(Integer.toString(i));
            }
        }
        return result;
    }
}
```

```java
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> result = new ArrayList<>(n);
        if (n < 1) return result;
        String Fizz = "Fizz";
        String Buzz = "Buzz";
        String FizzBuzz = "FizzBuzz";
        // 新增两个变量来表示3或5的倍数
        for (int i = 1, fizz = 3, buzz = 5; i <= n; i++) {
            if (i == fizz && i == buzz) {
                result.add("FizzBuzz");
                fizz += 3;
                buzz += 5;
            } else if (i == fizz) {
                result.add(Fizz);
                fizz += 3;
            } else if (i == buzz) {
                result.add(Buzz);
                buzz += 5;
            } else {
                result.add(Integer.toString(i));
            }
        }
        return result;
    }
}
```
