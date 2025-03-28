import time
import random


# BF = Brute Force (Sequence)
def findPeakBF(arr):
    for current in range(len(arr)):
        if (current == 0 and arr[current] > arr[current + 1]):
            return arr[current]
        
        if (current == len(arr) - 1 and arr[current] > arr[current - 1]):
            return arr[current]

        if (current > 0 and arr[current] > arr[current + 1] and arr[current] > arr[current - 1]):
            return arr[current]

# DC = Divide and Conquer (Binary Search)
def findPeakDC(arr):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + ((right - left) // 2)
        
        if (mid > 0 and arr[mid] < arr[mid - 1]):
            right = mid - 1
        elif (mid < len(arr) - 1 and arr[mid] < arr[mid + 1]):
            left = mid + 1
        else:
            return arr[mid]

def main():
    arrs = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]

    # Brute Force
    print("Brute Force")
    for arr in arrs:
        start_time = time.perf_counter()
        peak = findPeakBF(arr) 
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Peak: {peak} -> {execution_time:.6f} seconds")
        
    # Divide and Conquer
    print("Divide and Conquer")
    for arr in arrs:
        start_time = time.perf_counter()
        peak = findPeakDC(arr) 
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Peak: {peak} -> {execution_time:.6f} seconds")

main()