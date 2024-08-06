# print("first commit. Actually not :)")
# print("test branch")
#
#

# import copy
# m_list = [1, 2, 3, 4, 5, 5, ]
# m_set = set(m_list)
# print("m-set", m_set)
#
# m_set1 = copy.deepcopy(m_set)
# m_set2 = copy.copy(m_set)
# m_set.add(20)
# print("m-set",m_set)
# print("m-set1",m_set1)
# print("m-set2",m_set1)

'''
userString = input("Your string: ")
setPunctuation = {".",",",";",":","!","?"}
#setPunctuation = set(",.:;!?")
stringSet = list(userString)
print(stringSet)

count = 0
for item in stringSet:
    if item in setPunctuation:
        count +=1

print(count)

'''

user_input = input("Code: ")
user_Set = set(user_input)
userSetNum = set()
for item in user_Set:
    if item.isdigit():
        userSetNum.add(item)

print(userSetNum)

print(set([x for x in user_Set if x.isdigit()]))

