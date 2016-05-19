class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            #FIFO if False set else LIFO
            self.cache.popitem(last=False)
        self.cache[key] = value



# second round: double linked list and dictionary
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.tail.prev = self.head
        self.head.next = self.tail

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.map:
            return -1    
        cur = self.map.get(key)
        # build two dummy prev, next node to avoid edge case
        prev = cur.prev
        next = cur.next
        prev.next = next
        next.prev = prev
        self.move_to_tail(cur)
        return cur.value
        
        
    def move_to_tail(self, cur):
        # two side
        cur.prev = self.tail.prev
        self.tail.prev = cur
        cur.prev.next = cur
        cur.next = self.tail
        
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.get(key) != -1:
            self.map[key].value = value
            return
        
        if len(self.map) == self.capacity:
            self.map.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        
        newNode = Node(key, value)
        self.map[key] = newNode
        self.move_to_tail(newNode)
        
        
        
