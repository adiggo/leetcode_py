
# find the right location of a number in a sorted array
def get_ceil_index_bst(arr, left, right, num):
    while right > left:
        mid = left + (right -left)/2
        if num > arr[mid]:
            left = mid + 1
        else:
            right = mid
    return left

# LIS
def LIS(arr):
    helper = []
    for i in arr:
        if len(helper) == 0:
            helper.append(i)
            continue

        if i > helper[len(helper)-1]:
            helper.append(i)
        elif i < helper[0]:
            helper[0] = i
        else:
            ceil_index = get_ceil_index_bst(arr, 0, len(helper)-1, i)
            helper[ceil_index] = i
        return len(helper)

