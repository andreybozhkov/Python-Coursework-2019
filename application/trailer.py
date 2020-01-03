import math

def roundDown(n, decimals = 0):
    multiplier = pow(10, decimals)
    return math.floor(n * multiplier) / multiplier

class Trailer:
    def __init__(self, plateNr):
        self.plateNr = plateNr
        self.ldm = 0
        self.ldmLimit = 13.6
        self.weight = 0
        self.weightLimit = 25160
        self.collis = []
    
    def addColli(self, colli):
        if (self.ldm + colli.ldm > self.ldmLimit):
            print('Cannot add current colli to trailer. Exceeds LDM limit. Adding new trailer.')
            return 0
        elif (self.weight + colli.weight > self.weightLimit):
            print('Cannot add current colli to trailer. Exceeds weight limit. Adding new trailer.')
            return 0
        else:
            self.collis.append(colli)
            self.ldm += colli.ldm
            self.weight += colli.weight
            return 1
        
    def printCollis(self):
        print(f'Trailer {self.plateNr} details:')
        print(f'Loaded with {len(self.collis)} collis.')
        print(f'Loaded with {self.ldm} ldm. Remaining: {roundDown(self.ldmLimit - self.ldm, 1)} ldm.')
        print(f'Loaded with {self.weight} kg. Remaining: {roundDown(self.weightLimit - self.weight, 1)} kg. \n')