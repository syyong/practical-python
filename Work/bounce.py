# bounce.py
#
# Exercise 1.5
height = 100
bounce_back = 3/5
for i in range(10):
    height = height * bounce_back
    print(round(height, 4))

