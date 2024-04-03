# s = ["5","2","C","D","+"]
# l = []
# for i in s:
#     if i.isdigit():
#         l.append(int(i))
#     elif i == '+':
#         l.append(l[-1] + l[-2])
#     elif i == 'C':
#         l.pop()
#     elif i == 'D':
#         l.append(l[-1] * 2)
# print(l)]

# words = ["pay", "attention", "practice", "attend"]
# pref = "at"
# r = [1 for word in words if word[:len(pref)] == pref]
# print(r)


# nums1 = [1, 2, 3]
# nums2 = [2, 4, 6]
# res = [[], []]
# for i in nums1:
#     if i not in nums2:
#         res[0].append(i)
# for i in nums2:
#     if i not in nums1:
#         res[1].append(i)
# nums1.pop(i)
# print([nums1, nums2])
# print(not nums1[0] in nums2)
# print(res)


# nums = [9,6,4,2,3,5,7,0,1]
# for i in range(max(nums)):
#     if i not in nums:
#         s = i

from decimal import Decimal

# a = '1'
# b = '100'
# bo = (bin(int(a, 2) + int(b, 2)))
# print(bo[2:])


# digits = [4,3,2,1]
# r = ''
# l = []
# for i in digits:
#     r += ''.join(str(i))
# for i in r:
#     l.append(int(i))
# print(int(r) + 1)

# nums = [1, 2, 3, 11]
# r = nums[1:]
# # print(r)
# for i in r:
#     if str(nums[0]) in str(i):
#         print(1)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums.index(3))