To find the floored square root in log n time I used a divide an conquer
approach. No additional data structures were necessary. At each step 
I check the squared value of the current number at the mid point and decide to 
increase or decrease the left or right pointer similar to binary search


Space Complexity
O(1) because no additional data structures are used, the only space used is
a constant amount for storing variables and values in the function

Time Complexity
O(log n) if we consider N as the number of possible integers between 0 and the
input value then at each iteration of the while look we are cutting down our
problem by 1/2. it will take log n steps to find the point where the pointers
cross or we have found an exact square
