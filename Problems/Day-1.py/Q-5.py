def factno(n):
    count=1
    for i in range(1,n+1):
        count*=i
    return len(str(count))
n=5
print(factno(5))
