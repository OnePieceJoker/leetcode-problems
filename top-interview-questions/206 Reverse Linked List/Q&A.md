# 206. Reverse Linked List

## Overview

Given the **head** of a singly linked list, reverse the list, and return the reversed list.

### Example

```text
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

## Solution

### Approach#1 Iterative

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            // 保存下一个节点信息
            ListNode nextTemp = curr.next;
            // 当前节点的下一个节点指向上一个节点
            curr.next = prev;
            // 当前节点赋值给prev
            prev = curr;
            // 将下一个节点的信息赋值给当前节点，进入下次循环
            curr = nextTemp;
        }
        return prev;
    }
}
```

### Approach#2 Recursive

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode p = reverseList(head.next);
        // 递归到倒数第二个节点时: head.next.next == p
        head.next.next = head;
        head.next = null;
        return p;
    }
}
```

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        return reverse(head, null);
    }
    
    public ListNode reverse(ListNode head, ListNode newHead) {
        if (head == null) {
            return newHead;
        }
        ListNode next = head.next;
        head.next = newHead;
        return reverse(next, head);
    }
}
```
