import random

class Algorithm():
    def __init__(self, seed):
        self.index= 0
        self.array = list(range(1, 51))
        self.comparisons = 0
        self.complete = False
        random.seed(seed)

class SearchAlgorithm(Algorithm):
    def __init__(self, seed):
        super().__init__(seed)
        self.search_val = 1
        while ((self.search_val == 1) or (self.search_val == 50)):
            self.search_val = random.choice(self.array)

class SortAlgorithm():
    def __init__(self, seed):
        super().__init__(seed)
        random.shuffle(self.array)
        self.index_1
        self.index_2

class LinearSearch(SearchAlgorithm):
    """Standard linear search algorithm"""
    def __init__(self, seed):
        super().__init__(seed)
        random.shuffle(self.array)
    
    def step(self):
        self.comparisons += 1
        if self.array[self.index] == self.search_val:
            self.complete = True
        else:
            self.index += 1

class BinarySearch(SearchAlgorithm):
    """Standard binary search algorithm"""
    def __init__(self, seed):
        super().__init__(seed)
        self.lower_index = 0
        self.upper_index = len(self.array) - 1
        self.index = self.lower_index + (self.upper_index - self.lower_index) // 2
    
    def step(self):
        self.comparisons += 1
        if self.array[self.index] == self.search_val:
            self.complete = True
        else:
            if self.search_val <= self.array[self.index]:
                self.upper_index = self.index - 1
            else:
                self.lower_index = self.index + 1
            self.comparisons += 1
            self.index = self.lower_index + (self.upper_index - self.lower_index) // 2