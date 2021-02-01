import sys

answer = ["0", "0", "0", "0"]
score = []

def dfs(temp_board, score_board, i, j, t):
	for o in range(len(score_board)):
		if score_board[o] < temp_board[o]:
			return
	if j==5:
		i += 1
		j = i+1
	else:
		j += 1
	if j == 6:
		for k in range(len(score_board)):
			if score_board[k] != temp_board[k]:
				return
		answer[t] = "1"
		return
	for p in range(3):
		if p == 0:
			temp_board[i*3]+=1
			temp_board[j*3+2]+=1
			dfs(temp_board, score_board, i, j, t)
			temp_board[i*3]-=1
			temp_board[j*3+2]-=1
		if p == 1:
			temp_board[i*3+1]+=1
			temp_board[j*3+1]+=1
			dfs(temp_board, score_board, i, j, t)
			temp_board[i*3+1]-=1
			temp_board[j*3+1]-=1
		if p == 2:
			temp_board[i*3+2]+=1
			temp_board[j*3]+=1
			dfs(temp_board, score_board, i, j, t)
			temp_board[i*3+2]-=1
			temp_board[j*3]-=1
	return

def solution(score_board, t):
	temp = []
	for _ in range(18):
		temp.append(0)
	for p in range(3):
		if p == 0:
			temp[0]+=1
			temp[5]+=1
			dfs(temp, score_board, 0, 1, t)
			temp[0]-=1
			temp[5]-=1
		if p == 1:
			temp[1]+=1
			temp[4]+=1
			dfs(temp, score_board, 0, 1, t)
			temp[1]-=1
			temp[4]-=1
		if p == 2:
			temp[2]+=1
			temp[3]+=1
			dfs(temp, score_board, 0, 1, t)
			temp[2]-=1
			temp[3]-=1

for _ in range(4):
	score.append(list(map(int, sys.stdin.readline().split())))

for i in range(4):
	solution(score[i], i)

print(" ".join(answer))
