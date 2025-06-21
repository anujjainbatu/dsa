# https://www.naukri.com/code360/problems/ninja-and-the-second-order-elements_6581960?leftPanelTabValue=PROBLEM

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    first_max = second_max = 0
    first_min = second_min = float("inf")

    for nums in a:
        #largest
        if nums > first_max:
            second_max = first_max
            first_max = nums
        elif nums > second_max and nums != first_max:
            second_max = nums
        #smallest
        if nums < first_min:
            second_min = first_min
            first_min = nums
        elif nums < second_min and nums != first_min:
            second_min = nums

    return [second_max,second_min]
