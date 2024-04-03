# m = [
#     [3, 5, 7],
#     [1, 5, 9],
#     [8, 5, 2],
#     [4, 5, 6]
# ]
#
# for j in range(len(m)):
#     s = 0
#     for i in range(len(m[j+1])):
#         s += m[i][j]
#     print(s)


# s = input()
# print(*[i.capitalize() for i in s.split()])


# from itertools import groupby
# s = 'ffaaaaxxrdddin'
# # t = [k + str(v) if len(list(v)) > 1 else k for k, v in groupby(s)]
# t = ''
# for k, v in groupby(s):
#     r = len(list(v))
#     t += k + ('' if r == 1 else str(r))
# print(t)


# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print([j for i in a for j in i])


# l = [1, 2, 3, 4, 5]
# print([sum(l[:i+1]) for i in range(len(l))])


# l = [1, 2, 3]
# r = 1
# for i in l:
#     r *= i
# print(r)


# r = 'alla'
# print(r[::-1] == r)


# from itertools import
# l = ["flower","flow","flight"]
# p = ''
# # print(l[0][0])
# for i in range(len(l)):
#     h = l[0][i]
#     for j in zip(l):
#         if

