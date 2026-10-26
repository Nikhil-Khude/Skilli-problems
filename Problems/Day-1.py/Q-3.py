def anagram(n1: int, n2: int) -> bool:
    # Write your solution here
    return sorted(str(abs(n1)))==sorted(str(abs(n2)))