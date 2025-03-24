# give tuple function in python
t=(1,2,3,4,5)
print(t)


# 1.      Write a Python program to unpack a tuple into several variables.
t=(1,2,3,4,5)
a,b,c,d,e=t
print(a,b,c,d,e)

# 2.       Write a  Python program to convert a tuple to a string.
t=('a','b','c','d','e')
s=''.join(t)
print(s)

# 3. Write a Python program to check whether an element exists within a tuple.
t=(1,2,3,4,5)
print(3 in t)
