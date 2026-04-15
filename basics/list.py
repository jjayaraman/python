days = [0,1,2,3,4,5,6]

# print(days)
# print(days[0])
# print(days[6])

days.append(7)
# print(days)


rows=3
cols=3
outer = []
inner= []
for r in range(0,rows,1):
  for c in range(0,cols,1):
    inner.append([r,c])
  # outer.append(inner)

print(inner)