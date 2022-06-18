from collections import deque
import random

def goal_setting(que_map, width, height):
    x_pos = random.randint(0, width-1)
    y_pos = random.randint(0, height-1)
    que_map[y_pos][x_pos] = 2
    return que_map

def wall_setting(que_map, width, height):
    x_pos = random.randint(0, width-1)
    y_pos = random.randint(0, height-1)
    if que_map[y_pos][x_pos] != 2:
        que_map[y_pos][x_pos] = 3
        return que_map
    else:
        que_map = wall_setting(que_map, width, height)
        return que_map

def move(y_pos, x_pos, pos):
    y_pos += pos[0]
    x_pos += pos[1]
    return y_pos, x_pos


# 맵 크기
width = 5
height = 5

# 시작 위치
x_pos = 0
y_pos = 0

# 이동 횟수
times = 0

# 벽 갯수
walls = 3

# 맵 세팅
que_map = deque()
for y in range(height):
    que_map.append(list(0 for x in range(width)))

# 목표 세팅
que_map = goal_setting(que_map, width, height)

# 벽 세팅
for i in range(walls):
    que_map = wall_setting(que_map, width, height)

# 이동 함수 사용 방법
# y_pos, x_pos = move(y_pos. x_pos, que_move.pop())
# 이동 가능 위치 큐
que_move = deque()

while True:
    # 지난곳 표시
    que_map[y_pos][x_pos] = 1

    # -- 사방 체크 하기 --
    # 오른쪽
    if que_map[y_pos][x_pos + 1] == 0:
        que_move.append([y_pos,x_pos + 1])

    # 왼쪽
    if que_map[y_pos][x_pos - 1] == 0:
        que_move.append([y_pos, x_pos - 1])

    # 아래
    if que_map[y_pos + 1][x_pos] == 0:
        que_move.append([y_pos + 1, x_pos])

    # 위
    if que_map[y_pos - 1][x_pos] == 0:
        que_move.append([y_pos - 1, x_pos])


    # 1. 갈수 있는곳 큐에 넣기

    # 2. 이동 하고 큐에서 빼기

    # 1번 2번 반복

    # int 2 를 만나면 Break 하기
