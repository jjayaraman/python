# data = [ x*2 for x in range(0,10,1)]
# print(data)

# data = [x*2 for x in range(0,10,1) if x < 5 ]
# print(data)


# rows,cols = 4,4
# two_d = [[ '£' for x in range(rows)]  for y in range(cols) ]
# print(two_d)


# a,b,c=3,3,3
# three_d = [[[z for x in range(a)] for y in range(b)] for z in range(c)]
# print(three_d)

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
x,y,z,n=2,2,2,2
data = [ [a,b,c] for a in range(x) for b in range(y) for c in range(z) if a+b+c != n]
print(data)
