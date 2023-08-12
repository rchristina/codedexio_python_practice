print('Bank of Codedex')

pin = int(input('Enter your PIN: '))

while pin != 1234:
    pin = int(input('Incorrect PIN. Enter your pin again: '))

if pin == 1234:
    print('PIN accepted!')