import time

class TrieNode:
  children = {}
  endofword = False
  def __init__(self):
    self.children = {}
    self.endofword = False
    self.count = 0

root = TrieNode() 
def insert(word):
  current = root
  for i in range(len(word)):
    if word[i] not in current.children:
      node = TrieNode()
      current.children[word[i]] = node
    else:
      node = current.children[word[i]]
    current = node
  current.endofword = True
  current.count += 1

lis = []
def printTrie(current):  
  for char, node in current.children.items():
    print(char,end='')
    lis.append(node)
  print("")
  if lis:
    nextnode = lis.pop()
    printTrie(nextnode)

def search(word,root):
  current  = root
  for i in range(len(word)):
    if word[i] not in current.children:
      return False
    else:
      node = current.children[word[i]]
    current = node
  return {"The word exists" : current.endofword,"No of times word occurs" : current.count}

start = time.process_time()
print("Reading the File")
store = open("store_for_trie.txt","r",encoding="utf8")
text = store.read()
words = text.split()
print("Calculating the number of words")
print("No of words: " + str(len(words)))
print(">>TIME: "+str(time.process_time() - start))

starts = time.process_time()
print("Creating Trie Data Structure")
for word in words:
      insert(word)
print("Trie Successfully Created")
print(">>TIME: "+str(time.process_time() - starts))

startss = time.process_time()
tosearch = input("enter the word to search: ")
print(search(tosearch,root))
print(">>TIME: "+str(time.process_time() - startss))

# insert("HelloBhavin")
# insert("Hell")
# insert("Hello")
# insert("Hat")
# insert("Cases")
# insert("Cast")
# insert("Cause")
# insert("Chastise")
# insert("Date")
# print(search("Bhavin",root))
# print(search("Hello",root))
# print(search("Hell",root))
# print(search("Cast",root))
# print(search("Dat",root))
# print(search("Date",root))
# printTrie(root)