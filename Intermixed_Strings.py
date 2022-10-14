# This program takes two strings as user input, and
# the strings are printed in an intermixed form.

s = input()
s2 = input()
minn = min(len(s), len(s2))
for i in range(minn):
  print(s[0], s2[0], sep = '', end = '')
  s = s[1:]
  s2 = s2[1:]
print(s, s2, sep = '')
