# 19) Arasu Series

def arasu_series(n):
    series = []
    for i in range(1, n + 1):
        series.append(i**2 + 1)
    print(*series)

arasu_series(4)