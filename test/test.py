r = ['M', 'L']

p1 = r[0]
plast = r[-1]
r.pop()
print(r)
r.append(p1)
r[0] = plast
print(r)

