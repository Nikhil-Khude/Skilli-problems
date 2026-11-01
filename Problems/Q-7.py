def sumOfSeries(n: int, a: int, d: int) -> int:
    # Write your solution here
    total=0
    for i in range(n):
        total+=a
        a+=d
    return total
print(sumOfSeries(5, 2, 3))
    