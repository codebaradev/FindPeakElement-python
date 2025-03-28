# Find Peak Element

Pseudocode 
```pseudocode
Algorithm FindPeakElement(arr)
    left ← 0
    right ← length of arr - 1
    
    while left <= right then
        mid ← left + ((right - left) // 2)
        
        if mid > 0 and arr[mid] < arr[mid - 1] then
            right ← mid - 1
        else if mid < length of arr - 1 and arr[mid] < arr[mid + 1] then
            left ← mid + 1
        else
            return arr[mid]
``` 

Reference:
* [Find Peak Element - Leetcode 162 - Python](https://www.youtube.com/watch?v=kMzJy9es7Hc)