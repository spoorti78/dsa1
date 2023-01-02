#program to check if two strings are a rotation of each other

def rotation(s1,s2):
  if len(s1) == len(s2):
    temp = s1 + s2
    if temp.count(s2)>0:
      return 1
  else:
    return 0
s1 = input("Enter the string1 =")
s2 = input("Enter the string2 =")
if rotation(s1,s2):
  print("Yes, rotation of each other --> ",s1,"==",s2)
else:
  print("No, enter another strings")
