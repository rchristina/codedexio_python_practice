#Magic 8 Ball 🎱

import random

input('Question for 8 Ball: ')

#random answer
response = random.randint(1,9)

#replace with function/dict later
if response == 1:
    print('Magic 8 Ball: Yes - defintely')
if response == 2:
    print('Magic 8 Ball: It is decidely so')
if response == 3:
    print('Magic 8 Ball: Without a doubt')
if response == 4:
    print('Magic 8 Ball: Reply hazy, try again')
if response == 5:
    print('Magic 8 Ball: Ask again later')
if response == 6:
    print('Magic 8 Ball: Better not tell you now')
if response == 7:
    print('Magic 8 Ball: My sources say no')
if response == 8:
    print('Magic 8 Ball: Outlook not so good')
if response == 9:
    print('Magic 8 Ball: Very doubtful')