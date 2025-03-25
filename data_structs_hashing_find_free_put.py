from operator import index
from turtledemo.penrose import start


class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'


class HashTable():
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0

    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        #return len(key) % self.size
        return sum((index+1) * ord(char) * ord(char) for index, char in enumerate(key)) % self.size


    # function _find_free_slot accepting a parameter representing a position on the heap (an index) and returns the index
    # of the next free slot available in the hash table.
    # after reaching the end of the table function continue from the very beginning of the table till the start position
    # return None if nothing being found
    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.

        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        current_position = start
        if start == None:
            return start
        else:
            while self.slots[current_position]:
                current_position = (current_position + 1) % self.size
                if current_position == start:
                    return None
            return current_position

    def _find_key(self, start, key):
        """
        Starting from 'start' try to find 'key'.

        Parameters:
        - 'start': Starting index
        - 'key': The key to be found

        Returns: The index position of the key or None if not found
        """
        # Start to search from the given position
        current = start

        # While current position is occupied and it's not the key, enter the loop
        while self.slots[current] and self.slots[current].key != key:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size
            # If we reach again the given position, that means
            # a whole cycle has been completed and the key was not found
            if current == start:
                return None

        # After the loop, current points to a free position or
        # to the position with the key
        if self.slots[current]:
            return current
        else:
            return None

    def put(self, key, value):
        """
        Add or updates a key with a value in the hash table

        Parameters:
        - 'key': The key to add or update.
        - 'value': The value of the key

        Returns: None
        """
        if self.used_slots == self.size: return MemoryError

        k = self._hash(key)
        key_to_find = self._find_key(k, key)
        #index = 0
        if key_to_find is not None:
            self.slots[key_to_find].value = value
        else:
            key_to_find = self._find_free_slot(k)
            self.slots[key_to_find] = HashItem(key, value)
            self.used_slots +=1

    def get(self, key, alternative=None):
        """
        Get the value of 'key'.

        Parameters:
        - 'key': The key to find
        - 'alternative': An alternative value if key is not found.
                         Optional. Default value=None

        Returns: The value of 'key' or alternative value
        """
        k = self._hash(key)
        key_to_find = self._find_key(k, key)
        #print(key_to_find)
        if key_to_find is not None:
            if self.slots[key_to_find].key == key:
                return (self.slots[key_to_find].value)
        else:
            return (alternative)

# main to test out ._find_free_slot function
'''def main():
    h = HashTable()

    for c in "abcdefghijklmnopqrstuvwxyz":
        h.slots[(ord(c) * ord(c)) % h.size] = c

    print(h._find_free_slot(0))
    print(h._find_free_slot(1))
    print(h._find_free_slot(10))
main()'''

# main to test out .put function
'''def main():
    h = HashTable()
    h.put("Name", "HashTable")
    print(h.slots[229])
main()'''

#main to test out  .get() function
'''def main():
    h = HashTable()
    h.put('Name', 'HashTable')
    print(h.get('Name'))
main()'''

'''def main():
    h = HashTable()

    s = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(s) - 1, 2):
        h.put(s[i:i + 2], s[i:i + 2])

    for i in range(1, len(s) - 2, 2):
        h.put(s[i:i + 2], s[i:i + 2])

    print(h.get('ab'))
    print(h.get('st'))
    print(h.get('zz', 'Nothing'))
    print(h.get('e', 'Nothing'))
main()'''
