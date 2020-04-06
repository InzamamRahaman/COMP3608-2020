import heapq

class Queue(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def enqueue(self, item):
        self.append(item)
        
    def dequeue(self):
        return self.pop(0)
        
class Stack(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def push(self, item):
        self.append(item)
    
    def pop(self):
        return super().pop(-1)
        
    

class PriorityQueue(dict):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._heapify()
    
    def _heapify(self):
        self._contents = [(priority, item) for item, priority in self.items()]
        heapq.heapify(self._contents)
        
    def pop(self):
        priority, item = heapq.heappop(self._contents)
        del self[item]
        return priority, item
    
    def __setitem__(self, item, priority):
        super().__setitem__(item, priority)
        self._heapify()
        
    def __getitem__(self, item):
        return self[item]
    
    def push(self, priority, item):
        self[item] = priority
        