s = input("what is your string?\n>")
s = s + ' '
current_string = ""
longest_string = ""

for x in range(len(s) - 1):
  t = 0
  while s[x + t] <= s[x + 1 + t]:

    if x + 1 + t >= len(s) - 1:
      break
    t = t + 1
    current_string = (s[x:x + t + 1])

    if len(current_string) > len(longest_string):
      longest_string = current_string
print("Your longest string is:", longest_string)
