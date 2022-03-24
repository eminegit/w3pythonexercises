#Write a Python program to count the number 4 in a given list.

def count (nums):
    count = 0

    for i in nums:
        if i == 4:
            count = count +1
    return count

print(count([1,3,5,4,6,4,9,4,8,4]))