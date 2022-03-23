# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.

def sumofnumbers(n1,n2,n3):
    if n1==n2==n3:
        return (n1+n2+n3)*3
    else:
        return n1 + n2 + n3

print(sumofnumbers(2,3,3))