def card_value(card):
  return '23456789TJQKA'.find(card[0])

def hitem_value(item):
  return card_value(item[1])+10**item[0]

def histogram(hand):
  histo = {}
  for card in hand:
    num = card[0]
    histo[num] = (num in histo) and histo[num]+1 or 1;
  items = [[v,k] for k, v in histo.items()]
  items.sort(key=hitem_value)
  items.reverse()
  return items

def rank(hand):
  histo = histogram(hand)
  if histo[0][0]==4:    #4 of a kind
    return 7
  elif histo[0][0]==3:
    if histo[1][0]==2:      #full house
      return 6
    else:      #3 of a kind
      return 3
  elif histo[0][0]==2:
    if histo[1][0]==2:      #2 pairs
      return 2
    else:            #1 pair
      return 1
  else:
    flush = True
    suit = hand[0][1]
    for card in hand:
      if card[1]!=suit:
        flush=False
        break
    straight = False
    hand.sort(key=card_value)
    v1 = card_value(hand[0])
    v5 = card_value(hand[4])
    if (v5-v1)==4:
      straight = True
    elif  hand[4][0]=='A' and hand[3][0]=='5':
      straight = True
    if straight:
      if flush:        #straightflush
        return 8
      else:        #straight
        return 4
    elif flush:        #flush
      return 5
    else:        #high card
      return 0

def deepcomp(hand1,hand2,rank):
  if rank <=3 or rank==6 or rank==7:    #highcard, pairs, 3oak, fh, 4oak
    histo1 = histogram(hand1)
    histo2 = histogram(hand2)
    for i in range(0,len(histo1)):
      v1 = hitem_value(histo1[i])
      v2 = hitem_value(histo2[i])
      if v1>v2:        
        return 1
      elif v2>v1:
        return 2
    return 0
  elif rank==4:    #straight
    hand1.sort(key=card_value)
    hand2.sort(key=card_value)
    v1 = card_value(hand1[1])
    v2 = card_value(hand2[1])
    if v1>v2:        
      return 1
    elif v2>v1:
      return 2
  elif rank==5 or rank==8:    #flush , straightflush
    hand1.sort(key=card_value)
    hand2.sort(key=card_value)
    for i in range(0,len(hand1)):
      v1 = card_value(hand1[i])
      v2 = card_value(hand2[i])
      if v1>v2:        
        return 1
      elif v2>v1:
        return 2
    return 0
  else:
    return -1

def winner(hand1, hand2):
  r1 = rank(hand1)
  r2 = rank(hand2)
  if r1 > r2:    
    return 1
  elif r1 < r2:
    return 2
  else:
    return deepcomp(hand1, hand2, r1)

import time

t0 = time.time()
f = open('poker.txt','r')
player1 = 0
for line in f:
    hands = line[:29].split()
    if winner(hands[:5], hands[5:10])==1:
      player1 += 1
    
f.close()
print('player1 wins', player1, 'times')
print('execution time', time.time()-t0, 's')
