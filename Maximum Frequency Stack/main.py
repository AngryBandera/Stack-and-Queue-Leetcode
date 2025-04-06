from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.dict[val] += 1
        self.max

    def pop(self) -> int:
        freq = 0
        freq_count = 0
        for key in self.dict.keys():
            if self.dict[key] > freq_count:

                freq = key
                freq_count = self.dict[key]
                print(key)
                print(self.dict)
        self.dict[freq] -= 1
        return freq
                
