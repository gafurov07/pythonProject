# l = '2345'
# n = 2
# for i in range(n):
#     s = l[0]
#     l = l[1:]
#     l += ''.join(s)
# print(l)
import math
from itertools import chain

# m = [
#     [3, 6, 9, 8, 7],
#     [7, 4, 1, 2, 3],
#     [8, 5, 2, 4, 9],
#     [2, 5, 7, 3, 4],
#     [7, 3, 4, 9, 6]
# ]
#
# for h in range(5):
#     for i in range(h, len(m)):
#         for j in range(h, len(m[0])):
#             print(m[i][j], end=' ')
#         print()
#     print()


# l = [1, 2, 3, 5, 4, 6, 7]
# for i in range(1, len(l) + 2):
#     if i not in l:
#         print(i)
#         s += 1
# if s == 0:
#     print(l[-1] + 1)

# l = [[1, 2], [3, 3]]
# r = list(chain(*l))
# print(sum(r) - sum(min(r), max(r)) *  / 2)

#
# m = [
#     [3, 6, 9, 8, 7],
#     [7, 4, 1, 2, 3],
#     [8, 5, 2, 4, 9],
#     [2, 5, 7, 3, 4],
#     [7, 3, 4, 9, 6]
# ]
# print(*map(min, zip(*m)))

# for i in range(len(m)):
#     l = []
#     for j in range(len(m[0])):
#         l.append(m[j][i])
#     print(min(l), end=' ')


# matrix = [
#     [3, 7, 8],
#     [9, 11, 13],
#     [15, 16, 17]
# ]
# min_ = list(map(min, matrix))
# max_ = list(map(max, zip(*matrix)))
# for i in matrix:
#     for j in i:
#         if j in min_ and j in max_:
#             print(j)


# matrix = [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]]
# res = []
# for i in range(len(matrix)):
#     row = []
#     for j in range(len(matrix[0])):
#         row.append(matrix[len(matrix) - 1 - j][i])
#         # matrix[i][j] = matrix[2 - j][i]
#         # print(matrix[2 - j][i], end=' ')
#     res.append(row)
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         matrix[i][j] = res[i][j]
#
# print(res)
# print(matrix)


# matrix = [[15, 7, 18, 11, 19, 10, 14, 16, 8, 2, 3, 6, 5, 1, 17, 12, 9, 4, 13],
#           [17, 15, 9, 8, 11, 13, 7, 6, 5, 1, 3, 16, 12, 19, 10, 2, 4, 14, 18],
#           [19, 14, 12, 10, 8, 9, 17, 16, 4, 3, 13, 18, 1, 5, 7, 11, 2, 15, 6],
#           [4, 2, 10, 15, 19, 16, 8, 9, 5, 3, 1, 11, 13, 14, 6, 18, 12, 17, 7],
#           [13, 19, 9, 16, 5, 8, 6, 12, 14, 11, 18, 10, 7, 2, 3, 4, 15, 17, 1],
#           [4, 7, 18, 11, 17, 16, 5, 12, 10, 1, 15, 13, 14, 6, 19, 2, 3, 9, 8],
#           [14, 5, 15, 1, 18, 6, 12, 7, 8, 9, 3, 13, 2, 10, 19, 4, 11, 16, 17],
#           [10, 3, 1, 8, 14, 19, 11, 18, 15, 13, 9, 12, 16, 17, 7, 4, 5, 2, 6],
#           [14, 13, 19, 18, 7, 2, 4, 8, 10, 17, 12, 5, 15, 1, 6, 9, 11, 3, 16],
#           [19, 8, 10, 18, 16, 12, 11, 17, 4, 9, 7, 2, 5, 13, 15, 3, 6, 1, 14],
#           [1, 10, 6, 14, 7, 18, 3, 9, 4, 16, 5, 11, 13, 17, 15, 8, 19, 2, 12],
#           [13, 10, 5, 16, 1, 19, 17, 3, 9, 11, 7, 8, 12, 6, 4, 2, 14, 15, 18],
#           [17, 2, 1, 6, 9, 19, 18, 14, 4, 11, 12, 13, 16, 5, 8, 7, 3, 10, 15],
#           [1, 4, 10, 5, 13, 6, 18, 11, 3, 2, 15, 14, 16, 12, 17, 19, 8, 9, 7],
#           [2, 14, 3, 12, 16, 17, 11, 9, 1, 6, 5, 19, 10, 13, 4, 18, 7, 15, 8],
#           [15, 9, 8, 18, 14, 13, 4, 12, 5, 17, 6, 1, 11, 16, 19, 3, 7, 2, 10],
#           [15, 8, 12, 16, 13, 2, 6, 19, 18, 14, 10, 5, 11, 9, 7, 1, 3, 17, 4],
#           [15, 6, 17, 7, 5, 3, 1, 9, 19, 12, 10, 11, 16, 14, 18, 8, 2, 13, 4],
#           [6, 11, 10, 14, 2, 13, 16, 1, 9, 15, 8, 19, 17, 3, 5, 18, 7, 4, 12]]
# r = []
# for i in range(len(matrix)):
#     matrix[i] = sorted(matrix[i])
#     print(matrix[i])
# for i in range(len(matrix)):
#     for j in range(i, len(matrix)):
#         if matrix[j] != matrix[i]:
#             r.append('False')
# if 'False' not in r:
#     print(True)
# else:
#     print(False)

