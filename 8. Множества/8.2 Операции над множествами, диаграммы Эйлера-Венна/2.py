n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))

o_1 = n + m - x - t
o_2 = n + k - z - t
o_3 = m + k - t - y

q_1 = n - o_1 - o_2 - t
q_2 = m - o_1 - o_3 - t
q_3 = k - o_2 - o_3 - t

r_1 = q_1 + q_2 + q_3
r_2 = o_1 + o_2 + o_3
r_3 = a - r_1 - r_2 - t

print(r_1, r_2, r_3, sep="\n")
