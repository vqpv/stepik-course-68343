def sum_ip(ip):
    ips = list(map(int, ip.split('.')))
    return (ips[0] * 256 ** 3) + (ips[1] * 256 ** 2) + (ips[2] * 256 ** 1) + (ips[3] * 256 ** 0)

print(*sorted([input() for _ in range(int(input()))], key=lambda x: sum_ip(x)), sep="\n")
