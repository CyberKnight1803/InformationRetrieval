from typing import Tuple

class TrieNode(object):
    """
    Trie node implementation
    """
    def __init__(self, char):
        self.char = char
        self.is_end_of_word = False
        self.children = []

def addWord(root, word):
    """
    Adding word in Trie
    """

    node = root
    for char in word:
        char_present = False
        
        for child in node.children:
            if child.char == char:
                node = child
                char_present = True
                break
        
        if not char_present:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    
    node.is_end_of_word = True



def recursive_word_find(node, possible_words, prefix):
    if node.is_end_of_word == True:
        possible_words.append(prefix)
    
    for child in node.children:
        recursive_word_find(child, possible_words, prefix+child.char)



def find_possible_words(root, prefix, possible_words, prefix_leftoff):
    
    node = root
    
    if not root.children:
        return
    
    for i in range(len(prefix)):
        
        if prefix[i] == '?':
            for child in node.children:
                find_possible_words(child, prefix[i+1:], possible_words, prefix_leftoff+prefix[:i]+child.char)
        
        else:
            char_not_found = True
            
            for child in node.children:
                if child.char == prefix[i]:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return
    
    recursive_word_find(node, possible_words, prefix_leftoff+prefix)
    return possible_words

if __name__ == "__main__":

    root = TrieNode('$')
    addWord(root, "habkathon")
    addWord(root, "hackathon1234")
    addWord(root, "hackathonasdfg")

    possible_words = []
    find_possible_words(root, 'ha?k', possible_words, '')

    print(possible_words)