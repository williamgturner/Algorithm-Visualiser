
import random

class linear_search():
    def __init__(self):
        self.index= 0
        self.array = []
        self.complete = False
        for i in range(20):
            self.array.append(i)
        random.seed(1)
        random.shuffle(self.array)
        self.search_val = random.choice(self.array)
    
    def step(self):
        if self.array[self.index] == self.search_val:
            self.complete = True
            return True
        else:
            self.index += 1
            self.complete = False
            return False


