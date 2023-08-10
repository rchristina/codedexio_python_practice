#Sorting hat quiz 🧙🏽

#Houses
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print('Q1) Do you like Dawn or Dusk?')
print('1) Dawn \n2)Dusk')
answer = int(input())

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Wrong Input')

print('Q2) When I\'m dead, I want people to remember me as:')
print('1) The Good\n2) The Great\n3) The Wise\n4) The Bold')
answer = int(input())

if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print('Wrong Input')

print('Q3) Which kind of instrument most pleases your ears?')
print('1) Violin\n2) Trumpet\n3) Piano\n4) Drums')
answer = int(input())

if answer == 1:
    slytherin += 4
if answer == 2:
    hufflepuff += 4
if answer == 3:
    ravenclaw += 4
if answer == 4:
    gryffindor += 4

#print('gryffindor:' + str(gryffindor) + ' ravenclaw:' + str(ravenclaw) + ' hufflepuff:' + str(hufflepuff) + ' slytherin:' + str(slytherin))

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
