from colli import Colli
from trailer import Trailer

def getInputFromUser(prop):
    inputFromUser = input(f'Enter {prop}: ')
    if inputFromUser == 'end':
        return 'end'
    
    try:
        value = float(inputFromUser)
    except ValueError:
        print('Input is not a number (integer or float)! Please try again.')
        value = getInputFromUser(prop)

    return value

def makeTempColli():
    tempColli = {
        'length': 0,
        'width': 0,
        'height': 0,
        'weight': 0
    }
    colliProperties = ['length', 'width', 'height', 'weight']

    for prop in colliProperties:
        value = getInputFromUser(prop)
        if value == 'end':
            raise Exception
        tempColli[prop] = value

    return tempColli

def makeNewColli(tempColli):
    newColli = Colli(tempColli['length'], tempColli['width'], tempColli['height'], tempColli['weight'])
    newColli.calcCBM()
    newColli.calcLDM()
    return newColli

def checkForCollis(collis):
    if len(collis) < 1:
        print('There are no collis. In order to continue, please restart and enter data for at least 1 colli.')
        print('Thank you! Goodbye! :)')
    raise SystemExit

collieSequenceNr = 1
collis = []

while True:
    print(f'Enter dimensions and weight (number integer or float) for colli nr {collieSequenceNr}. If you wish to stop, type "end" instead and hit enter.')

    try:
        tempColli = makeTempColli()
    except Exception:
        break

    collis.append(makeNewColli(tempColli))
    collieSequenceNr += 1

checkForCollis(collis)

trailerSequenceNr = 100
trailers = []