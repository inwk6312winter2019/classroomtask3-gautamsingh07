class card():
 
 suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
 rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']

 def __init__(self, rank=0,suit=2):
  self.rank= rank
  self.suit= suit

 def __str__(self):
  return f" The rank is { card.rank_names[self.rank] } and the suit is { card.suit_names[self.suit] } "=
 
 def __lt__(self,other):
  if self.suit < other.suit: return True
  if self.suit > other.suit: return False
  return self.rank < other.suit 
 
 def __eq__(self,other):
  return self.rank == other.rank and self.suit == other.suit

ace_of_spade = card(1,3)
print(ace_of_spade)
