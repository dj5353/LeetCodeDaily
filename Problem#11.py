class TrieNode:
    def __init__(self):
        self.children = {}
        self.my_total_word_so_far = ''
        self.endofword = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        d = self.root.children
        for c in word:
            if c not in d:
                node = TrieNode()
                d[c] =  node
            else:
                node = d[c]
            d = node.children
            n1 = node
        n1.endofword = True
        if(n1.endofword):
            self.root.my_total_word_so_far += word

    def search(self,word):
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.endofword


    def prefix(self,word):
        d = self.root.children
        for c in word:
            if c not in d:
                return False
            d = d[c].children
        return True

                

    def auto_complete(self,word):
        if len(word)>0 and word[0] in self.root.children:
            self.root.children[word[0]].auto_complete(word[1:])
        if(len(word) == 0):
            print("Auto Complete : ")
            self.print_tree()


    def print_tree(self):
        if self:
            if(len(self.root.children) == 0):
                print("Word : ",self.root.my_total_word_so_far)
            else:
                for i in self.root.children:
                    self.root.children[i].print_tree()


call = Trie()
call.insert("dear")
call.insert("deer")
print("Inserted Successfully!")
print(call.prefix("de"))
print(call.search("deer"))
call.auto_complete('d')


