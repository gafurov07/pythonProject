from collections import Counter

# 1.1
# s = input()
# d = {}
# t = set(s)
# for i in t:
#     d[i] = s.count(i)
# print(d)


# 1.2
# s = input()
# t = set(s)
# d = {i: s.count(i) for i in t}
# print(d)


# 1.3
# s = input()
# d = {}
# t = set(s)
# for i in t:
#     r = 0
#     for j in s:
#         if j == i:
#             r += 1
#     d[i] = r
# print(d)


# 2
# s = input()
# d = dict(Counter(s))
# d2 = d.copy()
# r = 0
# g = ''
# for k, v in d.items():
#     if v >= r:
#         r = v
#         g = k
# r = 0
# p = ''
# for k, v in d.items():
#     if v >= r and k != g:
#         r = v
#         p = k
# print(g, p)


# .most_common(n)  eng kop ishlatilgan n ta sini chiqarib beradi


# 3
# n = 'abcde'
# l = [1, 2, 3, 4, 5]
#
# r = [n[i] + str(l[i]) for i in range(len(n))]
# print(*r) 48 57


# 4
# s = 'a4b8c16d32e64'
# r = ''
# h = ''
# for i in s:
#     if i.isdigit():
#         r += i
#     else:
#         h += i
# print(h + r)

