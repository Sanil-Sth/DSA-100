"""
Day 01 - Two Sum
Difficulty: Easy
Topic: Arrays & Hashing
Pattern: Hash Map / Complement Lookup

Problem:
    Given an integer array nums and a target, return indices of two numbers
    that add up to target. Exactly one solution exists.

Approach:
    Single-pass hash map. For each element, check if its complement
    (target - num) has already been seen. Store value->index as we go.

Time:  O(n)
Space: O(n)

LeetCode: https://leetcode.com/problems/two-sum/
"""

def two_sum(nums, target):
    seen = {}  # maps value -> index for every number we've visited so far

    for i, num in enumerate(nums):
        complement = target - num  # if num=8 and target=10, we need 2

        if complement in seen:
            # found the pair — return both indices as a LIST (not a set)
            return [seen[complement], i]

        # pair not found yet — store this number so future iterations can find it
        seen[num] = i

nums   = [3, 2, 8, 6, 4, 9, 1, 2, 7]
target = 10

result = two_sum(nums, target)
i, j   = result

print(f"Indices : {result}")                                           # [1, 2]
print(f"Check   : nums[{i}] + nums[{j}] = {nums[i]} + {nums[j]} = {nums[i] + nums[j]}")  # 8 + 2 = 10