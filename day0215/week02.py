import copy
# l = [1,2,3,[4,5]]
#
# l2 = copy.copy(l)
# l2.append(5)
# # l.append(6)
# print(id(l))
# print(id(l2))
# print(l)
# print(l2)

#浅拷贝
l1 = [1,2,[3,4]]
print(l1)
l2 = copy.copy(l1)
print(l2)
# list1.append(5)
# print(list1,list2)
l1[2].append(3.5)
print(l1,l2)


#深拷贝
l1 = [1,2,[3,4]]
print(l1)

l2 = copy.deepcopy(l1)
print(l2)
l1.append(5)
l2[2].append(3.5)
print(l1)
print(l2)