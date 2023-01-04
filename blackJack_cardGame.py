import random

# show the result
def show_result(user_hand, dealer_hand_show,user_total):
    print(f"user hand : {user_hand} , your score {user_total} ")
    print(f"computer first hand {dealer_hand_show}")
#  update the ace value
def aceCondition(hand):
        for i in hand:
            if i == 11 :
                i = 1

def blackJack(total) :
    if total == 21 :
        return True

def check_user_brust(user_total) :
    if user_total >21 :
        print("you lose")
        winner= 1
def add_card(user_hand,user_total,deck):
    adding_card = random.choice(deck)
    user_hand = user_hand.append(adding_card)
    user_total += adding_card
    # check if the user total gose over 21 for the first round
    if user_total > 21:
        # convert the Ace card with 11 value , to Ace card with 1 value so the total gose to total - 10
        aceCondition(user_hand)
    check_user_brust()
    should_add_card = input("you want to add card or pass , 'y' for adding card 'n' for pass").lower()
    if should_add_card == 'n':
        should_hit = False

deck =[11,2,3,4,5,6,7,8,9,10,10,10,10]

user_hand=[]
dealer_hand=[]
should_hit = True

winner = 0
# --------------------------------------------------------------------------------------------------

#  a starting hand for the user with 2 random card
user_total=0
for i in range(0,2):
    user_hand.append(random.choice(deck))
    # add each card for the user total
    user_total+=user_hand[i]
    # check if the user total gose over 21 for the first round
    if user_total>21 :
       # convert the Ace card with 11 value , to Ace card with 1 value so the total gose to total - 10
        aceCondition(user_hand)

# -----------------------------------------------------------------------------------------------------
dealer_total = 0
#  a starting hand for the computer with 2 random card
for i in range(0,2):
    dealer_hand.append(random.choice(deck))
    # add card for the computer total
    dealer_total+=dealer_hand[i]
    # check if the dealer total gose over 21 for the first round
    if dealer_total> 21 :
        # convert the Ace card with 11 value , to Ace card with 1 value so the total gose to total - 10
        aceCondition(dealer_hand)
if (blackJack(dealer_total)):
    print(f"computer win with blackJack score {dealer_hand}")
    # dealer win
    winner = 1
elif (blackJack(user_total)):
    print(f"you win with blackJack score {user_hand}")
    print(f"computer card {dealer_hand} , dealer_total {dealer_total}")
    # user win
    winner =  2

check_user_brust(user_total=user_total)
# -----------------------------------------------------------------------------------------------------
if (winner == 0):
    # only show the first card of the computer hand
    dealer_hand_show = dealer_hand[0]
    # show the result for the first round
    show_result(user_hand=user_hand,user_total=user_total,dealer_hand_show=dealer_hand_show)
    should_add_card= input("you want to add card or pass , 'y' for adding card 'n' for pass").lower()
    if should_add_card == 'n':
        should_hit=False
while(should_hit):
    add_card(user_hand=user_hand,user_total=user_total,deck=deck)

# -----------------------------------------------------------------------------------------------------


# # check the first win or lose condition , if the user over 21 then they lose
# if (user_total> 21 ):
#     print(f"your total {user_total} brust you lose ")
#     winner=1

# def hit(deck, user_hand):
#     user_hand.append(random.choice(deck))
#     check_in_user(user_hand)
# def check_should_hit(add_card):
#     if should_hit=='y':
#         hit(deck,user_hand)
# def check_in_user(user_hand):
#     if (user_total > 21):
#         print(f"your total {user_total} brust you lose ")
#     elif (user_total == 21 ):
#         print("you win with blackJack score")
#         should_hit=False
#     else:
#         should_hit = print("type 'y' to get another card , type 'n' to pass")
#         check_should_hit(should_hit)
# #  ask the user if they want to add another card
#
#
# should_hit = print("type 'y' to get another card , type 'n' to pass")
#
#
#
# while (should_hit):
#     user_hand.append(random.choice(deck))
#     check_in_user(user_hand)
# hit = print("type 'y' to get another card , type 'n' to pass")
# if hit=='y':
#
#
#




