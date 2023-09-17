n = int(input())
board =  [[0 for _ in range(19)] for _ in range(19)] #매우중요성능완전굿대박 / comprehension

for _ in range (n) :
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

for i in board:
    print(*i)
