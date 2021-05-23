Problem 4

I used a counting sort algoritm to solve in O(n) time. Because the values are 
well known (0, 1, 2) this makes count sort a good solution.

Time complexity
O(n) is the running time. There are n iterations to look at each element of the
input_list and add to the counter.
There is an addition n iterations for each count in the array to build back the
final array.
O(n) + O(n) = O(n)

Space complexity
O(1) Additional space is used for the count array. This space is constant
because the problem will always store an array with 3 elements. I also 
updated the original input_list with the new sorted values so no additional 
storage was used for the output results
