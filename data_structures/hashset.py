from array import array

class HashSet(object):
    
    @staticmethod
    def _default_hash(n):
        h = 3
        for c in str(n):
            h = h * 31 + ord(c)
        return h

    def __init__(self, hash_function=None, size=10000):
        self._hash_function = self._default_hash if hash_function == None else hash_function
        self.size = size
        self._array = array('I', (0,) * self.size)

    def add(self, n):
        o = i = self._hash_function(n) % self.size
        while self._array[i] != 0:
            if i == (self.size - 1):
                i = 0
            elif i == (o - 1):
                if self._array[o - 1] != 0:
                    raise Exception("HashTable full")
                else:
                    self._array[o - 1] = n
                    break
            else:
                i += 1
        self._array[i] = n

    def contains(self, n):
        i = o = self._hash_function(n) % self.size
        while self._array[i] != n:
            if i == (self.size - 1):
                i = 0
            elif i == (o - 1):
                return self._array[o - 1] == n
            elif self._array[i] == 0:
                return False
            else:
                i += 1
        return True

    def remove(self, n):
        if self.contains(n):
            i = self._hash_function(n) % self.size
            while self._array[i] != n:
                i = 0 if i == (self.size - 1) else i + 1
            self._array[i] = 0
    