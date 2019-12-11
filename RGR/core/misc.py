def split_iter(letters: list, n: int):
    local_copy = letters.copy()
    length = (len(letters) // n) * n
    for i in range(n):
        yield [local_copy[j + i] for j in range(0, length, n)]
