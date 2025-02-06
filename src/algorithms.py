import random

class Algorithm():
    def __init__(self, seed, array_size = 21):
        self.index = 0
        self.array = list(range(1, array_size))
        self.comparisons = 0
        self.complete = False
        random.seed(seed)

class SearchAlgorithm(Algorithm):
    def __init__(self, seed, array_size = 21):
        super().__init__(seed, array_size)
        self.search_val = random.choice(self.array)

class SortAlgorithm(Algorithm):
    def __init__(self, seed):
        super().__init__(seed)
        random.shuffle(self.array)

class LinearSearch(SearchAlgorithm):
    """Standard linear search algorithm"""
    def __init__(self, seed):
        super().__init__(seed)

        random.shuffle(self.array)
        # if search val is at start of array it can be confusing
        while (self.array.index(self.search_val) <= 5):
            self.search_val = random.choice(self.array)
    
    def step(self):
        self.comparisons += 1
        if self.array[self.index] == self.search_val:
            self.complete = True
        else:
            self.index += 1

class BinarySearch(SearchAlgorithm):
    """Standard binary search algorithm"""
    def __init__(self, seed):
        super().__init__(seed, 51)
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

class BubbleSort(SortAlgorithm):
    """Standard bubble sort algorithm"""
    def __init__(self, seed):
        super().__init__(seed)
        self.swapped = False
        self.completed_passes = 0

    def step(self):
        # perform comparison and swap if necessary
        if self.index < len(self.array) - self.completed_passes - 1:
            self.comparisons += 1
            if self.array[self.index] > self.array[self.index + 1]:
                # swap elements
                self.array[self.index], self.array[self.index + 1] = self.array[self.index + 1], self.array[self.index]
                self.swapped = True
            self.index += 1
        else:
            self.completed_passes += 1
            self.index = 0  # reset index for the new pass

            if not self.swapped:
                self.complete = True
            else:
                self.swapped = False

class InsertionSort(SortAlgorithm):
    """Standard insertion sort algorithm"""
    def __init__(self, seed):
        super().__init__(seed)
        self.index = 1 
        self.key = None
        self.position = 1

    def step(self):
        if self.index < len(self.array):
            self.key = self.array[self.index]  # take the current element as the key
            self.position = self.index - 1

            # shift elements to the right as long as they are greater than the key
            while self.position >= 0 and self.array[self.position] > self.key:
                self.comparisons += 1
                self.array[self.position + 1] = self.array[self.position]
                self.position -= 1

            self.array[self.position + 1] = self.key
            self.comparisons += 1

            self.index += 1
        else:
            self.complete = True

class SelectionSort(SortAlgorithm):
    """Standard selection sort algorithm"""
    def __init__(self, seed):
        super().__init__(seed)
        self.index = 0

    def step(self):
        if self.index < len(self.array) - 1:
            self.comparisons += 1
            index = self.index

            for i in range(self.index + 1, len(self.array)):
                self.comparisons += 1
                if self.array[i] < self.array[index]:
                    index = i
            if index != self.index:
                self.array[self.index], self.array[index] = self.array[index], self.array[self.index]

            self.index += 1
        else:
            self.complete = True
