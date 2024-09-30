from collections import Counter

# ini_list = [10, 10, 20, 30, 40, 40, 50, 50, 50]
ini_list = [1, 1, 3, 1, 1, 2, 2, 4, 5, 1, 3, 4, 5, 4]
res = []    # result array
count = {}  

# Counting frequencies
for num in ini_list:
    count[num] = 1 + count.get(num, 0)


for val in sorted(set(count.values())):
    # sorted(set(count.values())) will sort a set
    temp_arr = []
    for key in count.keys():
        if count[key] == val:
            temp_arr.append(key)
    
    if len(temp_arr) > 1:
        temp_arr.sort()
        
    for num in temp_arr:
        for _ in range(val):
            res.append(num)
            
print(res)
    