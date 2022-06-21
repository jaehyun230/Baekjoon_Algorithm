import sys

input = sys.stdin.readline

n = int(input())

class Trie :
  def __init__(self) :
    self.root = {}

  def insert(self, s) :
    cur_node = self.root
    for c in s :
      if c not in cur_node :
        cur_node[c] = {}
      cur_node = cur_node[c]
    cur_node['*'] = {}

  def trie_search(self, level, cur_node = None) :
    if level == 0 :
      cur_node = self.root

    for c in sorted(cur_node.keys()) :
      if c != '*' :
        print('--' * level, c, sep="")
      self.trie_search(level+1, cur_node[c])
    
trie = Trie()
for _ in range (n) :
  info = list(input().rstrip().split())
  trie.insert(info[1:])

trie.trie_search(0)