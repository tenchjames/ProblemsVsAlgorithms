
Problem 7

The primary difference between this problem and the prior is how we are
splitting the path into words instead of characters. I made assumptions and
implemented those into the code for the "/" character. A valid route will be 
seperated by a "/" and cannot have trailing or beginning spaces. In addition, 
to simplify the routing I removed extra "//" occurrences when filtering.

Time complexity

RouteTrieNode
insert = O(1) because it is simply checking a dictionary and doing an insert
which are all constant time for this data structure


RouteTrie
insert = O(n) let n = number of path parts in the url. We iterate over each to 
do the insert.

find = O(n) let n = number of path parts in the url we are searching. Each 
part of the path is iterated over as we descend deeper into the Trie

Router
add handler = O(n) where n is the number of path parts in the path being
inserted because each path part needs to be accessed to go deeper in the 
trie for insertion

lookup = O(n) because all parts of the path need to be searched to reach the 
node at the end.


Space complexity

TrieNode

O(n) space. The amount of space in each node grows linearally based on the
number of path parts stored in the node.


RouteTrie

O(n) space when n is defined as the number of possible path parts accross all
urls stored in the RouteTrie. It would be O(n) in the worst case if each url
stored had unique paths from all other urls. 

Router
O(C^n) because a single path as the input could be split into an infinite
number of path parts that need to be stored for a single url. 
For example the route /a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/a/deep_a is a single 
route that expands into many paths that need to be stored for one url


