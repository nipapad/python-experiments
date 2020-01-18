

list1 = [1,2,3,4,5,6]
list2 = [6,5,4,3,2,1]

# Holds an iterator object
zipped = zip(list1, list2)

result = map(sum,zipped)

result_list = list(result)

if result_list.count(result_list[0]) != len(result_list):
    print(False)
else:
    print(True)