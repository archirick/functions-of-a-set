##isdisjoint function

x={"apple","banana","cherry"}
y={"google","microsoft","facebook"}
z=x.isdisjoint(y)
print(z)
print("\n")

##subset function

q={"a","b","c"}
v={"f","e","d","c","b","a"}
z=q.issubset(v)
print(z)
print("\n")

##Superset function

y={"a","b","c"}
x={"f","e","d","c","b","a"}
z=x.issuperset(y)
print(z)
print("\n")

##Intersection_update function

x={"apple","banana","cherry"}
y={"google","microsoft","facebook"}
z=x.intersection_update(y)
print(z)
print("\n")

##symmetric_difference function

x={"Apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.symmetric_difference(y)
print(z)
print("\n")

##union function

x={"apple","banana","cherry"}
y={"google","microsoft","facebook"}
z=x.union(y)
print(z)
print("\n")

##update function

x={"apple","banana","cherry"}
y={"google","microsoft","facebook"}
z=x.update(y)
print(z)
print("\n")
