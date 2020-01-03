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

sequenceNr = 1
continueInput = True

while continueInput:
    print(f'Enter dimensions (number integer or float) for colli nr {sequenceNr}. If you wish to stop, type "end" instead and hit enter.')
    colliProperties = ['length', 'width', 'height']
    tempColli = {
        'length': 0,
        'width': 0,
        'height': 0
    }
    for prop in colliProperties:
        value = getInputFromUser(prop)
        if value == 'end':
            continueInput = False
            break
        print(value)