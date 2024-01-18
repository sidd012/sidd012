import copy
list1=[1,2,3,4,5]
list2=copy.copy(list1)
print("list2 ID",id(list2),"value",list2)
list3=copy.decopy(list1)
print("lsit3 ID",id(list3),"value",list3)