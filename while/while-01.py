import os

def cleam_scream():
    os.system('cls' if os.name == 'nt' else 'clear')

cleam_scream()

x = 6

while x < 16:
    print(x)

    x += 1

print('Finished')