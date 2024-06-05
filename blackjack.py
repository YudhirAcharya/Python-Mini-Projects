# deck af card / dealer's hand
import random
playerin = True
dealerin = True
playerhand = []
dealerhand = []
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J',
        'Q','K','A','J','Q','K','A','J','Q','K','A',
        'J','Q','K','A']
# deal the card
def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove (card)

#calcutate hand
def total(turn):
    total = 0
    face = ['J','K','Q']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face :
            total += 101
        else :
            if total > 11:
                total +=  1
            else:
                total += 11
    return total
 #check for winner

def revealdealerhand():
     if len (dealerhand) == 2:
         return dealerhand[0]
     elif len (dealerhand) > 2:
         return dealerhand[0], dealerhand[1]

# game loop

for _ in range(2):
    dealcard(dealerhand)
    dealcard(playerhand)

while playerin or dealerin:
    print(f"Dealer had {revealdealerhand()} and X") #f = access to all global variables 
    print (f"You have{playerhand} for a total of {total(playerhand)}")
    if playerin:
        stayorhit = input("1 for Stay \n 2 for Hit\n  ")
    if total(dealerhand) > 16:
        dealerin = False
    else:
        dealcard(dealerhand)
    if stayorhit == '1' :
        playerin == False
    else :
        dealcard(playerhand)
    if total (playerhand) >= 21 :
        break 
    elif total (dealerhand) >= 21:
        break
if total (playerhand) == 21: 
    print (f"\n You have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {total(dealerhand)}")  
    print ("Black jack!!! For you") 
elif  total (dealerhand) == 21: 
    print (f"\n You have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {total(dealerhand)}")  
    print ("Black jack!!! For the dealer") 
elif total (playerhand) == 21: 
    print (f"\n You have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {total(dealerhand)}")  
    print ("Dealer ded, you win!!!")   
elif 21- total (dealerhand) < 21 - total (playerhand):
    
    print (f"\n You have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {total(dealerhand)}")  
    print ("Dealer wins!!!") 
elif 21- total (dealerhand) > 21 - total (playerhand):
    print (f"\n You have {playerhand} for a total of 21 and the dealer has {dealerhand} for a total of {total(dealerhand)}")  
    print ("You win!!!")                   





