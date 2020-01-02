import colli

continueLoop = True
sequenceNr = 1

while True:
    print(f'Enter dimensions (numbers) for colli nr {sequenceNr}. If you wish to stop at any point, type "end" and hit enter.')
    colliProperties = ['length', 'width', 'height']
    for prop in colliProperties:
        inputFromUser = input(f'Enter {prop}: ')
        try:
            value = float(inputFromUser)
        except ValueError:
            print('Input is not a number (integer or float)! Please try again.')
    break