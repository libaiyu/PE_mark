import random

while(input("input something:")):
    messages = [ 'It is certain', 
             'It is decidedly so',
             'Yes definitely',
             'Repy hazy try again',
             'Ask again later',
             'Concentrate and ask again',
             'My reply is no',
             'Outlook not so good',
             'Vety doubtful']

    print(messages[random.randint(0,len(messages) - 1)])