# for i in matrix:
#     r.extend(i)
# print(True if len(set(r)) =
# r = []= len(matrix) else False)

# print(matrix[0] in matrix[1])
# s = []
# for i in range(len(matrix)):
#     for j in matrix[i+1]:
#         if j in matrix[i]:
#             s.append('True')
#         else:
#             s.append('False')
#     if 'False' in s:
#         print(False)
#         break
# else:
#     print(True)

# r = set(map(sum, matrix))
# print(len(r))
# for i in range(1, len(matrix)):
#     s = 0
#     for j in range(1, len(matrix[0])):
#         s += matrix[i][j]
#     if s == sum(matrix[0]):
#         r += 1
# if r == len(matrix):
#     print(True)
# else:
#     print(False)

# mat = [
#     [0, 0, 0],
#     [0, 1, 0],
#     [1, 1, 1]]
# target = [
#     [1, 1, 1],
#     [0, 1, 0],
#     [0, 0, 0]]
# l = mat
# n = 1
# while n != 4:
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#
#
#     n += 1

# for i in range(len(target)):
#     target[i] = tuple(target[i])
# r = list(zip(*reversed(mat)))
# n = 0
# while n != 4:
#     if r == target:
#         print(True)
#         break
#     r = list(zip(*reversed(r)))
#     n += 1
# else:
#     print(False)


# m = [
#     [1, 2, 3, 4],
#     [5, 1, 2, 3],
#     [9, 5, 1, 2],
# ]
# l = []
# for i in range(1, len(m) + 1):
#     l.append(i)
# print(l)
#
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         if i == j:
#             print(m[i][j], end='  ')
#         else:
#             print(' ', end='  ')
#     print()

# matrix = [
#     [1, 9, 1],
#     [5, 4, 7],
#     [1, 2, 3]]
# for i in range(len(matrix)):
#     r = []
#     for j in range(len(matrix[0])):
#         r.append(matrix[j][i])
#     pass


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l[::-1])

# def func(a: list[int], b: list[int]) -> bool:
#     if len(a) != len(set(a)) or len(b) != len(set(b)):
#         return False
#     for i in range(min(a), max(a) + 1):
#         if i not in a:
#             return False
#     for i in range(min(b), max(b) + 1):
#         if i not in b:
#             return False
#     for i in a:
#         l = b.count(i)
#         if l > 1 or l == 0:
#             return False
#     else:
#         return True
#
#
# print(func([3, 3, 1], [3, 2, 1]))
#
# matrix = [
#     [1, 2, 3],
#     [2, 1, 2],
#     [3, 3, 1]
# ]
# matrix2 = list(zip(*matrix))
# print(func([1, 2, 3], [1, 2, 3]))
#
# for i in range(len(matrix)):
#
#     print(func(matrix[i], matrix2[i]))


# def func(m):
#     return list(zip(*reversed(m)))
#
#
# mat = [
#     [0, 0, 0],
#     [0, 1, 0],
#     [1, 1, 1]]
# target = [
#     [1, 1, 1],
#     [0, 1, 0],
#     [0, 0, 0]]
#
# for h in range(4):
#     r = []
#     for i in func(mat):
#         l = []
#         for j in i:
#             l.append(j)
#         r.append(l)
#     if r == target:
#         print(True)
#         break
#     mat = r
# else:
#     print(False)


# def f(m: list[int], k: int):
#
#     for h in range(k):
#         m.append(m[0])
#         m.pop(0)
#     return m
#
#
# mat = [[1,2]]
# k = 1
# r = []
#
# print(mat)
# for i in mat:
#     r.append(f(i, k))
#     print(mat)
#     print(r)
#
#
# print(mat == r)


# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# r = m
# for i in range(len(m)):
#     s = []
#     for j in range(len(m[0])):
#         s.append(m[j][i])
#         r[i][j] += s
#
#
# print(sum(r[0]), sum(r[-1]))
