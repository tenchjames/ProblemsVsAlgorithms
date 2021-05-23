Problem 5

For this problem we were to use a TrieNode. When inserting a node I chose to 
return a refrence to the inserted node. This made getting a refrence to the
node easier when doing an insert in the Trie itself so a handler could be
attached. To find suffixes I used a helper function for the recursion so
I could keep an output list that I could pass down and build up each level of
recursion

Time complexity

TrieNode
insert = O(1) because it is simply checking a dictionary and doing an insert
which are all constant time for this data structure

suffixes = O(n) because for a single input node it is possible to return the
suffix for every word in the Trie. 

Trie
insert = O(n) let n = number of characters in the word. We iterate over each to 
do the insert.

find = O(n) let n = number of characters in the prefix we are searching. Each 
character is iterated over as we descend deeper into the Trie


Space complexity

TrieNode

O(n) space. The amount of space in each node grows linearally based on the
number of characters stored in the node.


Trie

O(n) space when n is defined as the number of possible characters accross all
words stored in the Trie. It would be O(n) in the worst case if each word
stored had unique characters from all other words. In practice the storeage is
much less.




