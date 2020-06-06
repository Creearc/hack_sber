import io
import pickle
f = io.open("selo.txt", encoding='utf-8')
ss =''

def move(arr, i, j):
  elem = arr[i]
  arr[i] = arr[j]
  arr[j] = elem
  return arr
  

names = {}

for s in f:
  s = s.partition(' ')
  s = s[2].partition(' ')
  if len(s) > 0:
    arr = names.get(s[0])
    if arr is None:
      arr = set()
    arr.add(s[2][:-1].lower())
    names[s[0]] = arr
      
categories = []
names_of = []
ends = {}

for elem in names:
  categories.append(elem)
  names_of.append(names.get(elem))
  for j in names.get(elem):
    arr = ends.get(elem)
    if arr is None:
      arr = set()
    arr.add(j[-3:])
    ends[elem] = arr

print(ends["г."])
print()
print(ends["п."])
print()
print(ends["г."] & ends["п."])

categories.pop(1)
names_of.pop(1)

categories = move(categories, 0, 4)
names_of = move(names_of, 0, 4)

#print(categories)
#print(names_of)

arr = [categories, names_of]

"""
with open('arr.dat', "wb") as f:
  pickle.dump(arr, f)

"""
