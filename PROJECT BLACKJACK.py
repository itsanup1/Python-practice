import random

card_values = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards=[]
comp_cards=[]
win_status= False
def deal_cards():#Card dealing
        for _ in range(2):
            dealt = random.choice(card_values)
            user_cards.append(dealt)
            comp_cards.append(dealt)
deal_cards() 

print(user_cards) #user card print

def score():#Score system
       user_score = sum(user_cards)
       if user_score == 21 and len(user_cards) <= 2 :
           return 0      
       if sum(comp_cards) == 21 and len(comp_cards) <= 2 :
           return 1
       return user_score 
diddy = score()
def finale_sys(): #win or lose
     if score()>21:
         pass
         
     else:
         win_status=True
     return win_status

def draw_card():#drawing card sys
    user_cards.append(random.choice(card_values))
            
score()
print(score())
print(finale_sys())

if diddy < 21 :
        draw = input("Do you want to draw a card ? (y/n) ")
        if draw == 'y':        
            draw_card()
else:
            finale_sys()      
            
                    