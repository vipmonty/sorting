# boolean is_sorted(lyst): This is a predicate function that returns 
# True if lyst is sorted, False otherwise. In addition 
# to verifying that lyst is a list, is_sorted() must also 
# verify that every element in the list is an integer. 
# If lyst is not a list, or a non-integer 
# element is found in it, is_sorted should raise a TypeError exception.



def is_sorted(lyst):
    integer = type(1)
    if type(lyst[0]) != integer:
        raise TypeError
    else:
        if all(lyst[i] <= lyst[i+1] for i in range(len(lyst)-1)) or all(lyst[i] >= lyst[i+1] for i in range(len(lyst)-1)):
            return True
        else:
            return False
def quicksort(lyst):
    if not isinstance(lyst, list):
        raise TypeError("Input is not a list.")
    
    comparisons = 0
    swaps = 0
    
    def partition(lyst, low, high):
        nonlocal comparisons, swaps
        pivot_index = low
        pivot = lyst[high]
        
        for i in range(low, high):
            comparisons += 1
            if lyst[i] <= pivot:
                lyst[i], lyst[pivot_index] = lyst[pivot_index], lyst[i]
                swaps += 1
                pivot_index += 1
        
        lyst[pivot_index], lyst[high] = lyst[high], lyst[pivot_index]
        swaps += 1
        return pivot_index
    
    def quicksort_helper(lyst, low, high):
        nonlocal comparisons, swaps
        if low < high:
            pivot_index = partition(lyst, low, high)
            quicksort_helper(lyst, low, pivot_index-1)
            quicksort_helper(lyst, pivot_index+1, high)
    
    quicksort_helper(lyst, 0, len(lyst)-1)
    return lyst, comparisons, swaps


def mergesort(lyst):
    if not isinstance(lyst, list):
        raise TypeError("Input is not a list.")
    
    comparisons = 0
    swaps = 0
    
    def merge(lyst, left, mid, right):
        nonlocal comparisons, swaps
        left_half = lyst[left:mid+1]
        right_half = lyst[mid+1:right+1]
        i = j = 0
        k = left
        
        while i < len(left_half) and j < len(right_half):
            comparisons += 1
            if left_half[i] <= right_half[j]:
                lyst[k] = left_half[i]
                swaps += 1
                i += 1
            else:
                lyst[k] = right_half[j]
                swaps += 1
                j += 1
            k += 1
        
        while i < len(left_half):
            lyst[k] = left_half[i]
            swaps += 1
            i += 1
            k += 1
        
        while j < len(right_half):
            lyst[k] = right_half[j]
            swaps += 1
            j += 1
            k += 1
    
    def mergesort_helper(lyst, left, right):
        nonlocal comparisons, swaps
        if left < right:
            mid = (left + right) // 2
            mergesort_helper(lyst, left, mid)
            mergesort_helper(lyst, mid+1, right)
            merge(lyst, left, mid, right)
    
    mergesort_helper(lyst, 0, len(lyst)-1)
    return lyst, comparisons, swaps


def main():
    lyst = [99,56,23,48,67,126,6,8,5]
    print(quicksort(lyst))
    print(f"mergesort:",mergesort(lyst))



    # quicksorted = quicksort(lyst,0,len(lyst)-1)
    # print(tuple(lyst),quicksorted)





    # stringing="dog"
    # lyst_sorted = sorted(lyst)
    # results=is_sorted(lyst)
    # print(results)
if __name__ == "__main__":
    main()