from operator import itemgetter
num=int(input("Enter the number of strings to be sorted: "))
org_list=[]
for i in range(num):
    str=input("Enter the string: ")
    org_list.append(str)
print("Original List of Strings: ", org_list)
sorted_list=sorted(org_list,key=itemgetter(-2))
print("Sorted List of String: ",sorted_list)
