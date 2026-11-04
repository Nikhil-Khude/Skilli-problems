def sumar(a:int,d:int,n:int):
    total=0
    for i in range(n):
        total+=a
        a+=d
    return total
print(sumar(1,3,5))