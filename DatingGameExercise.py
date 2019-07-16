import time
result = ''
while True:
    print('CHAPTER ONE')
    print('You are Ollie, a likeable young guy in search '
        'of love. Our story begins when Ollie comes across'
        ' an attractive young woman on Tinder...')

    swipe = ''
    while swipe != '1' and swipe != '2':
        swipe = input('Will you swipe left or right? (1) Right, (2) Left ')
    # Loops until correct input
    if swipe == '2':
        result = "Hmm, perhaps Ollie's standards are a little high... GAME OVER"
        break
    # else continue
    time.sleep(0.5)

    print('\n CHAPTER TWO')
    print('She messages you and asks for a date! But she wants you to pick the type of restaurant')
    choice = ''
    while choice != '1' and choice != '2' and choice != '3':
        choice = input('What kind of food will you choose?: (1)Italian (2)Curry (3)Pub grub')
    # loops until correct input
    if choice == '1':
        print('Ah, molto bella!')
    elif choice == '2':
        result = 'Curry on a first date!? What were you thinking? GAME OVER'
        break
    else:
        print('Lovely jubbly.')
    time.sleep(0.5)

    print('\n CHAPTER THREE')
    print('You meet at the restaurant and after an hour, everything seems to be going fine! '
          'However, you notice your date might have had a bit much to drink...')
    judgement = ''
    while 't' not in judgement and 'f' not in judgement:
        judgement = input(' what do you think? (Enter true or false)').lower()
    print("Whatever you say! Oh no, now she's asking how old you think she is! "
          "Maybe she's had too much drink to really notice what you say...")
    age = input('What age will you say?')
    if age.isnumeric() == 0:
        result = "There's no talking your way out of this one! GAME OVER"
        break
    if int(age) < 30 or 't' in judgement:
        print("She smiles and shrugs. 'I'll never tell!' Phew, that was a close one!")
    else:
        result = "Uh, I think you might have miscalculated somewhere... GAME OVER"
        break
    time.sleep(0.5)

    print('\n CHAPTER FOUR')
    print('The rest of the evening goes wonderfully and soon, the bill arrives. Yikes! £100!?')
    choice = ''
    while choice != '1' and choice != '2':
        choice = input('What will you do?: (1)Say you left your wallet at home. (2)Offer to pay')
    money = input('Wait... how much money do you actually have?')
    if money.isnumeric() == 0:
        result = "I don't think you can pay with that! GAME OVER"
        break
    if choice == '2' and int(money) >= 100:
        result = 'How very gallant of you! She seems impressed... YOU WIN!'
        break
    else:
        result = "Sorry, nobody likes a cheapskate."
    time.sleep(0.5)
print(result)

