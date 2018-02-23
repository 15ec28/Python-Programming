def reverse(s):
  r = ""
  for i in s:
    r = i + r
  return r
s = raw_input()
print (reverse(s))
