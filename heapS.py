"""
This file is the code for changing a random array of numbers into a max heap.

CPE 202
Lab #6

Edward Zhou
"""

def del_max(arr, end = None, compare = 0):
    """
    Deletes the item (integer) with the largest value from an array (arr).
    Args:
        arr (array): an array containing None type items and/ or integers.
        end (int): an index of the array
    Returns:
        arr (array): an array with sorted integers in the form of a max heap.
        temp (int): the largest value in the input array.
        end (int): the index of the last item in the array.
    """
    temp = arr[0]
    arr[0] = arr[end]
    arr[end] = None
    arr, compare = shift_down(arr, 0, end)
    return arr, temp, end-1, compare

def shift_down(arr, index, end, compare = 0):
    """
    Shifts an item (integer) from an index (index) down an array (arr) till
        it reaches end (integer).
    Args:
        arr (array): an array containing None type items and/ or integers.
        index (int): an index of the array
        end (int): an index of the array
    Returns:
        arr (array): an array with sorted integers in the form of a max heap.
    """
    if index*2+2 <= end-1:
        if arr[index] < arr[index*2+1] >= arr[index*2+2]:
            temp = arr[index]
            arr[index] = arr[index*2+1]
            arr[index*2+1] = temp
            compare += 1
            return shift_down(arr, index*2+1, end, compare)

        elif arr[index] < arr[index*2+2]:
            temp = arr[index]
            arr[index] = arr[index*2+2]
            arr[index*2+2] = temp
            compare += 1
            return shift_down(arr, index*2+2, end, compare)
        compare += 1

    elif index*2+1 == end-1:
        if arr[index] < arr[index*2+1]:
            temp = arr[index]
            arr[index] = arr[index*2+1]
            arr[index*2+1] = temp
        compare += 1

    return arr, compare

def heapify(arr, compare = 0):
    """
    Turns an unsorted array (arr) into a max heap via shifting each item up.
    Args:
        arr (array): an array containing None type items and/ or integers.
    Returns:
        arr (array): an array with sorted integers in the form of a max heap.
    """
    length = index = len(arr)-1
    for item in enumerate(arr):
        if length-item[0] < index//2+1:
            arr, compare = shift_down(arr, length-item[0], length+1, compare)
    return arr, compare

def sort(arr):
    """
    Turns an unsorted array (arr) into a max heap via shifting each item up,
        then getting a sorted version by deleting the max value each time.
    Args:
        arr (array): an array containing None type items and/ or integers.
    Returns:
        arr (array): an array with sorted integers in ascending order.
    """
    arr, compare = heapify(arr)
    sort_sub = len(arr)-1
    while sort_sub > 0:
        arr, value, sort_sub, comp = del_max(arr, sort_sub, compare)
        compare += comp
        arr[sort_sub+1] = value
    print(arr)
    return compare
