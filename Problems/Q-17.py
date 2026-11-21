def zeroafterno(arr:list):
    k=len(arr)
    for i in range((k-1)//2,-1,-1):
        arr[2*i]=arr[i]

        if 2*i+1<k:
            arr[2*i+1]=0
    return arr
arr=[int(x)for x in input("enter a list:-").split()]
print(zeroafterno(arr))