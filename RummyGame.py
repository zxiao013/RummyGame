import random

# Read and understand the docstrings of all of the functions in detail.


def make_deck(num):
    '''(int)->list of int
        Returns a list of integers representing the strange deck with num ranks.

    >>> deck=make_deck(13)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413]

    >>> deck=make_deck(4)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    
    '''
    deck=[]
    for i in range(1,5):
         for num in range(1,num+1):
           card=((i*100)+num)
           deck+=[card]
    return deck                

def shuffle_deck(deck):
    '''(list of int)->None
       Shuffles the given list of strings representing the playing deck

    Here you should use random.shuffle function from random module.
    
    Since shufflling is random, exceptionally in this function
    your output does not need to match that show in examples below:

    >>> deck=[101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    >>> shuffle_deck(deck)
    >>> deck
    [102, 101, 302, 104, 304, 103, 301, 403, 401, 404, 203, 204, 303, 202, 402, 201]
    >>> shuffle_deck(deck)
    >>> deck
    [402, 302, 303, 102, 104, 103, 203, 301, 401, 403, 204, 101, 304, 201, 404, 202]
    '''
    deck2=[]
    for j in range (0,len(make_deck(num))):
        numbe = random.randint(0,len(make_deck(num))-1)
        n=make_deck(num)[numbe]
        deck2+=[n]
        del make_deck(num)[numbe]
    return deck2

        

def deal_cards_start(deck):
     '''(list of int)-> list of int

     Returns a list representing the player's starting hand.
     It is  obtained by dealing the first 7 cards from the top of the deck.
     Precondition: len(dec)>=7
     '''
     if len(deck)>=7:
         player=[]
         for k in range(len(deck)-8,len(deck)-1):
             c=deck[k]
             player+=[c]
     return player 
         


def deal_new_cards(deck, player, num):
    '''(list of int, list of int, int)-> None
    Given the remaining deck, current player's hand and an integer num,
    the function deals num cards to the player from the top of the deck.
    If  the number  of cards in the deck is less than num then then all the remaining cards are from the deck.
    Precondition: 1<=num<=6l deck and player are disjoint subsets of the strange deck. 
    
    >>> deck=[201, 303, 210, 407, 213, 313]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 313, 213, 407, 210]
    >>> deck
    [201, 303]
    >>>

    >>> deck=[201, 303]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 303, 201]
    >>> deck
    []
    '''
    if len(deck)<=num:
        for h in range (0,len(deck)-1):
            d=deck[h]
            player+=[d]
    if len(deck)>num:
         for h in range(len(deck)-num-1,len(deck)-1):
             d=deck[h]
             player+=[d]
    return player
    
             
             
