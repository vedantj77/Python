Dict1 ={"a":3,"b":4,"c":5}
Dict2 ={"a":2,"b":4,"c":6}

for i in Dict1.items():
    for j in Dict2.items():
        if i==j:
            print(i)