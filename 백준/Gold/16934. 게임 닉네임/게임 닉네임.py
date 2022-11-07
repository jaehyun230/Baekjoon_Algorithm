from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

n = int(input())

class Node :
  def __init__(self) :
    self.word = False
    self.children = {}

class Trie :
  def __init__ (self) :
    self.root = Node()

  def insert(self, word) :
    node = self.root

    for char in word :
      if char not in node.children :
        node.children[char] = Node()
      node = node.children[char]
    name_dic[word] +=1
    node.word = True
    
  def search(self, word) :
    node = self.root
    result = ""
    for char in word :
      result +=char
      if char not in node.children :
        return result
      node = node.children[char]

    if node.word :
      result += str(name_dic[result]+1)
    return result
  
name_dic = defaultdict(int)
Trie = Trie()

for _ in range(n) :
  word = input().rstrip()
  print(Trie.search(word))
  Trie.insert(word)