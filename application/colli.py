import math

def roundUp(n, decimals = 0):
    multiplier = pow(10, decimals)
    return math.ceil(n * multiplier) / multiplier

class Colli:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.cbm = 0
        self.ldm = 0

    def calcCBM(self):
        cbm = self.length * self.width * self.height
        self.cbm = roundUp(cbm, 2)

    def calcLDM(self):
        ldm = (self.length * self.width) / 2.4
        self.ldm = roundUp(ldm, 1)