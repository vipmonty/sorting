#code snippet 
from random import seed, sample

# error handling 
def is_sorted(lyst):
    if not isinstance(lyst, list):
        raise TypeError("Input is not a list.")
    
    for element in lyst:
        if not isinstance(element, int):
            raise TypeError("List contains non-integer elements.")
    
    return all(lyst[i] <= lyst[i+1] for i in range(len(lyst)-1))

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

def selection_sort(lyst):
    if not isinstance(lyst, list):
        raise TypeError("Input is not a list.")
    
    comparisons = 0
    swaps = 0
    
    for i in range(len(lyst)):
        min_index = i
        for j in range(i+1, len(lyst)):
            comparisons += 1
            if lyst[j] < lyst[min_index]:
                min_index = j
        lyst[i], lyst[min_index] = lyst[min_index], lyst[i]
        swaps += 1
    
    return lyst, comparisons, swaps

def insertion_sort(lyst):
    if not isinstance(lyst, list):
        raise TypeError("Input is not a list.")
    
    comparisons = 0
    swaps = 0
    
    for i in range(1, len(lyst)):
        key = lyst[i]
        j = i - 1
        while j >= 0 and lyst[j] > key:
            comparisons += 1
            lyst[j+1] = lyst[j]
            swaps += 1
            j -= 1
        lyst[j+1] = key
        swaps += 1
    
    return lyst, comparisons, swaps

def main():
    DATA_SIZE = 100000
    seed(0)
    DATA = sample(range(DATA_SIZE+3), k=DATA_SIZE)
    test = DATA.copy()
    
    print("Starting insertion_sort")
    results = insertion_sort(test)
    sorted_list, comparisons, swaps = results
    print("Sorted List:", sorted_list[:10])  # Example: print the first 10 elements
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)
    
    # Repeat the above process for the other sorting functions:
    # results = quicksort(test)
    # results = mergesort(test)
    # results = selection_sort(test)
    
    # Perform additional tests and analyze the results as needed
    
if __name__ == "__main__":
    main()