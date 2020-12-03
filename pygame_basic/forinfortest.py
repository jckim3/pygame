weapons=[]
weapons.append([0,1])
print(weapons)
weapons.append([1,3])
print(weapons)
weapons.append([2,9])
print(weapons)

# i = [ i for i in weapons ]
test = [ [w[1],w[0]] for w in weapons if w[1] == 1  ]
print(test)