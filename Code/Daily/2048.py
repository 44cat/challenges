import curses
from random import randrange,choice
from collections import defaultdict

#user behavior
actions = ['Up','Left','Down','Right','Restart','Exit']

#ord()读取字符
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

# zip()压包,将输入与行为进行关联
actions_dict = dict(zip(letter_codes,actions * 2))

def main(stdscr):

	def init():
		# 重置游戏棋盘
		return 'Game'

	def not_game(state):
		'''
		画出 GameOver 或者 Win 的界面
		读取用户输入得到action,判断是重启还是结束游戏'''
		responses = defaultdict(lambda:state) #默认是当前状态,没有行为就会一直在当前界面循环
		#print(responses)
		responses['Restart'],responses['Exit'] = 'Init','Exit'#平行赋值，对应不同的行为转换到不同的状态
		return responses[action]

	def game():
		#画出当前棋盘状态
		#读取用户输入得到action
		if action == 'Restart'
			return 'Init'
		if action == 'Exit'
			return 'Exit'
		#if 成功移动了一步
			if 游戏胜利了:
				return 'Win'
			if 游戏失败了:
				return 'Gameover'
		return 'Game'

	state_actions = {
		'Init':init,
		'Win':lambda:not_game('Win'),
		'Gameover':lambda:not_game('Gameover'),
		'Game':game
}
	state = 'Init'

	# 状态机开始循环
	while state != 'Exit':
		state = state_actions[state]()

#用户输入处理
def get_user_action(keyboard):
	char = "N"
	while char not in actions_dict:
		char = keyboard.getch()
	return actions_dict[char]


