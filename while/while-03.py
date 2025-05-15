import os

def cleam_scream():
    os.system('cls')

cleam_scream()

while True:
    try:
        number = int(input('Write any number or [000] to close the system: '))
    except ValueError:
        print('Invalid value. Just numbers')
    if number == 000:
        break