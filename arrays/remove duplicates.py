def replicate(old, new):
    new.append(old[0])
    for i in range(0, len(old)):
        if old[i] != new[-1]:
            new.append(old[i])
            
    print(new)
    return len(new)

old = [1,1,2]
new = []
print(replicate(old,new))

