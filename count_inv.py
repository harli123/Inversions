from Merge_Sort import merge_sort

def count_inversions(lst):
    """
    counts inversions in LST. Inversion: is when the natural relative order
    or 2 elements does not match their relative order in LST
    Also outputs new ordered list
    """
    if len(lst) < 2:
        return lst, 0
    else:
        split_index = round(len(lst)/2)
        left = lst[:split_index]
        right = lst[split_index:]
        left_inv = count_inversions(left)[1]
        right_inv = count_inversions(right)[1]
        output_lst, split_inv = merge_count(merge_sort(left), merge_sort(right))
        total = left_inv + right_inv + split_inv
    return output_lst, total


def merge_count(lst_a, lst_b):
    """
    merges 2 lists. to be used in merge_sort function. non-destructive
    Counts the inversions between LST_A and LST_B
    """
    lst = []
    i = 0
    j = 0
    inv_count = 0
    while i < len(lst_a) and j < len(lst_b):
        if lst_a[i] < lst_b[j]:
            lst.append(lst_a[i])
            i += 1
        else:
            lst.append(lst_b[j])
            inv_count += len(lst_a) - i
            j += 1
    if i < len(lst_a):
        for i in range(i, len(lst_a)):
            lst.append(lst_a[i])
    elif j < len(lst_b):
        for j in range(j, len(lst_b)):
            lst.append(lst_b[j])
    return lst, inv_count
"""
lst = [1,8,5,3,2,6,4,7]
# number of inversions = 3 + 2 + 3 + 1 + 1 + 1 = 11
print(count_inversions(lst))
lst2 = [1,3,2]
print(count_inversions(lst2))
"""
