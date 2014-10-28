def heapsort(iterable):
    'Equivalent to sorted(iterable)'
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]
