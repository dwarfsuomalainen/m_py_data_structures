from data_structs_stacks_push_pop_methods import Stack


class StackBasedQueue():
    def __init__(self):

        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        self._size = 0

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        self._InboundStack.push(data)
        self._size += 1

    def dequeue(self):
        if self._OutboundStack.__len__() == 0:
            while self._InboundStack.__len__() != 0:
                pop = self._InboundStack.pop()
                self._OutboundStack.push(pop)
        if self._OutboundStack.__len__() == 0: return None

        self._size -= 1
        return self._OutboundStack.pop()



def main():
    #queue = StackBasedQueue()
    '''queue = StackBasedQueue()
    queue.enqueue('A')
    print(queue)'''

    queue = StackBasedQueue()
    queue.enqueue('A')
    print(queue)
    queue.enqueue('B')
    print(queue)
    queue.enqueue('C')
    print(queue)
    val = queue.dequeue()
    print(val, queue)

    '''	
queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
val = queue.dequeue()
val = queue.dequeue()
val = queue.dequeue()
val = queue.dequeue()
print(val, queue)'''

'''	
queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
val = queue.dequeue()
val = queue.dequeue()
val = queue.dequeue()
print(val, queue)'''

'''	
queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
val = queue.dequeue()
val = queue.dequeue()
print(val, queue)'''

'''	
queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
val = queue.dequeue()
print(val, queue)'''

'''	
queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print(queue)'''
main()