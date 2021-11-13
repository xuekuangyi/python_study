from collections import deque


def search(lines, pattern, history=5):
	# deque()创建了一个固定上长度的队列，。当有新的记录加入而队列已满的时候，会自动移除最老的记录
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			# yield 表达式 生成器
			yield line, previous_lines
		previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
	with open('somefile.txt') as f:
		for line, prevlines in search(f, 'python', 5):
			for pline in prevlines:
				print(pline, end='')
			print(line, end='')
			print('-' * 20)
