#Entry program for ride 🎢

height = int(input('Enter your height(cm): '))
credits = int(input('Enter amount of credits on hand: '))

if height>=137 and credits>=10:
    print('Enjoy the ride!')
elif height<137 and credits>=10:
    print('Sorry, you\'re not tall enough to ride.')
elif height>=137 and credits<10:
    print('Sorry, not enough credits')
else:
    print('Sorry, you\'re not tall enough and do not have enough credits')
    