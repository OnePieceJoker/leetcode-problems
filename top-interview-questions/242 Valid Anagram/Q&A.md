# 242. Valid Anagram

## Overview

Given two strings *s* and *t*, write a function to determine if *t* is an anagram of *s*.

### Example

```text
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
```

## Solution

### Approach#1 字符排序

如果两个字符串是存在anagram关系的话，那么两个字符串的长度以及在排序后的单词字符数组应该是相同的。

```Java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] str1 = s.toCharArray();
        char[] str2 = t.toCharArray();
        Arrays.sort(str1);
        Arrays.sort(str2);
        return Arrays.equals(str1, str2);
    }
}
```

### Approach#2 使用计数器

字符串s和t出现相同字符的次数应该是一样，因此可以通过引入计数器记录字符出现的次数来判断两者之间是否是anagram关系。

```Java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] counter = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counter[s.charAt(i) - 'a']++;
            counter[t.charAt(i) - 'a']--;
        }
        for (int count : counter) {
            if (count != 0) {
                return false;
            }
        }
        
        return true;
    }
}
```
