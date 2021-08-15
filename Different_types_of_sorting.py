# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 22:31:11 2021

@author: Lenovo
"""
import numpy as np
import random
import time
import copy

# ------------------------ select sort ----------------------------------------
def select_sort(nums):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


# ------------------------ bubble sort ----------------------------------------
def bubble_sort(nums):
    for i in range(len(nums)-1):
        max_index = i
        for j in range(i, len(nums)):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]


# ------------------------ insert sort ----------------------------------------
def insert_sort(nums):
    for i in range(1, len(nums)):
        j = i-1
        key = nums[i]
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key


# ------------------------ shell sort -----------------------------------------
def shell_sort(nums):
    step = int(len(nums)/2)
    while step > 0:
        for i in range(step, len(nums)):
            # insert nums[i] to sorted one
            key = nums[i]
            j = i
            while j >= step and nums[j-step] > key:
                nums[j] = nums[j-step]
                j -= step
            nums[j] = key
        step = int(step/2)


# ------------------------ merge sort -----------------------------------------
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[0:mid])
    right = merge_sort(nums[mid::])
    sorted_nums = merge_two_list(left, right)
    return sorted_nums


def merge_two_list(nums1, nums2):
    if nums1 == [] or nums2 == []:
        return nums1 + nums2
    else:
        res = []
        i = 0
        j = 0
        while True:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
                if i >= len(nums1):
                    res.extend(nums2[j::])
                    break
            else:
                res.append(nums2[j])
                j += 1
                if j >= len(nums2):
                    res.extend(nums1[i::])
                    break
    return res


# ------------------------ qucik sort -----------------------------------------
def quick_sort(start, end, nums):
    if end-start < 1:
        return
    pos = partition(start, end, nums)
    quick_sort(start, pos, nums)
    quick_sort(pos+1, end, nums)


def partition(start, end, nums):
    pivot = nums[start]
    pos = start
    i = pos+1
    while True:
        if i > end:
            break
        if nums[i] < pivot:
            value = nums[i]
            pos += 1
            nums.pop(i)
            nums.insert(start, value)
        i += 1
    return pos


def quick_sort1(nums):
    if len(nums) <= 1:
        return nums
    pos, nums = partition1(nums)
    left = quick_sort1(nums[0:pos])
    right = quick_sort1(nums[pos+1::])
    nums = left + [nums[pos]] + right
    return nums


def partition1(nums):
    pivot = nums[0]
    pos = 0
    new_nums = [pivot]
    for i in range(1, len(nums)):
        if nums[i] < pivot:
            pos += 1
            new_nums.insert(0, nums[i])
        else:
            new_nums.append(nums[i])
    return pos, new_nums


# ------------------------ heap sort ------------------------------------------
def heapify(tree, n, i):
    if i >= n:
        return
    c1 = 2*i+1
    c2 = 2*i+2
    max_index = i
    if c1 < n and tree[c1] > tree[i]:
        max_index = c1
    if c2 < n and tree[c2] > tree[max_index]:
        max_index = c2
    if max_index != i:
        tree[max_index], tree[i] = tree[i], tree[max_index]
        heapify(tree, n, max_index)


def build_heap(tree, n):
    last_node = n-1
    last_parent = (last_node-1)//2
    for i in range(last_parent, -1, -1):
        heapify(tree, n, i)


def heap_sort(nums):
    end = len(nums)
    build_heap(nums, end)
    i = end-1
    while True:
        if i < 0:
            break
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
        i -= 1

t1 = time.time()
for i in range(100):
    nums = list(np.random.randint(100, size=random.randint(0, 10)))
    nums1 = copy.deepcopy(nums)
    heap_sort(nums)
    nums1 = sorted(nums1)
    print(nums1 == nums)
    if not nums1 == nums:
        print('FFFFFFalse')
        print(nums)
        break



t2 = time.time()
# print(t2-t1)
# import random

#     temp = sorted(temp)
#     print(res == temp)
