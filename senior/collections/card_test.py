import collections
from random import choice

# collections模块下的namedtuple方法可以创建简单的只有属性的类，参数格式为('大写首字母的类名',['字段1变量名'……'字段n变量名'])
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
	# 点数为2到10的数字，加上JQKA，得到字符串list
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')

	# 花色为四种，用str.split()方法分开
	suits = 'spades diamonds clubs hearts'.split()

	# 初始化方法，私有属性_cards
	def __init__(self):
		# 实例化Card类型对象，点数，花色，都来自于两个for循环给出的ranks 和 suits的list类型成员变量
		# _cards被一组Card对象所填充，成为装满Card对象的list
		self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

	# __len__()的作用是返回容器中元素的个数，要想使len()函数成功执行，必须要在类中定义__len__()
	def __len__(self):
		return len(self._cards)

	# __getitem__方法抽取指定对象
	def __getitem__(self, position):
		return self._cards[position]


def random_choice():
	deck = FrenchDeck()
	# random.choice方法可以直接随机选择一个元素；
	print(choice(deck))


def slicing():
	deck = FrenchDeck()
	# 最后三张牌
	print(deck[:3])
	# 先抽出索引是12的牌（’A‘,'spades'），再每隔13张抽一张，就得到了所有的A的牌
	print(deck[12::13])


def show_all_01():
	deck = FrenchDeck()
	print(type(deck._cards))
	for element in deck._cards:
		print(element)
	print(len(deck))


def show_all_02():
	deck = FrenchDeck()
	print(type(deck._cards))
	# 反向
	for element in reversed(deck):
		print(element)


# 排序
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

deck = FrenchDeck()


def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
	print(card)

# show_all_01()
# show_all_02()

# random_choice()
# slicing()
