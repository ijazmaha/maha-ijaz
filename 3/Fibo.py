def Index(n):
    n1 = 0
    n2 = 1
    count = 0
    nth = 0
    
    while count < n:
        if count == 0:
            nth = 0
            count += 1
            continue
        else:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    
    return nth

result = Index(20)
print(result)