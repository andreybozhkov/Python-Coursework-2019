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
            print('Cannot add current colli to trailer. Exceeds LDM limit.')
            return 0
        elif (self.weight + colli.weight > self.weightLimit):
            print('Cannot add current colli to trailer. Exceeds weight limit.')
            return 0
        else:
            self.collis.append(colli)
            self.ldm += colli.ldm
            self.weight += colli.weight
            return 1