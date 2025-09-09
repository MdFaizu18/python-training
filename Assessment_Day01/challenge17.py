# 17) Garage Waiting Time

def garage_waiting_time(n, x):
    service_time = n * 10
    last_arrival = (n - 1) * x
    wait = max(0, service_time - last_arrival)
    print(wait)

garage_waiting_time(4, 5)