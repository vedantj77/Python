var = [1,2,2,1]
var2 = [2,3]

var = set(var)
var2 = set(var2)

newlist = list(var.intersection(var2))
print(newlist)