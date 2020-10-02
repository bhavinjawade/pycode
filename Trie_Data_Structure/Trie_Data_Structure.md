# Trie Data Structure

Trie is an efficient information reTrieval data structure. Trie also called digital tree, radix tree or prefix tree is a kind of search tree—an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings. Using Trie, search complexities can be brought to optimal limit (key length). If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. Using Trie, we can search the key in O(M) time. However the penalty is on Trie storage requirements.
<br>

## Efficiency of Trie

The complexity of creating a trie is O(W x L), where W is the number of words, and L is an average length of the word: you need to perform L lookups on the average for each of the W words in the set.
<br>
In the associated [code](Trie_Data_Structure.py), I have used a text file with more than 7 million words (A file created by concatinating text from Books like - [Gone with the wind](http://biblioteka.kijowski.pl/mitchell%20margaret/gone%20with%20the%20wind.pdf) and few others). Creating the Trie Data structure takes O(m*n) time complexity. 
But searching takes only O(L) complexity where L is the length of word you are going to search.
<br>

### Analysis

If you run the associated [code](Trie_Data_Structure.py) , you must get something like:

```python

Reading the File
Calculating the number of words
No of words: 7171744
>>TIME: 1.359375

Creating Trie Data Structure
Trie Successfully Created
>>TIME: 24.203125

enter the word to search: the
{'No of times word occurs': 407360, 'The word exists': True}
>>TIME: 0.0

```
where the time is in **fractional seconds** and measured using **time.process_time()** in python.

## Advantages of Tries

<br>

* With Trie, we can insert and find strings in O(L) time where L represent the length of a single word. This is obviously faster that BST. 
* This is also faster than Hashing because of the ways it is implemented. We do not need to compute any hash function. No collision handling is required (like we do in open addressing and separate chaining)
* Another advantage of Trie is, we can easily print all words in alphabetical order which is not easily possible with hashing.
We can efficiently do prefix search (or auto-complete) with Trie.

<br>

[![Tries](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Patricia_trie.svg/350px-Patricia_trie.svg.png)](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Patricia_trie.svg/350px-Patricia_trie.svg.png)

<br>

## Advanced Learning Resources
1) https://www.cs.cmu.edu/~fp/courses/15122-f10/lectures/18-tries.pdf
2) http://ellard.org/dan/www/libsq/cb_1998/c06.pdf
3) [Harvard CS50: Tries](https://www.youtube.com/watch?v=TRg9DQFu0kU)