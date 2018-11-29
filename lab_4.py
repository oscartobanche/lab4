#Oscar Tobanche
#Prof. Diego Aguirre
#manoj saha
#CS 2302
#this code implements a binary search tree of words.
class HashTableNode:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class HashTable:

    def __init__(self, table_size):
        self.table = [None] * table_size

    def hash(self, k):
        return k % len(self.table)
    def no_duplicates_insert(self, k):
        loc = self.hash(k)

        temp = self.table[loc]

        while temp is not None:
            if temp.item == k:
                return

            temp = temp.next

        self.table[loc] = HashTableNode(k, self.table[loc])
    def insert(self, k):
        loc = self.hash(k)
        self.table[loc] = HashTableNode(k, self.table[loc])
    def search(self, k):
        loc = self.hash(k)

        temp = self.table[loc]

        while temp is not None:
            if temp.item == k:
                return temp

            temp = temp.next

        return None


    def load_factor(self):
        count = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            while temp is not None:
                count += 1
                temp = temp.next
        load = count // len(self.table)
        print("the load factor is:" + load)
chaining = HashTable()

with open('glove.6B.50d.txt','r') as file:
    for line in file:
        chaining[load_factor] = HashTableNode(line)

