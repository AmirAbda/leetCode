def merge_two(num_1, num_2):
    merged_list = []
    p1, p2 = 0, 0
    m, n = len(num_1), len(num_2)
    
    while p1 < m and p2 < n:
        if num_1[p1] < num_2[p2]:
            merged_list.append(num_1[p1])
            p1 += 1
        else:
            merged_list.append(num_2[p2])
            p2 += 1
    
    
    while p1 < m:
        merged_list.append(num_1[p1])
        p1 += 1
    while p2 < n:
        merged_list.append(num_2[p2])
        p2 += 1
    
    return merged_list

num_1=[1,3,5,7]
num_2=[2,4,6,8]
print(merge_two(num_1,num_2))