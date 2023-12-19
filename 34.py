arr = [1, 1, 2,3,4,3, 4,10 , 4,5,6,9]

def find_duplicate(arr):
    count_dict = {}
    for elem in arr:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    # duplicate_list = [elem for elem in count_dict if count_dict[elem] > 1]
    # return duplicate_list
    return(count_dict)

duplicate_numbers = find_duplicate(arr)
d=[]
for k,v in duplicate_numbers.items():
    if v > 1:
       # print(f"The duplicate number in the list are: {k}")
       d.append(k)
print(d)

l = []
m =[]
for i in arr:
    if i not in l:
        l.append(i)
    elif i not in m:
        m.append(i)

print(l)
print(m)