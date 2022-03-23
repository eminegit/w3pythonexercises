
# Write a Python program to test whether a number is within 100 of 1000 or 2000
def within(n):
    if 1000-n <=100 or 2000-n <=100:
        print("the number is within 100 of 1000 or 2000")
    else:
        print("the number is not within 100 of 1000 or 2000")

within(923)
