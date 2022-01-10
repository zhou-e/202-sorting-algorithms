def quick_sort(items, start = 0, end = None, compare = 0):
    if end is None:
        end = len(items)-1
    size = (end-start)+1
    if size < 2:
        return items, compare

    pivot = (start+end)//2
    temp = items[start]
    items[start] = items[pivot]
    items[pivot] = temp

    l_point, r_point = start+1, end
    while l_point <= r_point:
        if items[l_point] < items[start]:
            l_point += 1
            compare += 1
        if items[r_point] > items[start] and l_point <= r_point:
            r_point -= 1
            compare += 1
        elif l_point < len(items) and items[r_point] < items[l_point] and \
             items[l_point] > items[start] and l_point <= r_point:
            temp = items[r_point]
            items[r_point] = items[l_point]
            items[l_point] = temp
            compare += 1

    temp = items[start]
    items[start] = items[r_point]
    items[r_point] = temp

    items, compare = quick_sort(items, start, r_point-1, compare)
    items, compare = quick_sort(items, r_point+1, end, compare)
    return items, compare

def caller(items):
    temp, compare = quick_sort(items)
    return compare
