

list=[1,2,3,3,4]
plist=[2,-1,3,4,1,-5]

#basic operations
print("length of list : "+str(len(list)))
print("max of list : "+str(max(list)))
print("min of list : "+str(min(list)))




# Modifying list
list.append(5)
list.append(-1)
print("new list after append: "+ str(list))

list.remove(2);
print("new list after removal: "+ str(list))

list.insert(4,18)
print("list after insertion" + str(list))


#counting object
print("the count of any obj : " + str(list.count(3)))

#reversing the list
plist.reverse()
print("plist after reverse : " + str(plist))

#sorting a list
plist.sort()
print("plist after sorting: "+str(plist))


"""
length of list : 5
max of list : 4
min of list : 1
new list after append: [1, 2, 3, 3, 4, 5, -1]
new list after removal: [1, 3, 3, 4, 5, -1]
list after insertion[1, 3, 3, 4, 18, 5, -1]
the count of any obj : 2
plist after reverse : [-5, 1, 4, 3, -1, 2]
plist after sorting: [-5, -1, 1, 2, 3, 4]
"""