def merge_sort(items, compare = 0):
    if len(items) == 1:
        return items, compare
    left, compare = merge_sort(items[:len(items)//2], compare)
    right, compare = merge_sort(items[len(items)//2:], compare)
    return merge(left, right, compare)

def merge(left, right, compare = 0):
    temp = []
    l_index = r_index = 0
    length_l, length_r = len(left), len(right)
    while l_index < length_l and r_index < length_r:
        if left[l_index] <= right[r_index]:
            temp.append(left[l_index])
            l_index += 1
            compare += 1
        else:
            temp.append(right[r_index])
            r_index += 1
            compare += 1
    if l_index < length_l:
        for item in enumerate(left[l_index:]):
            temp.append(item[1])
    elif r_index < length_r:
        for item in enumerate(right[r_index:]):
            temp.append(item[1])
    return temp, compare

def caller(items):
    temp, compare = merge_sort(items)
    return compare
