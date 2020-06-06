import io
import pickle
f = io.open("selo.txt", encoding='utf-8')
ss =''

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
for elem in names:
  categories.append(elem)
  names_of.append(names.get(elem))

#print(categories)
#print(names_of)

arr = [categories, names_of]

with open('arr.dat', "wb") as f:
  pickle.dump(arr, f)

