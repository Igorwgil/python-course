'''Write a program to calculate the reduction in a smoker's lifespan. Ask for the number of cigarettes smoked per day and how many years the person has been smoking. Consider that a smoker loses 10 minutes of life for each cigarette. Calculate how many days of life the smoker will lose and display the total in days. '''

numberCigarettes = int(input('How many cigarettes do you smoke per day? '))
yearsSmoking = int(input
('How many years do you smoke? '))

totalCigarettes =(numberCigarettes * 365) * yearsSmoking

minutesLost = totalCigarettes * 10

daysLost = minutesLost / 60 / 24

print('You lost', round(daysLost, 2), 'of your life')