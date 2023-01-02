#

size = int(input("Enter the size = "))
arr = []
for i in range(size):
  elements = int(input("Enter elements = "))
  arr.append(elements)
print(arr)
arr = arr[::-1]
print("Reversed array = ", arr)