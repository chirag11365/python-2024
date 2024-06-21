# Python lists are containers to store a set of values of any data type 
friends = ["apple", "orange", 5,365.78,False,"akash","roahn"]
print(friends[0])
friends[0] = 'grapes'
print(friends[0])
print(friends[1:4]) 
# # Output: grapes

l1 = [1,34,23,67,2,11]

print(l1.sort())
print(l1)

print(l1.reverse())
print(l1)

l1.insert(4,444444444) # insert 4444444444 such that its index is 4 
print(l1)

value=l1.pop(2) # 23 will be removed
print(value,",pop value extracted")