"""
1.1 一摞Python风格的纸牌 __getitem__ 和 __len__ ***


"""

import collections

# Card类定义
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
	# Lambda表达式['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self.cards = [Card(rank, suit) for suit in self.ranks
		              for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]


# 实例化Card对象
beer_card = Card(rank='7', suit='diamonds')
deck = FrenchDeck()
print(len(deck))