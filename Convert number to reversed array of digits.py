def digitize(n):
    if n == 0:
        return [0]
    res = []
    while n > 0:
        res.append(n % 10)
        n //= 10
    return res
