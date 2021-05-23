Problem 2

Because the array is sorted, but rotated I chose to solve the problem in 
two steps. The first step is to find the index of the lowest value. The second
step was a regular binary search once we knew where our lowest index is and how
it relates to the value we are trying to find.

Time complexity
O(log n) because both steps take log n time because the problem size is reduced
by 1/2 in each iteration. we do this two times. Overall it will take 2 * log n
but with big O we can eliminate the constant factor and the result is still 
O(log n)

Space complexity
No additional data structures are used in the code, so the space complexity is 
a constant. O(1)
