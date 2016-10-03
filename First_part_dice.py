'''
Use "random" module to show the "law of large numbers" in Probability. But when 
I run my code, I found the possibility of the difference number is pretty large.
This code only show the test part. After that, I will upload more specific code
to show the work
'''


import random
L=["1","2","3","4","5","6"]     # This is the element in dice
i = 0
while i < 1000000:              # I choose 1000000 as my total trials
    a = random.choice(L)        # This module is import from file
    L.append(a)                 # Add element to L
    i +=1
"""
There is small fault in list L since L includes the original six elements. Next 
part, this kind of small fault will be fix.
"""
print("one:",L.count("1"))      
print("two:",L.count("2"))
print("three:",L.count("3"))
print("four:",L.count("4"))
print("five:",L.count("5"))
print("six:",L.count("6"))

"""
I conclude in that part that the "random" module should be refine.
""" 
