
"""Slot Games
This is a simple slot game. Increase the number of coins you hold at the start of the game.
This code makes Reel run 1 milion times just in a few dozen seconds depending on your system.
When a pattern is matched, you will win coins at a payout multiplier corresponding to the pattern.
Good Luck!
"""


import random   


REEL_MARK_LIST = ('7', 'BAR', '🍒', '🍎', 'Reply','♢','♢', 'Reply', '🍎','Reply','♢','Reply','🍎')


game_count=int(0)
count_cherry=int(0)


def show_start_message():
    print('--------------')
    print('Exciting Slot Game')
    print('--------------')

def ask_player_name():
    player_name = input('AI ')

def ask_bets(player_coin):
    print('------------------------------')
    bets = int(1)
    return bets

def show_and_get_result():
    
    result_list = []
    for _ in range(3):
        index = random.randint(0, 12)
        result = REEL_MARK_LIST[index]
        result_list.append(result)
    result_all = ''.join(result_list)
    print(result_all)
    return result_all

def get_division(marks):
    """
    Dividends List
    """
    
    if marks == '777':
        print('Jackpot！！120 Coins')
        return 120
    elif marks == 'BARBARBAR':
        print('BAR！30 Coins')
        return 30
    elif marks == '🍎🍎🍎':
        print('Apple！Coins')
        return 8
    elif marks == 'ReplyReplyReply':
        print('Reply！')
        return 1
    elif marks[0:1] == '🍒':
        print('Cerry 3 Coins')
        return 3
    else:
        print('You Lose')
        return -1

def calculate_coin(coin, bets, division):
    """
    Calculation
    """
    coin = coin + bets * division
    return coin


player_coin = int(1000000)
count_777=int(0)
count_BAR=int(0)
# show_start_message()
# player_name = ask_player_name()

# if player_name in BONUS_PLAYER_AND_COINS:
#    player_coin = player_coin + BONUS_PLAYER_AND_COINS[player_name]
#elif player_name in SPECIAL_THANKS:
#    player_coin = player_coin + SPECIAL_THANKS_COIN

while player_coin > 0:
    bets = ask_bets(player_coin)
    marks = show_and_get_result()
    division = get_division(marks)
    player_coin = calculate_coin(player_coin, bets, division)
    
    if marks=='777':
        count_777=count_777+1 
    elif marks=='BARBARBAR':
        count_BAR=count_BAR+1 
    else:
        print('Run Again ! ')
        
    print('----------------------------------')
    game_count=game_count+1
    print('Total Game number is : '+str(game_count)+'')
    print('----------------------------------')

print('===================')
print('1) You got 777 at '+str(count_777)+' times ! ')
print('2) You got BAR at '+str(count_BAR)+' times ! ')
print('===================')

print('Game Over')
print(f'Good Night ! ')