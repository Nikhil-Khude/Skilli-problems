def insertposition(arr:list[int],n,p):
    for i in range(len(arr)-1,p,-1):
        arr[i]=arr[i-1]
    arr[p]=n
    return arr
print(insertposition([10,20,30,40,50],99,2))