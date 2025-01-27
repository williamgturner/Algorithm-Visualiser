
import random

class linear_search():
    def __init__(self, seed):
        self.index= 0
        self.array = list(range(1, 21))
        self.complete = False
        random.seed(seed)
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