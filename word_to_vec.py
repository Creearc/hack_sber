import pickle

with open("arr.dat", 'rb') as f:
  arr = pickle.load(f)

def clean(s):
  s = s.lower()
  return s

def a(s):
  global arr
  s = clean(s)
  for i in range(len(arr[1])):
    #print(arr[1][i])
    if s in arr[1][i]:
      return i+1
  return 0

s = "Известковый"
i = a(s)
print(i, arr[0][i-1])


s = "Коломна"
i = a(s)
print(i, arr[0][i-1])


with open("vitya.dat", 'rb') as f:
  v = pickle.load(f)

out = []
for i in v:
  if a(i) == 0:
    out.append(i)


print(len(out))
print(out)
