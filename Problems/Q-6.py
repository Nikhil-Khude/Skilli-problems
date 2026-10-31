def sums(n):
    count=0
    for i in range(1,n+1):
        count+= i**2
    return count
print(sums(6))