# https://www.naukri.com/code360/problems/implement-upper-bound_8165383?leftPanelTabValue=PROBLEM

def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    n = len(arr)
    l = 0
    r = n - 1
    upper_Bound = n

    while r >= l:
        mid = (l+r)//2

        if arr[mid] <= x:
            l = mid + 1
        else:
            r = mid - 1
            upper_Bound = mid

    return upper_Bound
