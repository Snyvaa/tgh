import random
from IPython.display import clear_output
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':10}
class Value:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
class Deck:
    def __init__(self):
        self.deck = []
        for a in suits:
            for b in ranks:
                self.deck.append(Value(a,b))
class Player(Value):
    def __init__(self, name):
        self.name = name
        self.cards_value_count = 0
        self.wins = 0
        self.loses = 0
        self.busts = 0
        self.money = 50000
class Bot(Value):
    def __init__(self):
        self.deck = []
    def totally_not_rigged(self):
        bot.deck.append(new_deck.deck[random.randint(0,len(new_deck.deck)-1)])
        new_deck.deck.remove(bot.deck[-1])   
game = True
new_deck = Deck()
player_one = Player("One")
bot = Bot()
count = 0
player_one_deck = []
while game:
    while True:
        try:
            bet_amount = int(input('bet amount: '))
            if bet_amount > player_one.money:
                print('Not enough money brokie')
                continue
            elif bet_amount <= 0:
                print('wtf this is not even demo')
                continue
        except:
            print('Put in numbers not something else')
            continue
        else:
            break
    for i in range(2):
        player_one_deck.append(new_deck.deck[random.randint(0,len(new_deck.deck)-1)])
        new_deck.deck.remove(player_one_deck[-1])
        player_one.cards_value_count += player_one_deck[-1].value
        print(f'{player_one_deck[-1].rank} of {player_one_deck[-1].suit}')
        bot.deck.append(new_deck.deck[random.randint(0,len(new_deck.deck)-1)])
        new_deck.deck.remove(bot.deck[-1])
        count = bot.deck[-1].value + count
    for i in range(len(player_one_deck)):
        while True:
            if player_one_deck[i].rank == 'Ace':
                try:
                    print(f'Total: {player_one.cards_value_count}')
                    a = int(input('Do u want to add 1 or 10 from your Ace (currently 10): '))
                    if a == 1:
                        player_one.cards_value_count = player_one.cards_value_count - 9
                        break
                    elif a == 10:
                        break
                except ValueError:
                    print('Huh')
                    continue
            else:
                break
    print(f'Total: {player_one.cards_value_count}')
    while True:
        k = input('DO U WANT TO HIT OR STAND: ')
        if k.lower() == 'hit':
            clear_output()
            player_one_deck.append(new_deck.deck[random.randint(0,len(new_deck.deck)-1)])
            new_deck.deck.remove(player_one_deck[-1])
            player_one.cards_value_count += player_one_deck[-1].value
            print(f'{player_one_deck[-1].rank} of {player_one_deck[-1].suit}')
            print(f'Total: {player_one.cards_value_count}')
            if player_one.cards_value_count > 21:
                player_one.money = player_one.money - bet_amount
                print(f'YOU BUSTED {bet_amount}')
                player_one.busts += 1
                break
        elif k.lower() == 'stand':
            clear_output()
            while True:
                if count <= 16:
                    bot.deck.append(new_deck.deck[random.randint(0,len(new_deck.deck)-1)])
                    new_deck.deck.remove(bot.deck[-1])
                    count = bot.deck[-1].value + count
                    continue
                else:
                    break
            break
        else:
            print('HUH?')
            continue
    if player_one_deck[0].rank == 'Ace' and player_one_deck[1].rank == 'Ace':
        print('BLACKJACK')
        player_one.wins += 1
    elif 21 >= player_one.cards_value_count > count:
        player_one.money = player_one.money + bet_amount
        for i in range(len(bot.deck)):
            print(f'{bot.deck[i].rank} of {bot.deck[i].suit}')
        print(f'Bot deck: {count}')
        print(f'YOU WON {bet_amount}')
        player_one.wins += 1
    elif 21 >= count >= player_one.cards_value_count:
        player_one.money = player_one.money - bet_amount
        for i in range(len(bot.deck)):
            print(f'{bot.deck[i].rank} of {bot.deck[i].suit}')
        print(f'Bot deck: {count}')
        print(f'YOU LOST {bet_amount}')
        player_one.loses += 1
    elif count > 21:
        player_one.money = player_one.money + bet_amount
        for i in range(len(bot.deck)):
            print(f'{bot.deck[i].rank} of {bot.deck[i].suit}')
        print(f'Bot deck: {count}')
        print(f'YOU WON {bet_amount}')
        player_one.wins += 1
    elif count == player_one.cards_value_count:
        for i in range(len(bot.deck)):
            print(f'{bot.deck[i].rank} of {bot.deck[i].suit}')
        print(f'Bot deck: {count}')
        print(f'YOU LOST {bet_amount}')
        player_one.money = player_one.money - bet_amount
        player_one.loses += 1
    print(f"Money: {player_one.money}\nWins: {player_one.wins}\nLoses: {player_one.loses}\nBusted: {player_one.busts}")  
    gambling_more = str(input('Do you want to continue Y-N: '))
    while True:
        if gambling_more.lower() == 'y':
            player_one_deck = []
            count = 0
            bot.deck = []
            player_one.cards_value_count = 0
            clear_output()
            break
        elif gambling_more.lower() == 'n':
            game = False
            break
        elif player_one.money <= 0 and gambling_more.lower() == 'y':
            print('you literally bankrupt')
            break
        else:
            clear_output()
            print('HUH?')
            gambling_more = input("Do you want to continue Y-N: ")  # Ask for input again
            continue