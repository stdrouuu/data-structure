class HashTable:
    def __init__(self, size = 0):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashVal = self.hashFunc(key, len(self.slots))

        if self.slots[hashVal] == None:
            self.slots[hashVal] = key
            self.data[hashVal] = data
        else: 
            if self.slots[hashVal] == key:
                self.data[hashVal] = data
            else:
                nextSlot = self.rehash(hashVal, len(self.slots))
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))

                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data

    def hashFunc(self, key, size):
        return key % size
        
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size
        
    def get(self, key):
        startSlot = self.hashFunc(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startSlot
        
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startSlot:
                    stop = True
        return data
        
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)

if __name__ == "__main__":
    H = HashTable(11)
    H[54] = "books"
    H[54] = "data"
    H[26] = "algorithms"
    H[93] = "made"
    H[17] = "easy"
    H[77] = "CarrerMonk"
    H[31] = "Jobs"
    H[44] = "Hunting"
    H[55] = "King"
    H[20] = "Lion"
    print(H.slots)
    print(H.data)
    print(H[20])