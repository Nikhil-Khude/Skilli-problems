def roundoff(n):
    num=int(n)
    result=((num+4)//10)*10
    return result
print(roundoff(15))