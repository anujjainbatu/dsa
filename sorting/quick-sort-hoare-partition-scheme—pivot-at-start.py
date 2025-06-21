class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi)
            self.quickSort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low - 1
        j = high + 1

        while True:
            # Move i to the right until arr[i] >= pivot
            i += 1
            while arr[i] < pivot:
                i += 1

            # Move j to the left until arr[j] <= pivot
            j -= 1
            while arr[j] > pivot:
                j -= 1

            # If two pointers cross, return j
            if i >= j:
                return j

            # Otherwise, swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