def print_deck_twice(hand):
    '''(list)->None
    Prints elements of a given list deck in two useful ways.
    First way: sorted by suit and then rank.
    Second way: sorted by rank.
    Precondition: hand is a subset of the strange deck.
    
    Your function should not change the order of elements in list hand.
    You should first make a copy of the list and then call sorting functions/methods.

    Example run:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_deck_twice(a)

    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410 

    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313 
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''
    if len(hand)==0:
        print()
        print()
    else:
        def rank(e):
            e=str(e)
            return int(e[1:3])
        hand.sort(key=rank)
        print(sorted(hand,key=rank))
        print(hand)
     

        


def is_valid(cards, player):
    '''(list of int, list of int)->bool
    Function returns True if every card in cards is the player's hand.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.

    Precondition: cards and player are subsets of the strange deck.
    
    >>> is_valid([210,310],[201, 201, 210, 302, 311])
    310 not in your hand. Invalid input
    False

    >>> is_valid([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''
    for i in cards:
        if i in player:
            return True
        else:
            return False
   
            

def is_discardable_kind(cards):
    '''(list of int)->True
    Function returns True if cards form 2-, 3- or 4- of a kind of the strange deck.
    Otherwise it returns False. If there  is not enough cards for a meld it also prints  a message about it,
    as illustrated in the followinng example runs.
    
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.
    
    >>> is_discardable_kind([207, 107, 407])
    True
    >>> is_discardable_kind([207, 107, 405, 305])
    False
    >>> is_discardable_kind([207])
    Invalid input. Discardable set needs to have at least 2 cards.
    False
    '''
    l=[]
    if len(cards)<=1:
        return False
    for i in cards:
        a=i%100
        l+=[a]
    for j in range(0,len(l)-1):
        if l[j]!=l[j+1]:
            return False
    return True    
  


def is_discardable_seq(cards):
    '''(list of int)->True
    Function returns True if cards form progression of the strange deck.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.

    >>> is_discardable_seq([313, 311, 312])
    True
    >>> is_discardable_seq([311, 312, 313, 414])
    Invalid sequence. Cards are not of same suit.
    False
    >>> is_discardable_seq([201, 202])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    >>> is_discardable_seq([])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    '''
    cards.sort()
    if len(cards)<=2:
            return False
    for i in range(0,len(cards)-3):
        if cards[i]!=cards[i+1] :
            return False
    return True
    

def rolled_one_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 1
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> rolled_one_round(player)
    Discard any card of your choosing.
    Which card would you like to discard? 103
    103
    No such card in the deck. Try again.
    Which card would you like to discard? 102

    Here is your new hand printed in two ways:

    201 212 311 

    201 311 212 

    '''
    a=int(input("Which card would you like to discard?"))
    if a in player:
        player.remove(a)
        print(player,"Here is your new hand printed in two ways")
        return player
    else:
        print("No such card in the deck. Try again.")
        a=int(input("Which card would you like to discard?"))
        return False
   

       

def rolled_nonone_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 2, 3, 4, 5, or 6.
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 102 103 104
    103 not in your hand. Invalid input
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 403 203

    Here is your new hand printed in two ways:

    102 104 401 

    401 102 104 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 2:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412 413

    Here is your new hand printed in two ways:

    103 211 

    103 211 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 3:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412
    Invalid meld: 11 is not equal to 12
    Invalid sequence. Discardable sequence needs to have at least 3 cards.

    >>> #example 4:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? alsj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? hlakj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? 22 33
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no
    '''
    if len(player)==0:
        return False
    while len(player)!=0:
        a=input("Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind?")
        if a=="yes":
            cards=input("Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space:").strip().split()
            if is_valid(cards, player)==True:
                if is_discardable_seq(cards)==True:
                    for i in cards:
                        player.remove(i)
                        print("Here is your new hand printed in two ways:",print_deck_twice(player))
                        return True
                if is_discardable_kind(cards)==True:
                    for i in cards:
                        player.remove(i)
                        print("Here is your new hand printed in two ways:",print_deck_twice(player))
                        return True
                if is_discardable_seq(cards)==False:
                    if is_discardable_kind(cards)==False:
                        print("Invalid sequence. Discardable sequence needs to have at least 3 cards.")
                        print("Invalid meld:",cards[0]%100,"is not equal to",cards[1]%100)
                        return False
            if is_valid(cards, player)==False:
                return False
                
                 
                
                    
        if a=="no":
            return False
        
                        
                        
            
        


# main
print("Welcome to Single Player Rummy with Dice and strange deck.\n")
size_change=input("The standard deck  has 52 cards: 13 ranks times 4 suits.\nWould you like to change the number of cards by changing the number of ranks? ").strip().lower()

# YOUR CODE GOES HERE and in all of the above functions instead of keyword pass
if size_change==" ÿes":
    num=int(input("Which rank you want:"))
else:
    num=13
print("You are playing with a deck of ",num*4," cards")
deck=shuffle_deck(make_deck(num))
player=deal_cards_start(deck)
deck = deck[0:len(deck)-7]
print_deck_twice(player)
r=1
while len(player) != 0:
    if len(deck) != 0:
        print("Welcome to round ",r,".")
        print("Please roll the dice.")
        n=random.randint(1,6)
        print("You rolled the dice and it shows: ",n)
        if n == 1:
            rolled_one_round(player)
            print("Round ",r," completed.")
            r=r+1
        else:
            print("Since you rolled", n," the following ","n", "or", len(deck), "if the deck has less than",n, "cards will be added to your hand from top of the deck.")
            deal_new_cards(deck,player,n)
            print_deck_twice(player)
            rolled_nonone_round(player)
            print(r," completed.")
            r=r+1
    else:
        print("Welcome to round ",rounds," .")
        print("The deck is empty deck.")
        rolled_nonone_round(player)
        rolled_one_round(player)
        print(r,"completed.")
        r=r+1
     
print("Congratulations, you completed the game in",r," rounds.")

    


  
