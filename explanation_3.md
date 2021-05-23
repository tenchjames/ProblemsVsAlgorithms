Problem 3

To rearrange the digits in O(n log n) time as required i solved the problem
using quick sort. The version I implemented uses a median of 3 approach to 
try to pick a good pivot each time so quick sort will perform O(n log n) with 
very high probability.

After solving the next problem (problem 4) I realized this could also be solved 
in time better than 0(n log n) if we avoid the sort and use counting sort.


Time complexity
O(n log n) for the sorted version. Quick sort takes O(n log n). Plus O(n) time 
to iterate over the sorted array and build up the two numbers.
O(n log n) + O(n) = O(n log n)

O(n) for the count sort version. O(n) to iterate of each digit and increase the
count for each. The total of all the counts = n. O(n) to iterate all counts to 
build up the two numbers
O(n) + O(n) = O(n)


Space complexity
O(1) for the quick sort version. Quick sort sorts the array in place so no
additional data structures are used. Everything else is just constant factors.

O(1) for the count sort version as well. We do use additional space for the 
count array. However the size is not determined by the input, it will always 
be an array holding the count for each of the 10 possible digits

