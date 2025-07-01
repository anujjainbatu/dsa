# https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401

def getFloorAndCeil(a, n, x):
    l = 0
    r = n - 1
    result = [-1,-1]

    while r >= l:
        mid = (l+r)//2

        if x < a[mid]:
            r = mid - 1
            result[1] = a[mid] #possible ceil
        elif x > a[mid]:
            l = mid + 1
            result[0] = a[mid] #possible floor
        else:
            return [a[mid], a[mid]]

    return result
