from colli import Colli

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
        'height': 0
    }
    colliProperties = ['length', 'width', 'height']

    for prop in colliProperties:
        value = getInputFromUser(prop)
        if value == 'end':
            raise Exception
        tempColli[prop] = value

    return tempColli

def makeNewColli(tempColli):
    newColli = Colli(tempColli['length'], tempColli['width'], tempColli['height'])
    newColli.calcCBM()
    newColli.calcLDM()
    return newColli

sequenceNr = 1
collis = []

while True:
    print(f'Enter dimensions (number integer or float) for colli nr {sequenceNr}. If you wish to stop, type "end" instead and hit enter.')

    try:
        tempColli = makeTempColli()
    except Exception:
        print('Thank you! Goodbye! :)')
        break

    collis.append(makeNewColli(tempColli))
    sequenceNr += 1