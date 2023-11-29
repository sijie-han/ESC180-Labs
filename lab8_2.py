def binary_search(L, e):
   low = 0
   high = len(L)-1
   while high-low >= 2:
      mid = (low+high)//2 #e.g. 7//2 == 3
      if L[mid] > e:
         high = mid-1
      elif L[mid] < e:
         low = mid+1
      else:
         return mid
   if L[low] == e:
      return low
   elif L[high] == e:
      return high
   else:
    return None
binary_search([1,2,3,4,5,6,7,8,9,10], 5)