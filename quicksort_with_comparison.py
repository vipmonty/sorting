def quicksort(A, lo, hi):
  if lo >= 0 and hi >= 0 and lo < hi:
    (comp, swap, p) = partition(A, lo, hi)
    (lcomp, lswap) = quicksort(A, lo, p)
    (rcomp, rswap) = quicksort(A, p + 1, hi)
    return (comp + lcomp + rcomp, swap + lswap + rswap)
  return (0,0)

def partition(A, lo, hi):
  comp = 0
  swap = 0
  pivot = A[(hi + lo) // 2]
  i = lo
  j = hi
  while True:
    while A[i] < pivot:
      comp += 1
      i += 1
    while A[j] > pivot:
      comp += 1
      j -= 1
    if i >= j:
      return (comp, swap, j)
    swap += 1
    A[i], A[j] = A[j], A[i]


x = [5,0,9,7,4,2,8,3,1,6]
print(x)
quick_sorted = quicksort(x, 0, len(x)-1)
print(tuple(x),quick_sorted)
