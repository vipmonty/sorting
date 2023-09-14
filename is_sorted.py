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

def main():
    lyst = [99,56,23,48,67,126,6,8,5]
    stringing="dog"
    lyst_sorted = sorted(lyst)
    results=is_sorted(lyst)
    print(results)
if __name__ == "__main__":
    main()