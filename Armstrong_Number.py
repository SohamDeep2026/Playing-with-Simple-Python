# This program checks if the integer inputted by
# the user is an Armstrong Number or not.

num = input()
sum = 0
length = len(num)
for i in num: sum += int(i) ** length
if sum == int(num): print('Yes')
else: print('No')
