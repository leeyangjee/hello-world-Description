import turtle as t
t.shape("turtle")

t.bgcolor("black") # 배경색은 검은색
t.speed(0) # 속도 빠르게

t.up() # 그림그리지 않는다
t.left(180) # 반시계방향으로 180 회전
t.forward(345) # 345만큼 직진
t.right(90) # 시계방향으로 90도 회전
t.forward(290) # 290만큼 직진
t.right(90) # 시계방향으로 90도 회전
t.down() # 상단으로 이동

for x in range(15): # 한 줄씩 15번 반복
    for x in range(6): # 6번 반복
        if x % 7 == 0: # 나머지가 0
            t.color("red") # 나머지가 0일 때 빨간색
        if x % 7 == 1: # 나머지가 1
            t.color("orange") # 나머지가 1일 때 주황색
        if x % 7 == 2: # 나머지가 2
            t.color("yellow") # 나머지가 2일 때 노란색
        if x % 7 == 3: # 나머지가 3
            t.color("green") # 나머지가 3일 때 초록색
        if x % 7 == 4: # 나머지가 4
            t.color("skyblue") # 나머지가 4일 때 하늘색
        if x % 7 == 5: # 나머지가 5
            t.color("blue") # 나머지가 5일 때 파란색
        if x % 7 == 6: # 나머지가 6
            t.color("purple") # 나머지가 6일 때 보라색 # 7의 배수로 색 바꾸기
        t.forward(50) # 50만큼 직진
        t.right(90) # 시계방향으로 90도 회전
        t.forward(50) # 50만큼 직진
        t.right(90) # 시계방향으로 90도 회전
        t.forward(50) # 50만큼 직진
        t.left(90) # 반시계방향으로 90도 회전
        t.forward(50) # 50만큼 직진
        t.left(90) # 네모만들기
    
    t.up() # 그림그리지 않는다
    t.forward(50) # 50만큼 직진
    t.left(90) # 반시계방향으로 90도 회전
    t.forward(600) # 600만큼 직진
    t.right(90) # 시계방향으로 90도 회전
    t.down() # 그림그린다 # 처음 상단으로 이동


