def merge_sort(lst):
    """
    takes in list and sorts them using merge sort algorithm described
    in Alg:D&A Part I class. Non destructive
    """
    if len(lst) < 2:
        return lst
    else:
        split_index = round(len(lst) / 2)
        left = merge_sort(lst[:split_index])
        right = merge_sort(lst[split_index:])
        merged = merge(left,right)
    return merged

def merge(lst_a, lst_b):
    """
    merges 2 lists. to be used in merge_sort function. non-destructive
    """
    lst = []
    i = 0
    j = 0
    while i < len(lst_a) and j < len(lst_b):
        if lst_a[i] < lst_b[j]:
            lst.append(lst_a[i])
            i += 1
        else:
            lst.append(lst_b[j])
            j += 1
    if i < len(lst_a):
        for i in range(i, len(lst_a)):
            lst.append(lst_a[i])
    elif j < len(lst_b):
        for j in range(j, len(lst_b)):
            lst.append(lst_b[j])
    return lst
"""
lst = [1,6,4,7]
lst2 = [3,2,5,8]
new_lst = merge(lst,lst2)
print(lst,lst2)
print(new_lst)

print(merge_sort(lst+lst2))
lst3 = ['a','c','g','f','d','e','b']
print(merge_sort(lst3))
"""



