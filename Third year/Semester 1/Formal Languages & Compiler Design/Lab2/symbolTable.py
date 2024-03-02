class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = []
        for index in range(size):
            self.table.append([])

    def getSize(self):
        return self.size

    def __hash(self, key):
        sum = 0
        for char in str(key):
            sum += ord(char.lower())
        hash_value = sum % self.size
        return hash_value, self.table[hash_value]

    def add(self, key):
        hashValue, index = self.__hash(key)
        if key not in index:
            index.append(key)

    def remove(self, key):
        hash_value, index = self.__hash(key)
        if key in index:
            index.remove(key)

    def contains(self, key):
        hashValue, index = self.__hash(key)
        return key in index

    def getIndex(self, value):
        hashValue, index = self.__hash(value)
        if value in index:
            return index.index(value)
        else:
            return -1

    def __str__(self):
        string = ""
        hashValue = 0
        for i in self.table:
            for keyword in i:
                string = string + "(" + str(hashValue) + "," + str(self.getIndex(keyword)) + ") : " + str(keyword) + "\n"
            hashValue += 1
            string = string + "\n"

        return string
