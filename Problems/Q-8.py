def table(n:int,limit:int):
    count=[]
    for i in range(1,limit+1):
        count.append(n*i)
    return count
print(table(3,5))